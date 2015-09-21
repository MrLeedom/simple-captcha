import tkinter as tk
from tkinter import filedialog


# filedialog.askopenfile()

class snake(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.gridcount = 3
        self.width = 900
        self.height = 500

        # self.top = self.winfo_toplevel()
        # self.top.resizable(False, False)
        self.grid()
        self.canvas = tk.Canvas(self)
        self.canvas.grid()
        self.canvas.config(
            width=self.width, height=self.height, relief=tk.RIDGE)

        self.drawgrid()

    def drawgrid(self):
        s = self.height / self.gridcount
        for i in range(0, self.gridcount):
            self.canvas.create_line(
                0, i * s, self.width, i * s, fill='#FFD39B')


# class App(tk.Tk):

#     """主窗口"""

#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.width = 900
#         self.height = 500
# self.grid()
# self.canvas = tk.Canvas(self)
# self.canvas.config(
# width=self.width, height=self.height, relief=tk.RIDGE)
# self.canvas.grid()
#         self.top = top(self)
#         self.top.grid(column=0, row=0)
#         self.top.columnconfigure(0, weight=1)
#         self.top.rowconfigure(0, weight=1)


class top(tk.Frame):

    """顶部窗口"""

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.width = 900
        self.height = 300
        self.bg = 'blue'
        # self.canvas = tk.Canvas(self)
        # self.canvas.config(
        #     width=self.width, height=self.height, bg='blue', relief=tk.RIDGE)
        # self.canvas.grid()


# def help_menu():
#     help_btn = tk.Menubutton(menu_frame, text='Help', underline=0)
#     help_btn.pack(side=tk.LEFT, padx="2m")
#     help_btn.menu = tk.Menu(help_btn)
#     help_btn.menu.add_command(label="How To", underline=0, command=HowTo)
#     help_btn.menu.add_command(label="About", underline=0, command=About)
#     help_btn['menu'] = help_btn.menu
#     return help_btn


# def GetSource():
#     get_window = tk.Toplevel(root)
#     get_window.title('Source File?')
#     tk.Entry(get_window, width=30,
#              textvariable=source).pack()
#     tk.Button(get_window, text="Change",
#               command=lambda: update_specs()).pack()

# source = tk.StringVar()
# source.set('txt2html.txt')

# source_string = source.get()

root = tk.Tk()
# root.geometry('80x80')
root.title('test')
snake = tk.Frame(root, height=500, widt=900, bg='blue')
# top = tk.Frame(root, height=root.height, width=root.width, bg='blue')
snake.grid(row=3, column=4, sticky='NSEW')

#-- Create the menu frame, and menus to the menu frame
# menu_frame = tk.Frame(root)
# menu_frame.pack(fill=tk.X, side=tk.TOP)
# menu_frame.tk_menuBar(file_menu(), action_menu(), help_menu())
# -- Create the history frame (to be filled in during runtime)
# history_frame = tk.Frame(root)
# history_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=2)
# -- Create the info frame and fill with initial contents
# info_frame = tk.Frame(root)
# info_frame.pack(fill=tk.X, side=tk.BOTTOM)
# first put the column labels in a sub-frame
# LEFT, Label = tk.LEFT, tk.Label  # shortcut names
# label_line = tk.Frame(info_frame, relief=tk.RAISED, borderwidth=1)
# label_line.pack(side=tk.TOP, padx=2, pady=1)
# Label(label_line, text="Run #", width=5).pack(side=LEFT)
# Label(label_line, text="Source:", width=20).pack(side=LEFT)
# Label(label_line, text="Target:", width=20).pack(side=LEFT)
# Label(label_line, text="Type:", width=20).pack(side=LEFT)
# Label(label_line, text="Proxy Mode:", width=20).pack(side=LEFT)
# then put the "next run" information in a sub-frame
# info_line = tk.Frame(info_frame)
# info_line.pack(side=tk.TOP, padx=2, pady=1)
# update_specs()
# -- Finally, let's actually do all that stuff created above
root.mainloop()
