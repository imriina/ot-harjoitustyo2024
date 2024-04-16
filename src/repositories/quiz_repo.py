from pathlib import Path

from repositories.user_repo import UserRepository
import csv
import random

class QuizRepository:
    def __init__(self, file_path):
        self.questions = self.load_questions_from_file(file_path)
    
    def load_questions_from_file(self, file_path):
        questions = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                question = {
                    'question_text': row['question_text'],
                    'options': [row['option1'], row['option2'], row['option3'], row['option4']],
                    'correct_option': int(row['correct_option'])
                }
                questions.append(question)
        return questions
    
    def get_random_question(self):
        return random.choice(self.questions)