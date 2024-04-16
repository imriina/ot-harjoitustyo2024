from tkinter import ttk
class QuizView:
    def __init__(self, root, backbutton_command):
        self._root = root
        self._frame = None
        self._backbutton_command = backbutton_command

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)


        header = ttk.Label(master=self._frame, text="tähän tulee")
        backbutton = ttk.Button(master=self._frame, text="Back", command=self._backbutton_command)

        backbutton.grid(row=5, column=5)
        header.grid(row=0, column=0)

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def destroy(self):
        self._frame.destroy()