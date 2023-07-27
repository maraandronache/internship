class SurveyResponse:
    def __init__(self):
        self.dict = {}

    def add_answer(self, question, answer):
        self.dict[question] = answer