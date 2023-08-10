from enum import Enum

class GenerateAnswersEnum(Enum):
    CITY_OPTIONS = ["bucharest", "cluj", "timisoara", "iasi", "mangalia", "oradea", "botosani", "brasov", "craiova",
                    "arad", "sibiu"]
    GENDER_OPTIONS = ["male", "female"]
    YES_NO_OPTIONS = ["yes", "no"]
    EDUCATION_OPTIONS = ["middle school", "high school", "college", "bachelor degree", "master degree", "phd"]
    PET_NAMES_OPTIONS = ["lily", "toto", "rocco", "cocco", "zbanti", "zizi", "goldie", "max", "daisy", "cici", "ida",
                         "sasha", "buddy", "mocha", "mitzy", "joy", "griffen", "garfield", "gilda", "spike", "tuffy",
                         "zorro", "xena"]
    PET_TYPES_OPTIONS = ["dog", "cat", "parrot", "fish", "hamster", "turtle", "bunny", "guinea pig"]
