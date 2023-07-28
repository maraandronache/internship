from enum import Enum
from Question import Question


class QuestionEnum(Enum):
    # TODO remove these from enum
    GENDER = ("male", "female")
    EDUCATION = ("middle school", "high school", "college", "bachelor degree", "master degree", "phd")
    YESNO = ("yes", "no")
    ASK_AGE = Question("What is your age? ", validation=lambda x: x.isnumeric())
    ASK_CITY = Question("What city are you from? ", validation=lambda x: x.isalpha())
    ASK_GENDER = Question("What is your gender? ", validation=lambda x: x.lower() in QuestionEnum.GENDER.value)
    ASK_EDUCATION = Question("What type of education did you finish last?(middle school, high school, bachelor degree,"
                             " master degree, PhD) ", validation=lambda x: x.lower() in QuestionEnum.EDUCATION.value)
    ASK_HAS_PETS = Question("Do you own pets? ", validation=lambda x: x.lower() in QuestionEnum.YESNO.value)
    ASK_NO_OF_PETS = Question("How many pets do you own? ", validation=lambda x: x.isnumeric())
    ASK_NAME_OF_PETS = Question("What is the name of your pet? ", validation=None)
    ASK_TYPE_OF_PETS = Question("What type of pet is it? ")
    ASK_OPEN_TO_ADOPT = Question("Are you open to the idea of owning pets? ", validation=lambda x: x.lower() in
                                 QuestionEnum.YESNO.value)
    ASK_ISSUE = Question("What is stopping you from adopting? ")
    ASK_CHANGE_MIND = Question("What would change your mind? ")
