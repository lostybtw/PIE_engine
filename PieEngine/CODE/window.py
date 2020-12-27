import functions
import tkinter as tk
root = tk.Tk()
root.title("PieEngine")
c = tk.Canvas(root,bg ="white",height =1000,width = 1000)
c.pack()

points1 = [200,200,100,300,290,300]
points2 = [200,200,300,300,350,270]

"""functions.triangle(c,200,200,100,300,300,300)"""

functions.pyramid(c,points1,points2)

root.mainloop()