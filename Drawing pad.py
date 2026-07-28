from tkinter import *

root = Tk()
root.title("Drawing Pad")

canvas = Canvas(root, width=500, height=400, bg="white")
canvas.pack()

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+3, y+3, fill="black", outline="black")

canvas.bind("<B1-Motion>", draw)

root.mainloop()