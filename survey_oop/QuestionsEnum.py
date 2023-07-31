from enum import Enum
from Question import Question
from ValidationUtil import ValidationUtil


class QuestionEnum(Enum):
    ASK_AGE = Question("What is your age? ", validation=ValidationUtil.valid_age)
    ASK_CITY = Question("What city are you from? ", validation=ValidationUtil.valid_city)
    ASK_GENDER = Question("What is your gender? ", validation=ValidationUtil.valid_gender)
    ASK_EDUCATION = Question("What type of education did you finish last?(middle school, high school, bachelor degree,"
                             " master degree, PhD) ", validation=ValidationUtil.valid_education)
    ASK_HAS_PETS = Question("Do you own pets? ", validation=ValidationUtil.valid_yes_no)
    ASK_NO_OF_PETS = Question("How many pets do you own? ", validation=lambda x: x.isnumeric())
    ASK_NAME_OF_PETS = Question("What is the name of your pet? ", validation=None)
    ASK_TYPE_OF_PETS = Question("What type of pet is it? ", validation=None)
    ASK_OPEN_TO_ADOPT = Question("Are you open to the idea of owning pets? ",
                                 validation=ValidationUtil.valid_yes_no)
    ASK_ISSUE = Question("What is stopping you from adopting? ")
    ASK_CHANGE_MIND = Question("What would change your mind? ")
