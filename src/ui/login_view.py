from tkinter import ttk
from services.quiz_service import QuizService, InvalidCredentialsError
class LoginView:

    def __init__(self, root, backbutton_command, togamebut_command, regbut_command):
        self._root = root
        self._frame = None
        self._backbutton_command = backbutton_command
        self._togamebut_command = togamebut_command
        self._regbut_command = regbut_command

        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            QuizService.login(username, password)
            self._togamebut_command()
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)


        header = ttk.Label(master=self._frame, text="tähän tuleem login")
        backbutton = ttk.Button(master=self._frame, text="Back", command=self._backbutton_command)
        togamebut = ttk.Button(master=self._frame, text="Login/play", command=self._togamebut_command)
        regbut = ttk.Button(master=self._frame, text="Register", command=self._regbut_command)

        username_label = ttk.Label(master=self._frame, text="username")
        password_label = ttk.Label(master=self._frame, text="password")
        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        backbutton.grid(row=0, column=10)
        togamebut.grid(row=3, column=1)
        regbut.grid(row=0,column=11)
        header.grid(row=0, column=0)

        username_label.grid(row=1, column=0, pady=5)
        password_label.grid(row=2, column=0, pady=5)
        self._username_entry.grid(row=1, column=1, pady=5)
        self._password_entry.grid(row=2, column=1, pady=5)


    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def destroy(self):
        self._frame.destroy()