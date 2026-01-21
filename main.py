import math



class Point:

    def __init__(self, xval=0, yval=0):
        self.xval = xval
        self.yval = yval
        self.__repr__()


    def calcdist(self, otherthing):
        
        if isinstance(otherthing, Point):
            # ok so for point to point distance we use pythagorean theorm
            # distance = sqrt((x2-x1)^2 + (y2-y1)^2)
            xdiff = self.xval - otherthing.xval
            ydiff = self.yval - otherthing.yval
            xsquared = xdiff ** 2
            ysquared = ydiff ** 2
            sumofsquares = xsquared + ysquared
            distresult = math.sqrt(sumofsquares)
            return distresult

        elif isinstance(otherthing, Line):
            Acoef = otherthing.Acoef
            Bcoef = otherthing.Bcoef
            Ccoef = otherthing.Ccoef
            numeratorpart = abs(Acoef * self.xval + Bcoef * self.yval - Ccoef)
            denominatorpart = math.sqrt(Acoef**2 + Bcoef**2)
            finaldist = numeratorpart / denominatorpart
            return finaldist

        elif isinstance(otherthing, Circle):
            disttocenter = self.calcdist(otherthing.centerpt)
            disttocircle = abs(disttocenter - otherthing.rad)
            return disttocircle

        elif isinstance(otherthing, Rectangle):
            # distance from point to rect we find closest point on rectangle boundary
            closestxval = max(otherthing.topleftpt.xval, min(self.xval, otherthing.toprightpt.xval))
            closestyval = max(otherthing.topleftpt.yval, min(self.yval, otherthing.bottomleftpt.yval))
            closestpt = Point(closestxval, closestyval)
            disttorect = self.calcdist(closestpt)
            return disttorect
        
        else:
            raise TypeError("dont know how to calculate distance to this type of object!!")
        


    def __repr__(self):
        return f"Point({self.xval}, {self.yval})"




class Circle:
    
    def __init__(self, centerpt=Point(0,0), rad=1):
        self.centerpt = centerpt
        self.rad = rad
        self.__repr__()

    def calcdist(self, otherthing):
        if isinstance(otherthing, Point):
            distcenterpt = self.centerpt.calcdist(otherthing)
            distresult = abs(distcenterpt - self.rad)
            return distresult

        elif isinstance(otherthing, Circle):
            # ok for circle to circle distance we need centers distance minus both radius
            centertocenter = self.centerpt.calcdist(otherthing.centerpt)
            gapbetweencircles = centertocenter - (self.rad + otherthing.rad)
            if gapbetweencircles < 0:
                gapbetweencircles = 0
            return gapbetweencircles

        elif isinstance(otherthing, Line):
            distcenterline = self.centerpt.calcdist(otherthing)
            distfromedge = distcenterline - self.rad
            if distfromedge < 0:
                distfromedge = 0
            return distfromedge
        
        elif isinstance(otherthing, Rectangle):
            closestxcord = max(otherthing.topleftpt.xval, min(self.centerpt.xval, otherthing.toprightpt.xval))
            closestycord = max(otherthing.topleftpt.yval, min(self.centerpt.yval, otherthing.bottomleftpt.yval))
            closestptonrect = Point(closestxcord, closestycord)
            distcentertoclosest = self.centerpt.calcdist(closestptonrect)
            finaldist = distcentertoclosest - self.rad
            if finaldist < 0:
                finaldist = 0
            return finaldist
        
        else:
            raise TypeError("cant calculate distance to this thing!!")
            

    def calcarea(self):
        radiussquared = self.rad ** 2
        areaval = math.pi * radiussquared
        return areaval


    def calccircumfrence(self):
        circumfrenceval = 2 * math.pi * self.rad
        return circumfrenceval


    def __repr__(self):
        return f"Circle(Center: {self.centerpt}, Radius: {self.rad})"




