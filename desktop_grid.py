from tkinter import *
from tools import *
from colors import color_palette

class DesktopGrid:

    def __init__(self):

        self.root = Tk()
        self.root.title("Desktop Grid")
        self.root.attributes("-fullscreen", True)
        self.root.resizable(0,0)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.bind('<KeyPress>', lambda e: self.root.destroy() if e.char.lower() == 'q' else None)

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self._create_grid()
        self._create_tools_menu()


    def _create_grid(self):

        self.canvas = Canvas(
            self.root,
            bg=color_palette['grid-background'],
            highlightthickness=0
            )
        self.canvas.grid(sticky=NSEW)

        # Create the 20s grid lines
        for n in range(20, self.width // 2, 20):

            self.canvas.create_line(
                self.width // 2 + n, 0,
                self.width // 2 + n, self.height,
                fill=color_palette['gridLines-twenties'],
                width=1
                )
            self.canvas.create_line(
                self.width // 2 - n, 0,
                self.width // 2 - n, self.height,
                fill=color_palette['gridLines-twenties'],
                width=1
                )
            self.canvas.create_line(
                0, self.height // 2 + n,
                self.width, self.height // 2 + n,
                fill=color_palette['gridLines-twenties'],
                width=1
                )
            self.canvas.create_line(
                0, self.height // 2 - n,
                self.width, self.height // 2 - n,
                fill=color_palette['gridLines-twenties'],
                width=1
                )
        
        # Create the 100s grid lines
        for n in range(100, self.width // 2, 100):

            self.canvas.create_line(
                self.width // 2 + n, 0,
                self.width // 2 + n, self.height,
                fill=color_palette['gridLines-hundreds'],
                width=3
                )
            self.canvas.create_line(
                self.width // 2 - n, 0,
                self.width // 2 - n, self.height,
                fill=color_palette['gridLines-hundreds'],
                width=3
                )
            self.canvas.create_line(
                0, self.height // 2 + n,
                self.width, self.height // 2 + n,
                fill=color_palette['gridLines-hundreds'],
                width=3
                )
            self.canvas.create_line(
                0, self.height // 2 - n,
                self.width, self.height // 2 - n,
                fill=color_palette['gridLines-hundreds'],
                width=3
                )
            
        # Create the axis lines
        self.canvas.create_line(
            0, self.height // 2,
            self.width, self.height // 2,
            fill=color_palette['gridLines-axes'],
            width=5
            )
        self.canvas.create_line(
            self.width // 2, 0,
            self.width // 2, self.height,
            fill=color_palette['gridLines-axes'],
            width=5
            )
        
        # Create the markers
        for n in range(100, self.width, 100):

                self.canvas.create_rectangle(
                    self.width // 2 + n - 12, self.height // 2 + 12,
                    self.width // 2 + n + 13, self.height // 2 + 29,
                    fill=color_palette['grid-background'],
                    outline=''
                    )
                self.canvas.create_rectangle(
                    self.width // 2 - n - 12, self.height // 2 + 12,
                    self.width // 2 - n + 13, self.height // 2 + 29,
                    fill=color_palette['grid-background'],
                    outline=''
                    )
                self.canvas.create_rectangle(
                    self.width // 2 - 32, self.height // 2 + n - 8,
                    self.width // 2 - 7, self.height // 2 + n + 9,
                    fill=color_palette['grid-background'],
                    outline=''
                    )
                self.canvas.create_rectangle(
                    self.width // 2 - 32, self.height // 2 - n - 8,
                    self.width // 2 - 7, self.height // 2 - n + 9,
                    fill=color_palette['grid-background'],
                    outline=''
                    )
                
                self.canvas.create_text(
                    self.width // 2 + n, self.height // 2 + 20,
                    text=str(n),
                    anchor=CENTER
                    )
                self.canvas.create_text(
                    self.width // 2 - n, self.height // 2 + 20,
                    text=str(n),
                    anchor=CENTER
                    )
                self.canvas.create_text(
                    self.width // 2 - 20, self.height // 2 + n,
                    text=str(n),
                    anchor=CENTER
                    )
                self.canvas.create_text(
                    self.width // 2 - 20, self.height // 2 - n,
                    text=str(n),
                    anchor=CENTER
                    )


    def _create_tools_menu(self):

        self.tools_menu = Frame(
            self.canvas,
            borderwidth=2,
            relief='groove',
            bg=color_palette["toolsMenu-background"]
            )
        self.tools_menu.grid(padx=5, pady=5)

        self.icons = [
            PhotoImage(file='icons\Pencil.png').subsample(2, 2),
            PhotoImage(file='icons\Eraser.png').subsample(2, 2),
            PhotoImage(file='icons\Rectangle.png').subsample(2, 2),
            PhotoImage(file='icons\Circle.png').subsample(2, 2),
            PhotoImage(file='icons\Line.png').subsample(2, 2),
            PhotoImage(file='icons\Text.png').subsample(2, 2)
        ]
        self.tools = [Tool(
            lambda _: 1,
            self.tools_menu,
            image=i,
            bg=color_palette["toolsMenu-background"],
            activebackground=color_palette["toolsMenu-tool-selected-background"],
            borderwidth=0
            ) for i in self.icons]

        self.tool_activated = False
        self.selected_tool = False
        for i, tool in enumerate(self.tools):
            
            tool.bind("<Enter>", lambda e: self._handle_events(e))
            tool.bind("<Leave>", lambda e: self._handle_events(e))
            tool.bind("<ButtonRelease-1>", lambda e: self._handle_events(e))
            
            tool.grid(row=i // 2 + 1, column=i % 2 + 1, padx=5, pady=5)


    def _handle_events(self, event):

        match event.type:

            case EventType.Enter:
                if event.widget != self.selected_tool:
                    event.widget.config(bg=color_palette["toolsMenu-tool-mouseover-background"])

            case EventType.Leave:
                if event.widget != self.selected_tool:
                    event.widget.config(bg=color_palette["toolsMenu-background"])

            case EventType.ButtonRelease:

                if self.tool_activated:
                    self.selected_tool.config(bg=color_palette["toolsMenu-background"])

                    if self.selected_tool == event.widget:
                        self.tool_activated = False
                        self.selected_tool = False

                    else:
                        event.widget.config(bg=color_palette["toolsMenu-tool-selected-background"])
                        self.selected_tool = event.widget

                else:
                    event.widget.config(bg=color_palette["toolsMenu-tool-selected-background"])
            
                    self.tool_activated = True
                    self.selected_tool = event.widget



if __name__ == "__main__":

    dg = DesktopGrid()
    dg.root.mainloop()
