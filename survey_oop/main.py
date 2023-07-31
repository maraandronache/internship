from Survey import Survey
from QuestionsEnum import QuestionEnum

if __name__ == "__main__":
    user_input = Survey()
    user_input.basic()
    if user_input.answers[QuestionEnum.ASK_HAS_PETS]:
        user_input.pet_documentation()
    else:
        user_input.open_to_adopt()
    user_input.write()

