
class Question:
    def __init__(self, prompt, validation=None):
        self.prompt = prompt
        self.validation = validation

    def ask(self):
        while True:
            answer = input(self.prompt)
            if not self.validation or self.validation(answer):
                return answer