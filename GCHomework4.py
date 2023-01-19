import random
import math
import matplotlib.pyplot as plt

def findLowest(totalList):
    yList = []
    xList = []
    for i in totalList:
        yList.append(i["y"])
        xList.append(i["x"])
    lowest = 0
    for i in range(len(yList)):
        if yList[i] < yList[lowest]:
            lowest = i
        elif yList[i] == yList[lowest]:
            if xList[i] > yList[lowest]:
                lowest = i
    return lowest

def leftOf(a, b, c):
    area = (b["x"]-a["x"])*(c["y"]-a["y"])-(b["y"]-a["y"])*(c["x"]-a["x"])
    if area > 0:
        return False
    else:
        return True

def dotProduct(a, b):
    return a["x"] * b["x"] + a["y"] * b["y"]
def lengthOfLine(a):
    return  math.sqrt(a["x"]**2) + (a["y"]**2)

def doFormula(a, b):
    return math.degrees(math.atan2(b["y"] - a["y"], b["x"] - a["x"]) - math.atan2(a["y"]-a["y"],(a["x"]-1)- a["x"]))
    
def specialSort(points, angles):
    for i in range(len(points)):
        for j in range(i, len(points)):
            if angles[i] > angles[j]:
                temp = angles[i]
                angles[i] = angles[j]
                angles[j] = temp
                
                temp = points[i]
                points[i] = points[j]
                points[j] = temp
                
    return points, angles
    
    
def convertToMat(dict):
    xValues = []
    for x in dict:
        xValues.append(x["x"])
    yValues = []
    for y in dict:
        yValues.append(y["y"])
    return [xValues, yValues]

def recurse(point, hull):
    current = len(hull)-1
    while not leftOf(point, hull[current], hull[current - 1]) and current > 0:
        hull.pop(current)
        current -= 1
    return hull

points = []
random.seed()
for i in range(10):
    points.append({"x" : random.random()*50, "y" : random.random()*50})
    
    
pointsLength = len(points)

#converted = convertToMat(points)
#plt.plot(converted[0], converted[1], "ro")
#plt.show()
    

pivotIndex = findLowest(points)
pivotPoint = points[pivotIndex]
anglePoint = {
    "x" : pivotPoint["x"]-1,
    "y" : pivotPoint["y"]
}
points.pop(pivotIndex)
print(str(pivotPoint["x"]) + " " + str(pivotPoint["y"]) + " index: " + str(pivotIndex))

angles = []

for i in range(len(points)):
    angles.append(doFormula(pivotPoint, points[i])*-1)

points, angles = specialSort(points, angles)

print(angles)

hull = [pivotPoint, points[len(points)-1], points[len(points)-2]]

counter = len(points)-3
while counter >= 0:
    hull = recurse(points[counter], hull)
    hull.append(points[counter])
    counter -= 1

hullLength = len(hull)

if hullLength == pointsLength:
    print("It is true!!!!")

hull.append(pivotPoint)
points.append(pivotPoint)
converted = convertToMat(hull)
plt.plot(converted[0], converted[1])
converted1 = convertToMat(points)
plt.plot(converted1[0], converted1[1], "ro")
plt.show()