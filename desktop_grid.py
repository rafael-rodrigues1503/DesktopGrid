from tkinter import *
from tools import *

class DesktopGrid:

    def __init__(self):

        self.root = Tk()
        self.root.title("Desktop Grid")
        self.root.attributes("-fullscreen", True)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self._create_grid()
        self._create_tools_menu()


    def _create_grid(self):

        self.canvas = Canvas(self.root, bg='antique white', highlightthickness=0)
        self.canvas.grid(sticky='nsew')

        for n in range(20, self.width // 2, 20):

            if n % 100 == 0:
                _fill = 'gray85'
                _width = 2
            else:
                _fill = 'gray90'
                _width = 1

            self.canvas.create_line(self.width // 2 + n, 0, self.width // 2 + n, self.height, fill=_fill, width=_width)
            self.canvas.create_line(self.width // 2 - n, 0, self.width // 2 - n, self.height, fill=_fill, width=_width)

            self.canvas.create_line(0, self.height // 2 + n, self.width, self.height // 2 + n, fill=_fill, width=_width)
            self.canvas.create_line(0, self.height // 2 - n, self.width, self.height // 2 - n, fill=_fill, width=_width)
        
            if n % 100 == 0:

                self.canvas.create_rectangle(self.width // 2 + n - 11, self.height // 2 + 12, self.width // 2 + n + 11, self.height // 2 + 27, fill='antique white', outline='')
                self.canvas.create_rectangle(self.width // 2 - n - 11, self.height // 2 + 12, self.width // 2 - n + 11, self.height // 2 + 27, fill='antique white', outline='')
                self.canvas.create_rectangle(self.width // 2 - 21, self.height // 2 + n - 7, self.width // 2 - 9, self.height // 2 + n + 7, fill='antique white', outline='')
                self.canvas.create_rectangle(self.width // 2 - 21, self.height // 2 - n - 7, self.width // 2 - 9, self.height // 2 - n + 7, fill='antique white', outline='')
                
                self.canvas.create_text(self.width // 2 + n, self.height // 2 + 20, text=str(n), anchor='center')
                self.canvas.create_text(self.width // 2 - n, self.height // 2 + 20, text=str(n), anchor='center')
                self.canvas.create_text(self.width // 2 - 20, self.height // 2 + n, text=str(n), anchor='center')
                self.canvas.create_text(self.width // 2 - 20, self.height // 2 - n, text=str(n), anchor='center')

        self.canvas.create_line(0, self.height // 2, self.width, self.height // 2, fill='black', width=5)
        self.canvas.create_line(self.width // 2, 0, self.width // 2, self.height, fill='black', width=5)


    def _create_tools_menu(self):

        self.tools_menu = Frame(self.canvas, borderwidth=2, relief='groove')
        self.tools_menu.grid(padx=5, pady=5)

        self.icons = [
            PhotoImage(file='icons\Pencil.png').subsample(2, 2),
            PhotoImage(file='icons\Eraser.png').subsample(2, 2),
            PhotoImage(file='icons\Rectangle.png').subsample(2, 2),
            PhotoImage(file='icons\Circle.png').subsample(2, 2),
            PhotoImage(file='icons\Line.png').subsample(2, 2),
            PhotoImage(file='icons\Text.png').subsample(2, 2)
        ]
        self.tools = [Tool(lambda _: 1, self.tools_menu, image=i) for i in self.icons]

        for i, tool in enumerate(self.tools):
            
            # tool.bind("<Enter>", lambda event, b=tool: b.config(background='blue', borderwidth=2))
            # tool.bind("<Leave>", lambda event, b=tool: b.config(background='gray80'))
            tool.grid(row=i // 2 + 1, column=i % 2 + 1, padx=5, pady=5)



if __name__ == "__main__":

    dg = DesktopGrid()
    dg.root.mainloop()
