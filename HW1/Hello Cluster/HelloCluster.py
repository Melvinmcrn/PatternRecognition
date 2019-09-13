import matplotlib.pyplot as plt
import numpy as np
import math
#import pandas as pd


def getDistance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def getCentroid(x, y):
    out = [-1,0]
    minDistance = 999999999999999
    for i in range(len(centroid)):
        distance = getDistance(x, y, centroid[i][0], centroid[i][1])
        if distance < minDistance:
            minDistance = distance
            out = [i,distance]
    #print("x = " + str(x) + " y = " + str(y) + " : ",end="")
    if out[0] == -1:
        print("ERROR @ POSITION" + str(x) + " " + str(y))
    return out


data = [(1, 2),
        (3, 3),
        (2, 2),
        (8, 8),
        (6, 6),
        (7, 7),
        (-3, -3),
        (-2, -4),
        (-7, -7)]
dataxcentroid = dict()
#centroid = [[3, 3], [2, 2], [-3, -3]]
centroid = [[-3, -3], [2, 2], [-7, -7]]
color = ['bo','go','ro']
count = 1

while(True):

    notChange = True
    
    # ASSIGN
    for position in data:

        newCentroid = getCentroid(position[0], position[1])
        if position in dataxcentroid:
            if dataxcentroid[position][0] != newCentroid[0]:
                #print("POSITION: " + str(position) + ", oldCentroid: " + str(dataxcentroid[position][0]) + ", newCentroid: " + str(newCentroid[0]))
                notChange = False
                dataxcentroid[position] = newCentroid
        else:
#            print("NEW POSITION: " + str(position) + ", Centroid = " + str(newCentroid))
            notChange = False
            dataxcentroid[position] = newCentroid

    if notChange:
        break

    #UPDATE
    totalDistance = []
    for i in range(len(centroid)):
        totalDistance.append([0,0,0])

    for c in dataxcentroid:
        x = c[0]
        y = c[1]
        c_position = dataxcentroid[c][0]
        totalDistance[c_position][0] += 1
        totalDistance[c_position][1] += x
        totalDistance[c_position][2] += y
    
    for i in range(len(totalDistance)):
        centroid[i][0] = totalDistance[i][1] / totalDistance[i][0]
        centroid[i][1] = totalDistance[i][2] / totalDistance[i][0]

    # ********************************************** SHOW DATA***************************************************
    print("********************** ROUND : " + str(count) + " ********************************")
    for i in range(len(centroid)):
        print("CENTROID " + str(i+1) + " : ( " + str(centroid[i][0]) + " , " + str(centroid[i][1]) + " )")
        for x in dataxcentroid:
            if dataxcentroid[x][0] == i:
                print("( " + str(x[0]) + " , " + str(x[1]) + " )")

    # SHOW CENTROID
    temp = [[],[]]
    for c in centroid:
        temp[0].append(c[0])
        temp[1].append(c[1])
    plt.plot(temp[0],temp[1],'mo')

    # SHOW DATA
    temp = [[[],[]],[[],[]],[[],[]]]
    for c in dataxcentroid:
        temp[dataxcentroid[c][0]][0].append(c[0])
        temp[dataxcentroid[c][0]][1].append(c[1])
    #plt.plot(c[0],c[1],color[dataxcentroid[c][0]])
    plt.plot(temp[0][0],temp[0][1],color[0])
    plt.plot(temp[1][0],temp[1][1],color[1])
    plt.plot(temp[2][0],temp[2][1],color[2])

    plt.title('Cluster & Centroid')
    plt.legend(['Centroid','Cluster 1', 'Cluster 2','Cluster 3'])
    plt.show()

    count += 1

# ************************************************ END WHILE **************************************************

print("OUT OF WHILE")
# for c in dataxcentroid:
#     plt.plot(c[0],c[1],color[dataxcentroid[c][0]])
# for c in centroid:
#     plt.plot(c[0],c[1],'mo')
# plt.show()
# print()
# print("************************** CENTROID ***********************************")
# print(centroid)
# print("************************** dataxcentroid********************************")
# print(dataxcentroid)


# for position in data:
#     plt.plot(position[0], position[1],'bo')

# plt.show()

# pd.Series(np.random.randn(5))

# print("hello")

# print(pd.Series(np.random.randn(5)))
# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
# s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
# print(s)

# d = {'one' : [1., 2., 3., 4.],
#      'two' : [4., 3., 2., 1.]}
# print(d)
# print(pd.DataFrame(d))
# print(pd.DataFrame(d).describe())
