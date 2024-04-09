from tkinter import ttk
class MainView:
    def __init__(self, root, startbutton_command):
        self._root = root
        self._frame = None
        self._start_command= startbutton_command

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)


        header = ttk.Label(master=self._frame, text="Visa")
        startbutton = ttk.Button(master=self._frame, text="Pelaa", command=self._start_command)


        header.grid(row=0, column=0)
        startbutton.grid(row=1, column=0)

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def destroy(self):
        self._frame.destroy()