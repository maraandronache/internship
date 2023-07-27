from enum import Enum
class QuestionEnum(Enum):
    Q1 = "What is your age? "
    Q2 = "What city are you from? "
    Q3 = "What is your gender? "
    Q4 = "What type of education did you finish last?(middle school, high school, bachelor degree, master degree, PhD) "
    Q5 = "Do you own pets? "
    Q6 = "How many pets do you own? "
    Q7 = "What is the name of your pet? "
    Q8 = "What type of pet is it? "
    Q9 = "Are you open to the idea of owning pets? "
    Q10 = "What is stopping you from adopting? "
    Q11 = "What would change your mind? "
    GENDER = ("male", "female")
    EDUCATION = ("middle school", "high school", "college", "bachelor degree", "master degree", "phd")
