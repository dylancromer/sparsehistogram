import numpy as np
from importgals import import_csv_nonp


gals  = import_csv_nonp('testpoints.csv')
gals = [[float(coord) for coord in gal] for gal in gals]

def groupbybin(points, res, weights=True):
    nbins = np.ceil(10/res)

    def binindex(point):
        point = point[:3]
        bi = [int(x//res) for x in point]
        bi = tuple(bi)
        return bi

    from collections import defaultdict
    if weights:
        pointlist = [(binindex(x), x[3]) for x in points]
    else:
        pointlist = [(binindex(x), 1) for x in points]

    pointdict = defaultdict(list)
    for k,v in pointlist:
        pointdict[k].append(v)

    for key,val in pointdict.items():
        val = sum(val)
        pointdict.update({key:val})
    return pointdict

