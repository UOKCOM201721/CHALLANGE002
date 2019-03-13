# TODO List
# 1. create scroll bar and a frame == Done
# 2. create edit menu == done
# 3. implement open functions
# 4. implement save and save_as function to open a file dialog

import tkinter as tk
# contains functions which create file dialogs
import tkinter.filedialog as fd


class Window:
    def __init__(self):
        self.textarea = ''
        self.filename = ''

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
        fileMenu.add_command(label='Open', command=self.open)
        fileMenu.add_command(label='Save', command=self.save)
        fileMenu.add_command(label='Save As', command=self.saveAs)
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.killWindow)
        menuBar.add_cascade(label='File', menu=fileMenu)

        # creating the editMenu
        editMenu = tk.Menu(menuBar, tearoff=0)
        editMenu.add_command(label='Undo', command=self.undo)
        editMenu.add_command(label='Redo', command=self.redo)
        editMenu.add_command(label='Copy', command=self.copy)
        editMenu.add_command(label='Paste', command=self.paste)
        menuBar.add_cascade(label='Edit', menu=editMenu)

        # creating the text area
        self.textarea = tk.Text(frame, borderwidth=0, relief='sunken')
        self.textarea.config(font=('consolas', 12), undo=True, wrap='word')
        self.textarea.grid(column=0, row=0, sticky='nsew')

        # creating scroll bar and linking it with the text area
        scrollBar = tk.Scrollbar(frame, command=self.textarea.yview, width=15)
        scrollBar.grid(column=1, row=0, sticky='nsew')
        self.textarea['yscrollcommand'] = scrollBar.set

        wind.config(menu=menuBar)
        wind.mainloop()

    def open(self):
        self.Clear()
        self.filename = fd.askopenfile().name
        filecontents = ''
        with open(self.filename, 'r+') as data:
            for line in data:
                filecontents += line

        self.textarea.insert(1.0, filecontents)

    def save(self):
        data = self.textarea.get(1.0, tk.END)
        if self.filename == '':
            self.saveAs()
        else:
            open(self.filename, 'w+').write(data)

    def saveAs(self):
        self.filename = fd.asksaveasfile(mode='w').name
        data = self.textarea.get(1.0, tk.END)
        open(self.filename, 'w+').write(data)

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

    # to clear the current contents of the text window
    def Clear(self):
        self.textarea.delete(1.0, tk.END)
        self.textarea.update()


def executable():
    Window().main()


if __name__ == '__main__':
    executable()
