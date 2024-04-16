import uuid

from entities.user import User
from repositories.quiz_repo import QuizRepository

class Quiz:
    def __init__(self, username, questions_file_path):
        self.username = User(username)
        self.quiz_repo = QuizRepository(questions_file_path)
        self.current_question = None
        self.is_game_over = False
    
 