class Question:
    def __init__(self, prompt, validation=None):
        self.prompt = prompt
        self.validation = validation
        self.wrong_answers = 0

    def ask(self):
        while self.wrong_answers < 3:
            answer = input(self.prompt)
            if not self.validation or self.validation(answer):
                return answer
            self.wrong_answers += 1
        else:
            return None
