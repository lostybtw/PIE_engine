def createWindow(height,width,colour):
    import tkinter as tk
    root = tk.Tk()
    root.title("PieEngine")
    c = tk.Canvas(root,bg = colour,height = height,width = width)
    c.pack()
def triangle(canvas,points,color):
    canvas.create_polygon(points,fill=color)
def pyramid(canvas,points1,points2):
    triangle(canvas,points1,"#0d0d0c")
    triangle(canvas,points2,"#1c1b17")
