# the main class in which answers from the survey are collected
from QuestionsEnum import QuestionEnum
from SurveysTable import AddDate
from sqlalchemy import create_engine
from AddAnswers import AddAnswer
from sqlalchemy.orm import sessionmaker
from SurveysTable import Surveys

engine = create_engine("mysql+mysqlconnector://root:mara@localhost:3306/survey")

class Survey():
    def __init__(self):
        self.pet_dict = {}  # storing pets' name & type
        self.answers = {}  # storing th answers to basic questions

    # gets the answers for the basic info
    def ask_basic_info(self):
        for x in (QuestionEnum.ASK_AGE, QuestionEnum.ASK_CITY, QuestionEnum.ASK_GENDER, QuestionEnum.ASK_EDUCATION):
            self.answers[x] = x.value.question.ask()

        if QuestionEnum.ASK_HAS_PETS.value.question.ask().lower() == "yes":
            self.answers[QuestionEnum.ASK_HAS_PETS] = True
        else:
            self.answers[QuestionEnum.ASK_HAS_PETS] = False

        # asks the following question, based on whether the person has animals or not
        if self.answers[QuestionEnum.ASK_HAS_PETS]:
            self.get_pet_documentation()
        else:
            self.is_open_to_adopt()

    # gets all pet info (name & type)
    def get_pet_documentation(self):
        self.no_of_pets = QuestionEnum.ASK_NO_OF_PETS.value.question.ask()
        self.store_pet_info()

    # stores all pet info (name & type)
    def store_pet_info(self):
        for i in range(int(self.no_of_pets)):
            name = QuestionEnum.ASK_NAME_OF_PETS.value.question.ask()
            name = name.capitalize()
            type = QuestionEnum.ASK_TYPE_OF_PETS.value.question.ask()
            self.pet_dict[name] = type.lower()

    # finds out whether the person is open to adopting or not, then asks the following questions
    def is_open_to_adopt(self):
        self.open_to_adopt = QuestionEnum.ASK_OPEN_TO_ADOPT.value.question.ask()
        if self.open_to_adopt:
            self.issue = QuestionEnum.ASK_ISSUE.value.question.ask()
        else:
            self.change_mind = QuestionEnum.ASK_CHANGE_MIND.value.question.ask()

    def get_survey_id(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        survey_obj = session.query(Surveys).order_by(Surveys.id.desc()).first()
        return int(survey_obj.id)


    # writes answers in the csv file, in order to analyze them
    def write(self):
        AddDate.add()
        survey_id = self.get_survey_id()
        # Session = sessionmaker(bind=engine)
        # session = Session()
        for x in self.answers.keys():
            new_answer = AddAnswer(self.answers[x], x.value.id, survey_id)
            new_answer.add_answers()

        if self.answers[QuestionEnum.ASK_HAS_PETS]:
            add_no_of_pets = AddAnswer(self.no_of_pets, QuestionEnum.ASK_NO_OF_PETS.value.id, survey_id)
            add_no_of_pets.add_answers()
            for x in self.pet_dict.keys():
                add_name_of_pet = AddAnswer(x, QuestionEnum.ASK_NAME_OF_PETS.value.id, survey_id)
                add_name_of_pet.add_answers()
                add_type_of_pet= AddAnswer(self.pet_dict[x], QuestionEnum.ASK_TYPE_OF_PETS.value.id, survey_id)
                add_type_of_pet.add_answers()
        else:
            add_open_to_adopt = AddAnswer(self.open_to_adopt, QuestionEnum.ASK_OPEN_TO_ADOPT.value.id, survey_id)
            add_open_to_adopt.add_answers()
            if self.open_to_adopt:
                add_issue = AddAnswer(self.issue, QuestionEnum.ASK_ISSUE.value.id, survey_id)
                add_issue.add_answers()
            else:
                add_change_mind = AddAnswer(self.change_mind, QuestionEnum.ASK_CHANGE_MIND.value.id, survey_id)
                add_change_mind.add_answers()
