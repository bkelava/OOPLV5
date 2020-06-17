import GraphObjects as GrObj
Line = GrObj.Line
Triangle = GrObj.Triangle
Rectangle = GrObj.Rectangle
Circle = GrObj.Circle
Ellipse = GrObj.Ellipse
Polygon = GrObj.Polygon

from tkinter import *
from tkinter import filedialog

class Application(Frame):
    def CreateWidgets(self):
        self.canvas = Canvas(height = 600, width = 800, background = 'LightSlateGray')
        self.canvas.pack()

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.CreateWidgets()

    def drawObjFromFile(self, cmdFile):
        for line in cmdFile:
            self.drawObj(line.strip())

    def drawObj(self, cmdStr):
        splitStr = cmdStr.strip().split(' ')
        objectType = splitStr[0]
        objectColor = splitStr[1]
        objectCoordinate = tuple(float(ea) for ea in splitStr[2:])
        print(objectCoordinate)
        if objectType == 'Line':
            line = Line(objectColor, objectCoordinate[0],objectCoordinate[1],objectCoordinate[2],objectCoordinate[3])
            line.Draw(self.canvas)
        elif objectType == 'Triangle':
            triangle = Triangle(objectColor,objectCoordinate[0],objectCoordinate[1],objectCoordinate[2],objectCoordinate[3],objectCoordinate[4],objectCoordinate[5] )
            triangle.Draw(self.canvas)
        elif objectType == 'Rectangle':
            rectangle = Rectangle(objectColor,objectCoordinate[0],objectCoordinate[1],objectCoordinate[2],objectCoordinate[3])
            rectangle.Draw(self.canvas)
        elif objectType == 'Circle':
            circle = Circle(objectColor, objectCoordinate[0],objectCoordinate[1],objectCoordinate[2])
            circle.Draw(self.canvas)
        elif objectType == 'Ellipse':
            ellipse = Ellipse(objectColor, objectCoordinate[0],objectCoordinate[1],objectCoordinate[2],objectCoordinate[3])
            ellipse.Draw(self.canvas)
        elif objectType == 'Polygon':
            coordinates = [float(i) for i in objectCoordinate]
            polygon = Polygon(objectColor, coordinates)
            polygon.Draw(self.canvas)



def fileOpen():
    file = filedialog.askopenfile(mode='r')
    app.drawObjFromFile(file)
def fileExit():
    root.destroy()

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    m = Menu(root)
    filemenu = Menu(m, tearoff=0)
    filemenu.add_command(label="Open", command = fileOpen)
    filemenu.add_command(label="Quit", command = fileExit)
    m.add_cascade(label="File", menu=filemenu)
    root.config(menu=m)
    app.mainloop()