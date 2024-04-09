from tkinter import ttk
class QuizView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)


        header = ttk.Label(master=self._frame, text="tähän tulee")
 
        header.grid(row=0, column=0)

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def destroy(self):
        self._frame.destroy()