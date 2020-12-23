def createWindow(height,width,colour):
    import tkinter as tk
    root = tk.Tk()
    root.title("PieEngine")
    c = tk.Canvas(root,bg = colour,height = height,width = width)
    c.pack()
    root.mainloop() 





createWindow(400,400,None)