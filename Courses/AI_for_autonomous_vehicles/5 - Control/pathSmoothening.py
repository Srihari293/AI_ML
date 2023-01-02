import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print ('['+ ', '.join('%.3f'%x for x in old) + '] -> ['+ ', '.join('%.3f'%x for x in new) +']')

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.2, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = deepcopy(path)

    #######################
    ### ENTER CODE HERE ###
    #######################
    while True:
        totalChange = 0.
        for i in range(len(path)):
            if i != 0 and i != (len(path) - 1):
                for dim in range(len(path[i])):
                    oldVal = newpath[i][dim]
                    newpath[i][dim] = newpath[i][dim] + \
                        weight_data * (path[i][dim] - newpath[i][dim]) + \
                        weight_smooth * (newpath[i+1][dim] + newpath[i-1][dim] - 2 * newpath[i][dim])
                    totalChange += abs(oldVal - newpath[i][dim])
        if totalChange < tolerance:
            break
    return newpath # Leave this line for the grader!
# printpaths(path,smooth(path))

# # Visualization
# smoothpath_arr = np.asarray(smooth(path))
# path_arr = np.asarray(path)
# for i in range(len(path)):
#     plt.scatter(path_arr[i][0], path_arr[i][1], c = "red")
#     plt.scatter(smoothpath_arr[i][0], smoothpath_arr[i][1], c = "blue")
# plt.show()