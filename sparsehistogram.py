from collections import defaultdict

"""Accepts a python list of 3D spatial points, e.g. [[x1,y1,z1],...], optionally with weights e.g. [[x1,x2,x3,w1],...], and returns the sparse histogram (i.e. no empty bins) with bins of resolution (spacing) given by res.
The weights option allows you to chose to histogram over counts instead of weights (equivalent to all weights being 1).
The bin_index option lets you return the points with their bin indices (the integers representing how many bins in each direction to walk to find the specified bin) rather than centerpoint coordinates."""
def sparse_hist(points, res, weights=True, bin_index=True):
    def _binindex(point):
        point = point[:3]
        bi = [int(x//res) for x in point]
        bi = tuple(bi)
        return bi

    def _bincenter(point):
        point = point[:3]
        bc = [(x//res+0.5)*res for x in point]
        bc = tuple(bc)
        return bc

    if not bin_index:
        if weights:
            pointlist = [(_bincenter(x), x[3]) for x in points]
        else:
            pointlist = [(_bincenter(x), 1) for x in points]
    else:
        if weights:
            pointlist = [(_binindex(x), x[3]) for x in points]
        else:
            pointlist = [(_binindex(x), 1) for x in points]

    pointdict = defaultdict(list)
    for k,v in pointlist:
        pointdict[k].append(v)

    for key,val in pointdict.items():
        val = sum(val)
        pointdict.update({key:val})
    return pointdict

