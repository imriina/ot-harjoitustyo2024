import uuid

class Quiz:

    def __init__(self, question_text, options, correct_answer):

        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer


   
    def __str__(self):
        
        return f"{self.question_text}\nOptions: {', '.join(self.options)}"
    

    def check_answer(self, selected_index):

        return selected_index == self.correct_answer