class Rectangle:
        
    def __init__(self, topleftpt=Point(0,0), bottomleftpt=Point(0,5)):
        self.topleftpt = topleftpt
        self.bottomleftpt = bottomleftpt
        self.wdth = abs(bottomleftpt.xval - topleftpt.xval)
        self.hght = abs(bottomleftpt.yval - topleftpt.yval)
        self.toprightpt = Point(self.topleftpt.xval + self.wdth, self.topleftpt.yval)
        
        if self.wdth <= 0 or self.hght <= 0:
            raise ValueError("rectangle dimensions must be positive!! width and height cant be 0 or negative")

        self.__repr__()

    def calcdist(self, otherthing):
        if isinstance(otherthing, Point):
            xclamped = max(self.topleftpt.xval, min(otherthing.xval, self.toprightpt.xval))
            yclamped = max(self.topleftpt.yval, min(otherthing.yval, self.bottomleftpt.yval))
            clampedpt = Point(xclamped, yclamped)
            distval = otherthing.calcdist(clampedpt)
            return distval

        elif isinstance(otherthing, Rectangle):
            # for rectangle to rectangle we check if they overlaping or not
            leftedge = max(self.topleftpt.xval, otherthing.topleftpt.xval)
            rightedge = min(self.toprightpt.xval, otherthing.toprightpt.xval)
            topedge = max(self.topleftpt.yval, otherthing.topleftpt.yval)
            bottomedge = min(self.bottomleftpt.yval, otherthing.bottomleftpt.yval)

            if leftedge < rightedge and topedge < bottomedge:
                return 0

            dxgap = max(0, leftedge - rightedge)
            dygap = max(0, topedge - bottomedge)
            totaldist = math.sqrt(dxgap * dxgap + dygap * dygap)
            return totaldist

        elif isinstance(otherthing, Circle):
            xclosest = max(self.topleftpt.xval, min(otherthing.centerpt.xval, self.toprightpt.xval))
            yclosest = max(self.topleftpt.yval, min(otherthing.centerpt.yval, self.bottomleftpt.yval))
            ptclosest = Point(xclosest, yclosest)
            disttocenter = otherthing.centerpt.calcdist(ptclosest)
            distfinal = disttocenter - otherthing.rad
            if distfinal < 0:
                distfinal = 0
            return distfinal

        elif isinstance(otherthing, Line):
            xclamp = max(self.topleftpt.xval, min(otherthing.pt1.xval, self.toprightpt.xval))
            yclamp = max(self.topleftpt.yval, min(otherthing.pt1.yval, self.bottomleftpt.yval))
            ptclamp = Point(xclamp, yclamp)
            distresult = ptclamp.calcdist(otherthing)
            return distresult

        else:
            raise TypeError("dont know how to calc distance to this!!")

    def calcarea(self):
        arearesult = self.wdth * self.hght
        return arearesult
    
    def calcperimiter(self):
        sumofsides = self.wdth + self.hght
        perimiterval = 2 * sumofsides
        return perimiterval


    def __repr__(self):
        return f"Rectangle(TopLeft: {self.topleftpt}, BottomLeft: {self.bottomleftpt})"

        


class Line:

    def __init__(self, pt1=Point(0,0), pt2=Point(1,1)):
        self.pt1 = pt1
        self.pt2 = pt2
        self.__repr__()
        self.Acoef = pt2.yval - pt1.yval
        self.Bcoef = pt1.xval - pt2.xval
        self.Ccoef = self.Acoef * pt1.xval + self.Bcoef * pt1.yval


    def calcdist(self, otherthing):
        if isinstance(otherthing, Point):
            numeratorval = abs(self.Acoef * otherthing.xval + self.Bcoef * otherthing.yval - self.Ccoef)
            denominatorval = math.sqrt(self.Acoef**2 + self.Bcoef**2)
            distresult = numeratorval / denominatorval
            return distresult

        elif isinstance(otherthing, Line):
            crossproduct = self.Acoef * otherthing.Bcoef
            crossproduct2 = self.Bcoef * otherthing.Acoef
            
            if crossproduct == crossproduct2:
                cdifference = abs(self.Ccoef - otherthing.Ccoef)
                denominator = math.sqrt(self.Acoef**2 + self.Bcoef**2)
                distbetweenlines = cdifference / denominator
                return distbetweenlines
            else:
                return 0

        elif isinstance(otherthing, Circle):
            distcentertoline = otherthing.centerpt.calcdist(self)
            disttocircle = distcentertoline - otherthing.rad
            if disttocircle < 0:
                disttocircle = 0
            return disttocircle

        elif isinstance(otherthing, Rectangle):
            xclamped = max(otherthing.topleftpt.xval, min(self.pt1.xval, otherthing.toprightpt.xval))
            yclamped = max(otherthing.topleftpt.yval, min(self.pt1.yval, otherthing.bottomleftpt.yval))
            clampedpt = Point(xclamped, yclamped)
            distval = clampedpt.calcdist(self)
            return distval

        else:
            raise TypeError("cant calculate distance to this type!!")


    def __repr__(self):
        return f"Line(Point1: {self.pt1}, Point2: {self.pt2})"



def main():

    mp = {
        'Point': Point,
        'Circle': Circle,
        'Rectangle': Rectangle,
        'Line': Line,
        'math': math
    }

    print("GeoCalc \n Type 'quit' to exit")

    while True:

        userinput = input(">").strip()

        if userinput == "":
            print("No input is given ")
            continue
        
        if userinput.lower() == "quit" or userinput.lower() == "exit":
            print("Exiting Geo Calc")
            break

        try:
            if '=' in userinput:
                exec(userinput, {}, mp)
            else:
                resultval = eval(userinput, {}, mp)
                if resultval is not None:
                    print(resultval)
        except Exception as err:
            print("Error:", err)






if __name__ == '__main__':
    main()