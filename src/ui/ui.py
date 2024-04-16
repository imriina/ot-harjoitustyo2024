from ui.main_view import MainView
from ui.guiz_view import QuizView
from ui.login_view import LoginView
from ui.register_view import RegisterView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_menu()


    def _show_main_menu(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = MainView(self._root, self._show_quiz, self._show_login)
        self._current_view.pack()
        

    def _show_quiz(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = QuizView(self._root, self._show_main_menu)
        self._current_view.pack()
        
    def _show_login(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = LoginView(self._root, self._show_main_menu, self._show_quiz, self._show_register)
        self._current_view.pack()
        
    def _show_register(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = RegisterView(self._root, self._show_main_menu, self._show_quiz,)
        self._current_view.pack()