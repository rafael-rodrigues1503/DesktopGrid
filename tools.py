from tkinter import *


class Tool(Button):

    def __init__(self, tool, master=None, cnf={}, **kw):
        
        super().__init__(master, cnf, **kw)
        self.tool = tool


class Pencil(Tool):

    def __init__(self, tool, master=None, cnf={}, **kw):

        super().__init__(tool, master, cnf, **kw)

    def _(self):

        pass


class Eraser(Tool):

    def __init__(self, tool, master=None, cnf={}, **kw):

        super().__init__(tool, master, cnf, **kw)

    def _(self):

        pass


class Rectangle(Tool):

    def __init__(self, tool, master=None, cnf={}, **kw):

        super().__init__(tool, master, cnf, **kw)

    def _(self):

        pass


class Circle(Tool):

    def __init__(self, tool, master=None, cnf={}, **kw):

        super().__init__(tool, master, cnf, **kw)

    def _(self):

        pass


class Line(Tool):

    def __init__(self, tool, master=None, cnf={}, **kw):

        super().__init__(tool, master, cnf, **kw)

    def _(self):

        pass


class Text(Tool):

    def __init__(self, tool, master=None, cnf={}, **kw):

        super().__init__(tool, master, cnf, **kw)

    def _(self):

        pass

