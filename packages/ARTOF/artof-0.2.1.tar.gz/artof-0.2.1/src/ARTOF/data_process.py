import numpy as np
    
def get_bin_edges(data: list, bin_config: list, data_id: str = "unknown") -> np.ndarray:
    """
    Create bin edges (limits) for given bin config.

    Args:
        data: 1D list of data values.
        bin_config: Bin config consisting of three values: [min, max, points].
        data_id: Identifier to raise error message with identifier.

    Returns:
        List of bin edges.
    """
    min_point, max_point, total_points = bin_config
    if type(total_points) != int:
        raise Exception(f"The number of bins for {data_id} needs given as an int")

    bin_size = (max_point - min_point) / (total_points-1)
    # create bin edges in a way that bin centers are min and max
    return np.linspace(min_point - bin_size/2, max_point + bin_size/2, total_points+1)



    
def project_data(data: np.ndarray, bin_edges: list, axes: list, ranges: list, norm_step_size: bool) -> np.ndarray:
    """
    Plot loaded data in given projection. Projections are possible in 1 or 2 dimensions.

    Args:
        data: 3D data to be transformed.
        bin_edges: List of bin edges for each axis.
        axes: List containing all axes onto which the projection is performed, e.g., [0,1].
        ranges: List of ranges for each axis.
        norm_step_size: Normalize projection with step size.

    Returns:
        1 or 2D list containing the projection.
    """

    if data is None:
        raise Exception('Load and bin the data before projecting the data.')         
    if len(axes) not in [1,2]:
        raise Exception(f'A projection onto {len(axes)} axes is not possible.')
    
    # determine ranges (None is entire range)
    start_1, end_1 = (0, data.shape[0]) if ranges[0] is None else (ranges[0][0], ranges[0][1])
    start_2, end_2 = (0, data.shape[1]) if ranges[1] is None else (ranges[1][0], ranges[1][1])
    start_3, end_3 = (0, data.shape[2]) if ranges[2] is None else (ranges[2][0], ranges[2][1])

    proj_data = data[start_1:end_1,start_2:end_2,start_3:end_3]
    
    if len(axes) == 2: # project data onto 2 axes
        # determine the projection axis
        proj_axis = 3 - sum(axes)
        # switch order of array if needed
        if axes[0] < axes[1]:
            proj_data = np.swapaxes(proj_data, axes[0], axes[1])
        proj_data = proj_data[:,:,:].sum(axis=proj_axis)
    elif len(axes) == 1: # project data onto 1 axis
        # get axes to project along
        proj_axes = [0,1,2]
        proj_axes.remove(axes[0])
        # project along axes
        proj_data = proj_data.sum(axis=tuple(proj_axes))

    # normalize data with step size if desired
    if norm_step_size:
        step_size_product = 1
        for i in axes:
            step_size_product *= bin_edges[i][1] - bin_edges[i][0]
        proj_data /= step_size_product

    return proj_data