import random
import matplotlib.pyplot as plt

'''slope = (a["y"]-b["y"])/(a["x"] - b["x"])
yintersect = a["y"] - slope*a["x"]
line = {
    "x" : c["x"]*slope + yintersect,
    "y" : (c["y"]-yintersect)/slope
}
if line["x"] > c["x"] and line["y"] < c["y"]:'''

def leftOf(a, b, c):
    area = (b["x"]-a["x"])*(c["y"]-a["y"])-(b["y"]-a["y"])*(c["x"]-a["x"])
    if area > 0:
        return False
    else:
        return True
        
        
def convertToMat(dict):
    xValues = []
    for x in dict:
        xValues.append(x["x"])
    yValues = []
    for y in dict:
        yValues.append(y["y"])
    return [xValues, yValues]

def convertToMatTwo(dict):
    xValues = []
    yValues = []
    for v in dict:
        xValues.append(v[0]["x"])
        yValues.append(v[0]["y"])
        xValues.append(v[1]["x"])
        yValues.append(v[1]["y"])
    return [xValues, yValues]


points = []
random.seed()
for i in range(20):
    points.append({"x" : random.random()*50, "y" : random.random()*50})

hull = []

goBack = False

for a in points:
    for b in points:
        if b == a:
            continue
        for c in points:
            if c == a or c == b:
                continue
            if not leftOf(a, b, c):
                goBack = True
                break
        if goBack == True:
            goBack = False
            continue
        hull.append([a, b])
        
converted2 = convertToMatTwo(hull)
converted = convertToMat(points)

figure, axis = plt.subplots(1, 2)

axis[0].plot(converted[0], converted[1], "ro")
axis[0].set_title("All Points")
axis[1].plot(converted2[0], converted2[1])
axis[1].plot(converted2[0], converted2[1], "ro")
axis[1].set_title("Hull")

plt.tight_layout()
plt.show()