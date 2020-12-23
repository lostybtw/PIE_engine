#define function using def
def createWindow(height,width,colour):#arguments and ":" for writing the code
    #importing tkinter for graphics
    import tkinter as tk
    #root is base of ui
    root = tk.Tk()
    #TITLING OUR WINDOW
    root.title("PieEngine")
    #OUR CANVAS
    c = tk.Canvas(root,bg = colour,height = height,width = width)
    #DISPLAYING OUR CANVAS
    c.pack()
    #MAINLOOP
    root.mainloop() 




#CALLING THE FUNCTION
createWindow(400,400,None)
