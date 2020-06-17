class GraphObject:
    color  = 'black'
    dotAx = 1
    dotAy = 1
    def __init__(self, color, x, y ):
        self.SetColor(color)
        self.dotAx = x
        self.dotAy = y
    def SetColor (self, color):
        self.color = color
    def GetColor(self):
        return self.color
    def Draw (self):
        return 0


class Line(GraphObject):
    dotBx = 1
    dotBy = 1
    def __init__(self, color, x1, y1, x2, y2):
        GraphObject.__init__(self, color, x1, y1)
        self.dotBx = x2
        self.dotBy = y2
    def Draw(self, tarCanvas):
        tarCanvas.create_line(self.dotAx, self.dotAy, self.dotBx, self.dotBy, fill = self.color, width = 1)



class Triangle(Line):
    dotCx = 1
    dotCy = 1
    def __init__(self, color, x1, y1, x2, y2, x3, y3):
        Line.__init__(self, color, x1,y2,x2,y2)
        self.dotCx = x3
        self.dotCy = y3
    def Draw(self, tarCanvas):
        tarCanvas.create_line(self.dotAx, self.dotAy, self.dotBx, self.dotBy, fill = self.color, width = 1)
        tarCanvas.create_line(self.dotBx, self.dotBy, self.dotCx, self.dotCy, fill = self.color, width = 1)
        tarCanvas.create_line(self.dotCx, self.dotCy, self.dotAx, self.dotAy, fill = self.color, width = 1)


class Rectangle(GraphObject):
    height = 0
    width = 0
    dotBx = 1
    dotBy = 1
    def __init__(self, color, x, y, height, width):
        GraphObject.__init__(self, color, x, y)
        self.height = height
        self.width = width
        self.dotBx = self.dotAx + width
        self.dotBy=self.dotAy+height
    def Draw(self, tarCanvas):
        tarCanvas.create_rectangle(self.dotAx, self.dotAy, self.dotBx, self.dotBy, outline = self.color, fill = '', width = 1)


class Circle(GraphObject):
    dotBx=1
    dotBy=1
    def __init__(self, color, x, y, radius):
        GraphObject.__init__(self, color, x-radius, y-radius)
        self.dotBx = x + radius
        self.dotBy = y + radius
    def Draw(self, tarCanvas):
        tarCanvas.create_oval(self.dotAx, self.dotAy, self.dotBx, self.dotBy, outline=self.color, fill='', width=1)


class Ellipse(Circle):
    def __init__(self, color, x, y, _x, _y):
        GraphObject.__init__(self, color, x-_x, y-_y)
        self.dotBx=x+_x
        self.dotBy=y+_y
    def Draw(self, tarCanvas):
        tarCanvas.create_oval(self.dotAx, self.dotAy, self.dotBx, self.dotBy, outline=self.color, fill='', width=1)


class Polygon(GraphObject):
    points = None
    def __init__(self, color, points):
        GraphObject.__init__(self, color, None, None)
        self.points = points
    def Draw(self, tarCanvas):
        tarCanvas.create_polygon(self.points, outline=self.color, fill='', width=1)
