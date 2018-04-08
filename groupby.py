import numpy as np
from importgals import import_csv_nonp
import time

start = time.time()
points = import_csv_nonp('testpoints.csv')
points = [[float(coord) for coord in point] for point in points]
chk1 = time.time()
print('Import time: ' + str(chk1 - start))
res = 1
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
chk2 = time.time()
print('Dictionary create time: ' + str(chk2 - chk1))

for key,val in pointdict.items():
    val = sum(val)
    pointdict.update({key:val})
chk3 = time.time()
print('Dictionary update time: ' + str(chk3 - chk2))

print('Total elapsed time: ' + str(chk3 - start))
