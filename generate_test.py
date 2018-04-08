import numpy as np

points = 10*np.random.rand(int(1e3), 4)
np.savetxt('testpoints.csv', points, delimiter=',')
