
class Question:
    def __init__(self, prompt, validation=None):
        self.prompt = prompt
        self.validation = validation

    def ask(self):
        while True:
            answer = input(self.prompt)
            if self.validation and self.validation(answer):
                return answer