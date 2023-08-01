# the class in which the custom error is created, for when the participant answers wrong 3 times for a single question
class InvalidInput(Exception):
    pass

# class made to ask the questions more efficiently, using the prompt and a validation rule (or none)
class Question:
    def __init__(self, prompt, validation=None):
        self.prompt = prompt
        self.validation = validation
        self.wrong_answers = 0

    # actually asks, while checking with the validation rule
    def ask(self):
        while self.wrong_answers < 3:
            answer = input(self.prompt)
            # if the validation rule is respected, the answer given is returned
            if not self.validation or self.validation(answer):
                return answer
            # else, the counter for wrong answers increases by 1, and the program either asks the user for other input,
            # or it throws the custom error
            self.wrong_answers += 1
        else:
            raise InvalidInput(f"You have answered the question {self.prompt}wrong 3 times. Please restart the survey.")
