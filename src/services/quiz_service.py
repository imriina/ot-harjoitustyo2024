from entities.quiz import Quiz
from entities.user import User


from repositories.quiz_repo import (
    QuizRepository as default_quiz_repository
)

from repositories.user_repo import (
    UserRepository as default_user_repository
)

class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class QuizService:
    def __init__(
        self,
        quiz_repository=default_quiz_repository,
        user_repository=default_user_repository

    ):

        self._user = None
        self._quiz_repository = quiz_repository
        self._user_repository = user_repository

    def login(self, username, password):
        user = self._user_repository.find_user(username, password)
        if not user or user.password != password:
            raise InvalidCredentialsError
        self._user = user

    def register(self, username, password):
        user_exist = self._user_repository.find_user(username, password)
        if user_exist:
            raise UsernameExistsError(f"Username {username} already exists")
        user = self._user_repository.create(User(username, password))
        self._user = user