from Survey import Survey
from QuestionsEnum import QuestionEnum

if __name__ == "__main__":
    user_input = Survey()
    user_input.ask_basic_info()
    user_input.write()
