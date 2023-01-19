class Polygon:
    def __init__(self, Points):
        self.Points = []
        for a in Points:
            self.Points.append(a)

    def __str__(self):
        b = ""
        for a in self.Points:
            b = b + str(a[0]) + " " + str(a[1]) + " | "

        return b
    
    def findArea(self):
        sum = 0
        for a in self.Points:
            #print(" | " + str(self.Points.index(a)))
            #print(str(a[0]) + " " + str(self.Points[self.Points.index(a)-1][1]))
            #print(str(self.Points[self.Points.index(a)-1][0]) + " " + str(a[1]))
            sum += ((a[0]*self.Points[self.Points.index(a)-1][1]) - self.Points[self.Points.index(a)-1][0]*a[1])
        sum = abs(sum)
        sum = sum*1/2
        return sum

box = Polygon([[2,0],[0,0],[0,2],[2,2]])
print(box)
print(box.findArea())

FiveSides = Polygon([[3,4],[3,0],[-1,-2],[1,3],[2,5]])
print(FiveSides)
print(FiveSides.findArea())