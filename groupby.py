import numpy as np
from importgals import import_csv_nonp
import time


gals  = import_csv_nonp('testpoints.csv')
gals = [[float(coord) for coord in gal] for gal in gals]

def groupbybin(points, res):
    start = time.time()
    nbins = np.ceil(10/res)

    def binindex(point):
        point = point[:3]
        bi = [int(x//res) for x in point]
        bi = tuple(bi)
        return bi

    from collections import defaultdict
    pointlist = [(binindex(x), x[3]) for x in points]
    pointdict = defaultdict(list)
    for k,v in pointlist:
        pointdict[k].append(v)
    chk1 = time.time()
    print('Dictionary create time: ' + str(chk1 - start))

    for key,val in pointdict.items():
        val = sum(val)
        pointdict.update({key:val})
    chk2 = time.time()
    print('Dictionary update time: ' + str(chk2 - chk1))
    print('Total elapsed time: ' + str(chk2 - start))
    return pointdict

groupbybin(gals, 1)
