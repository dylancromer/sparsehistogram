from collections import defaultdict

def sparse_hist(coords, resolution, use_weights, return_bin_index):
    """
    Accepts a python list of 3D spatial points, e.g.
    [[x1,y1,z1],...], optionally with weights e.g. [[x1,x2,x3,w1],...],
    and returns the sparse histogram (i.e. no empty bins) with bins of
    resolution (spacing) given by resolution.

    The weights option allows you to chose to histogram over counts instead
    of weights (equivalent to all weights being 1).

    The bin_index option lets you return the points with their bin indices
    (the integers representing how many bins in each direction to walk to
    find the specified bin) rather than centerpoint coordinates.
    """

    def _binindex(coord):
        coord = coord[:3]
        bin_index = [int(x//resolution) for x in coord]
        bin_index = tuple(bin_index)
        return bin_index

    def _bincenter(coord):
        coord = coord[:3]
        bin_center = [(x//resolution + 0.5) * resolution for x in coord]
        bin_center = tuple(bin_center)
        return bin_center

    if return_bin_index:
        binning_function = _binindex
    else:
        binning_function = _bincenter

    if use_weights:
        coord_list = ((binning_function(x), x[3]) for x in coords)
    else:
        coord_list = ((binning_function(x), 1) for x in coords)

    binned_coords = defaultdict(float)
    for coord, weight in coord_list:
        binned_coords[coord] += weight

    return binned_coords
