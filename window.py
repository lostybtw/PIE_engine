class window():
    def __init__(self):
        self.height = 0
        self.width = 0
        self.colour = "white"

    def createWindow(self,height,width,colour):
       import tkinter as tk
       root = tk.Tk()
       root.title("PieEngine")
       c = tk.Canvas(root,bg = colour,height = height,width = width)
       c.pack()
       root.mainloop() 

    def triangle(self,x1,y1,x2,y2,x3,y3):
       import tkinter as tk

       root = tk.Tk()

       points = [x1,y1,x2,y2,x3,y3]
       create_polygon(points)

       root.mainloop()
  
x = window()
x.createWindow(400,400,None)
x.triangle(200,200,100,300,300,300)