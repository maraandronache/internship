from enum import Enum
from Question import Question
from ValidationUtil import ValidationUtil
from EnumValues import EnumValues


# stores all questions using the Question class, including the validation using th ValidationUtil class
class QuestionEnum(Enum):
    ASK_AGE = EnumValues(Question("What is your age? ", validation=ValidationUtil.validate_number), 1)
    ASK_CITY = EnumValues(Question("What city are you from? ", validation=ValidationUtil.validate_city), 2)
    ASK_GENDER = EnumValues(Question("What is your gender? ", validation=ValidationUtil.validate_gender), 3)
    ASK_EDUCATION = EnumValues(Question("What type of education did you finish last?(middle school, high school, "
                        "bachelor degree, master degree, PhD) ", validation=ValidationUtil.validate_education), 4)
    ASK_HAS_PETS = EnumValues(Question("Do you own pets? ", validation=ValidationUtil.validate_yes_or_no), 5)
    ASK_NO_OF_PETS = EnumValues(Question("How many pets do you own? ", validation=ValidationUtil.validate_number), 6)
    ASK_NAME_OF_PETS = EnumValues(Question("What is the name of your pet? ", validation=None), 7)
    ASK_TYPE_OF_PETS = EnumValues(Question("What type of pet is it? ", validation=None), 8)
    ASK_OPEN_TO_ADOPT = EnumValues(Question("Are you open to the idea of owning pets? ",
                                            validation=ValidationUtil.validate_yes_or_no), 9)
    ASK_ISSUE = EnumValues(Question("What is stopping you from adopting? "), 10)
    ASK_CHANGE_MIND = EnumValues(Question("What would change your mind? "), 11)
