# TODO List
# 1. create scroll bar and a frame
# 2. create edit menu
# 3. implement open functions
# 4. implement save and save_as function to open a file dialog

import tkinter as tk


class Functions:
    def open(self):
        pass

    def save(self):
        pass

    def saveAs(self):
        pass

    def killWindow(self):
        pass

    def undo(self):
        pass

    def redo(self):
        pass

    def copy(self):
        pass

    def paste(self):
        pass



class Window(Functions):
    def main(self):
        # GUI container
        wind = tk.Tk()
        wind.title("Cpil Text Editor")
        # creating the container frame
        frame = tk.Frame(wind, width=600, height=600)
        frame.pack(fill='both', expand=True)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # creating a menu item
        menuBar = tk.Menu(wind)

        # creating the fileMenu
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label='Open', command=Functions.open)
        fileMenu.add_command(label='Save', command=Functions.save)
        fileMenu.add_command(label='Save As', command=Functions.saveAs)
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=Functions.killWindow)
        menuBar.add_cascade(label='File', menu=fileMenu)

        # creating the editMenu
        editMenu = tk.Menu(menuBar, tearoff=0)
        editMenu.add_command(label='Undo', command=Functions.undo)
        editMenu.add_command(label='Redo', command=Functions.redo)
        editMenu.add_command(label='Copy', command=Functions.copy)
        editMenu.add_command(label='Paste', command=Functions.paste)
        menuBar.add_cascade(label='Edit', menu=editMenu)

        # creating the text area
        textarea = tk.Text(frame, borderwidth=0, relief='sunken')
        textarea.config(font=('consolas', 12), undo=True, wrap='word')
        textarea.grid(column=0, row=0, sticky='nsew')

        # creating scroll bar and linking it with the text area
        scrollBar = tk.Scrollbar(frame, command=textarea.yview, width=15)
        scrollBar.grid(column=1, row=0, sticky='nsew')
        textarea['yscrollcommand'] = scrollBar.set

        wind.config(menu=menuBar)
        wind.mainloop()


def executable():
    Window().main()


if __name__ == '__main__':
    executable()
