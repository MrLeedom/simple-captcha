# !/usr/bin/env python
# coding:utf-8
# python3.3
import tkinter as tk
#import tkFileDialog


class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.floater = FloatingWindow(self)


class FloatingWindow(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)
        self.attributes("-transparentcolor", "blue")
        self.attributes("-topmost", 1)
        self.attributes("-alpha", 0.5)
#        self.label = tk.Label(self, text="Click on the grip to move")
#        self.grip = tk.Label(self, bitmap="gray25")
#        self.grip.pack(side="left", fill="y")
#        self.label.pack(side="right", fill="both", expand=True)
        self.canvas = tk.Canvas(self, width=300, height=200)
        # self.canvas.pack(side="bottom",fill="both",expand=True)
        self.canvas.create_rectangle(0, 0, 300, 200, fill="blue")
        self.canvas.create_text(
            50, 10, text='tkinter', font=("Fixdsys", 15, "bold"), fill="yellow")
        self.canvas.grid(column=0, row=0)
        self.canvas.bind("<ButtonPress-1>", self.StartMove)
        self.canvas.bind("<ButtonRelease-1>", self.StopMove)
        self.canvas.bind("<B1-Motion>", self.OnMotion)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))

if __name__ == "__main__":

    app = App()
