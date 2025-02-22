import numpy as np
import matplotlib.pyplot as plt
import threading
from io import TextIOWrapper

# internal
from .data_read import read_metadata, load_file
from .data_process import get_bin_edges, project_data
from .Transformer import ARTOFTransformer
from .sweep_scienta import get_sweep_parameters
from .normalize import get_norm_scaling_factor, norm_sweep

# convert name of datatype to actual type
data_type_dict = {'int32': np.int32, 'float64': np.float64}


class ARTOFLoader:
    """Class to load ARTOF data."""

    def __init__(self):
        """Initialize ARTOFLoader class"""
        self.data = None
        self.binned_data = None
        self.bin_edges = list()
        self.format = None
        self.axes = None
        self.metadata = None
        self.transformer = None

    def load_run(self, path: str, format: str, x0: int = None, y0: int = None, t0: int = None, iter_interval: tuple = None, sweep_type: str = 'Sienta', multithreading=True):
        """
        Load ARTOF data for run in directory and transform into desired format.

        Args:
            path: Path to run directory.
            format: Load parameters in given format ('raw', 'raw_SI', 'cylindrical', 'spherical').
                `raw`: Load raw data in ticks (x,y,t).
                `raw_SI`: Load raw data in SI units (x,y,t).
                `cylindrical`: Load data in cylindrical coordinates (r, phi, t).
                `spherical`: Load data in spherical coordinates and associated energy (E, theta, phi).
            x0: Offset for x ticks, optional (default None).
            y0: Offset for y ticks, optional (default None).
            z0: Offset for t ticks, optional (default None).
            iter_interval: Tuple of start (including) and stop (excluding) lens iteration to load (default None, load all).
            sweep_type: Type of sweep analysis ('Sienta' or 'normal').
            multithreading: Use multithreading for data loading (default True).
        """
        # save format 
        self.format = format
        # aquire metadata
        self.metadata = read_metadata(path)
        # setup everything need for sweep analysis
        self.acquisitionMode = self.metadata.general.acquisitionMode
        if self.acquisitionMode == 'sweep':
            if sweep_type == 'Sienta':
                general = self.metadata.general
                self.sweep_start_energy, self.sweep_end_energy, self.adjusted_channel_width, self.lens_steps, self.lens_k = get_sweep_parameters(general.spectrumBeginEnergy,
                    general.spectrumEndEnergy, general.lensLowEdgeEnergyStep, self.metadata.lensmode.lensK)
            else:
                raise Exception('Normal sweep analysis not implemented yet.')
        else: 
            self.lens_steps = 1
        # create transformer based on metadata and transformation parameters
        self.transformer = ARTOFTransformer(self.metadata, x0, y0, t0)
        # save axes and set returned bin configurations as default
        self.axes, self.default_bin_confs = self.transformer.get_axis_and_bins(format, self.metadata, t0)

        # setup range of iterations to load
        if iter_interval is None:
            iter_range = range(self.metadata.general.lensIterations)
        else:
            if iter_interval[1] > self.metadata.general.lensIterations or iter_interval[0] < 0:
                raise ValueError(f'Given range of iterations is not within range of available iterations (0 to {self.metadata.general.lensIterations-1}).')
            iter_range = range(iter_interval[0], iter_interval[1])
        # save number of iterations
        self.iterations = len(iter_range)
        # setup progress information                
        self.progress_info = {'current': 0, 'total': len(iter_range) * self.lens_steps}
        self.__print_progress()
        # transform data to desired format via multithreading if desired
        data_pieces = []
        if multithreading:
            threads = []
            for iter in iter_range:
                for step in range(self.lens_steps):                    
                    thread = threading.Thread(target=self.__process_data, args=(path, iter, step, data_pieces, format))
                    threads.append(thread)
                    thread.start()
            for thread in threads:
                thread.join()
        else:
            for iter in range(self.metadata.general.lensIterations):
                for step in range(self.lens_steps):
                    self.__process_data(path, iter, step, data_pieces, format)
        self.data = np.concatenate(data_pieces, axis=0)

        # print information about loaded data
        print() # need to stop overwriting of progress bar
        print(f'Loaded and transformed {self.data.shape[0]} data points to formats {self.axes}.')

    def save_transformed_data(self, path: str):
        """
        Save transformed data to binary file (path + '.bin') and save addional info file (path + '_info.txt')

        Args:
            path: Path to file where transformed data should be stored.
        """        
        self.data.tofile(f'{path}.bin') 
        with open(f'{path}_info.txt', 'w') as f:
            self.__write_par(f, type(self.data[0,0]).__name__)
            self.__write_par(f, self.format)
            self.__write_par(f, self.acquisitionMode)
            if self.acquisitionMode == 'sweep':
                self.__write_par(f, f'{self.sweep_start_energy},{self.sweep_end_energy},{self.adjusted_channel_width},{self.lens_steps},{self.lens_k}')
            self.__write_par(f, ",".join(self.axes))
            self.__write_par(f, ";".join(map(str, self.default_bin_confs)))

        print(f'Saved transformed data as binary file to {path}_{self.format}.bin and additional information to {path}_{self.format}_info.txt')


    def __write_par(self, file: TextIOWrapper, par):
        """
        Write parameter to file with new line at the end.

        Args:
            file: File to write to.
            par: Parameter to write.
        
        """
        file.write(par)
        file.write('\n')

    def load_transformed_data(self, data_path: str, info_path: str):
        """
        Load transformed data from file.

        Args:
            data_path: Path to file where transformed data is stored.
            info_path: Path to file where information about the transformed data is stored.
        """
        with open(info_path) as f:
            data_type = data_type_dict[next(f).strip()]
            self.format = next(f).strip()
            self.acquisitionMode = next(f).strip()
            if self.acquisitionMode == 'sweep':
                self.sweep_start_energy, self.sweep_end_energy, self.adjusted_channel_width, self.lens_steps, self.lens_k = map(float, next(f).strip().split(','))
                self.lens_steps = int(self.lens_steps)
            self.axes = next(f).strip().split(',')
            self.default_bin_confs = [eval(bin_conf) for bin_conf in next(f).strip().split(';')]
        self.data = np.fromfile(data_path, dtype=data_type).reshape(-1,3)


    def bin_data(self, bin_confs: list = [None, None, None], norm_modes: list = None):
        """
        Bin loaded data into 3D histogram.

        Args:        
            bin_confs: List of 3 binning configurations for the 3 parameters [min, max, points]. F.e.: [[-1500, 1500, 101], [-1500, 1500, 101],[12000, 18000, 201]].       
            norm_mode: Normalization mode for binned data ('iterations', 'dwell_time', 'step_size',  'sweep'). Default is None.
                `iterations`: Normalize data by number of iterations.
                `dwell_time`: Normalize data by dwell time.
                `sweep`: Normalize data by changing window size of sweep data.

        Raises:
            Exception: If data is not loaded before binning.
        """
        if self.data is None:
            raise Exception('Load the data before binning the data.')

        # use either passed or default bin configurations
        cur_bin_confs = []
        for i, bin_conf in enumerate(bin_confs):
            if bin_conf is None:
                print(f'Using default bin configuration for {self.axes[i]}: {self.default_bin_confs[i]}')
                cur_bin_confs.append(self.default_bin_confs[i])
            else:
                cur_bin_confs.append(bin_conf)
        
        # create bin edges based on the passed bin configs
        self.bin_edges = list()
        for i in range(3):
            self.bin_edges.append(get_bin_edges(self.data[:,i], cur_bin_confs[i], data_id=self.axes[i]))
        # bin data in 3D histogram
        self.binned_data, _ = np.histogramdd(self.data, bins=self.bin_edges) 

        # normalize data if desired        
        if norm_modes is not None:
            scaling_factor = get_norm_scaling_factor(norm_modes, self.iterations, self.metadata.general.lensDwellTime)
            self.binned_data *= scaling_factor
            # normalize data by sweep acceptance if desired and in sweep mode
            if 'sweep' in norm_modes: 
                if self.acquisitionMode != 'sweep' or self.format != 'spherical':
                    raise Exception('Sweep normalization only possible for sweep data in spherical format.')
                self.binned_data = norm_sweep(self.binned_data, self.bin_edges[0], self.sweep_start_energy,
                                              self.adjusted_channel_width, self.lens_steps, self.lens_k)
                
            # print all non-recognized norm modes
            for mode in norm_modes:
                if mode not in ['iterations', 'dwell_time', 'sweep']:
                    print(f'Normalization mode "{mode}" not recognized.')
            
            
                
    

    def __process_data(self, path: str, iter: int, step: int, data_pieces: list, load_as: str):        
        """
        Load and transform single data file in given format (needed for multithreading).

        Args:
            path: Path where data files are located.
            iter: Index of the lens iteration to be loaded.
            step: Index of the lens step to be loaded.
            data_pieces: List of transformed data pieces to which the newly transformed data should be appended.
            load_as: Desired transformation format.
        """
        raw_data = load_file(path, iter, step)
        if self.acquisitionMode == 'sweep':
            center_energy = self.sweep_start_energy + step * self.adjusted_channel_width
            data_pieces.append(self.transformer.transform(raw_data, load_as, center_energy=center_energy))
        else:
            center_energy = self.metadata.general.centerEnergy
            data_pieces.append(self.transformer.transform(raw_data, load_as, center_energy=center_energy))
        self.progress_info['current'] += 1
        self.__print_progress()


    def __print_progress(self):
        """
        Print progress information.
        """
        current = self.progress_info['current']
        total = self.progress_info['total']
        print('\r', end='')
        print(f'Progress: [{"="*int(current*20/total):<20}] {current}/{total}', end='\r')


    def plot(self, axes: list, ranges: list = [None, None, None], norm_step_size: bool = False, width: float = 5.5, height: float = 5.5):
        """
        Plot loaded data as projection onto given axes. Projections are possible onto 1 or 2 axes.

        Args:
            axes: List containing all axes onto which the projection is performed, e.g., [0,1].
            ranges: List containing ranges for axes (e.g., [[50, 101], [0,50], None]), if None entire range of axes is used (default entire range of each axis).
            norm_step_size: Normalize data with step size before plotting (default False).
            width: Width of plot (default 5).
            height: Height of plot (default 5).
        """
        
        proj_data = project_data(self.binned_data, self.bin_edges, axes, ranges, norm_step_size)

        if len(axes) == 2: # plot data in 2D as image
            img_fig, img_ax = plt.subplots(figsize=(width, height))
            img_fig.subplots_adjust(bottom=0.2, left=0.2)
            img_ax.imshow(proj_data, cmap='terrain', norm='linear', origin='lower', extent=[self.bin_edges[axes[0]][0], self.bin_edges[axes[0]][-1], self.bin_edges[axes[1]][0], self.bin_edges[axes[1]][-1]], aspect="auto")
            img_ax.set_xlabel(self.__axis_label(self.axes[axes[0]]))
            img_ax.set_ylabel(self.__axis_label(self.axes[axes[1]]))
        elif len(axes) == 1: # plot data in 1D as line
            x_values = [(self.bin_edges[axes[0]][i] + self.bin_edges[axes[0]][i+1])/2 for i in range(len(self.bin_edges[axes[0]])-1)]            

            line_fig, line_ax = plt.subplots(figsize=(width, height))
            line_fig.subplots_adjust(bottom=0.2, left=0.2)
            line_ax.plot(x_values, proj_data)
            line_ax.set_xlabel(self.__axis_label(self.axes[axes[0]]))
            line_ax.set_ylabel('Counts')


        else:
            raise Exception(f'A projection along {len(axes)} axes is not possible.')
        
    def export_to_csv(self, path: str, axes: list, ranges: list = [None, None, None], norm_step_size: bool = False, delimiter: str = ','):
        """
        Export loaded data as projection onto given axes. Projections are possible onto 1 or 2 axes.

        Args:
            path: Path including file name to which the data is saved.
            axes: List containing all axes onto which the projection is performed, e.g., [0,1].
            ranges: List containing ranges for axes (e.g., [[50, 101], [0,50], None]), if None entire range of axes is used (default entire range of each axis).
            norm_step_size: Normalize data with step size before plotting (default False).
            delimiter: Delimiter by which the data is separated (default ',').
        """  
        data_to_export = project_data(self.binned_data, self.bin_edges, axes, ranges, norm_step_size)        
        np.savetxt(path, data_to_export, delimiter=delimiter)

    def __axis_label(self, axis: str) -> str:
        """
        Build string for matplotlib axis label including Greek characters.

        Args:
            axis: String containing the axis label and unit separated by '_'.

        Returns:
            Formatted string for matplotlib.
        """
        name, unit = axis.split('_')
        match name:
            case 'phi':
                name = '$\\varphi$'
            case 'theta':
                name = '$\\theta$'
        return f'{name} [{unit}]'



