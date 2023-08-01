from QuestionsEnum import QuestionEnum

class InvalidInput(Exception):
    pass

class Survey:
    def __init__(self):
        self.pet_dict = {}
        self.answers = {}

    def ask_basic_info(self):
        for x in (QuestionEnum.ASK_AGE, QuestionEnum.ASK_CITY, QuestionEnum.ASK_GENDER, QuestionEnum.ASK_EDUCATION):
            self.answers[x] = x.value.ask()
            if self.answers[x] == None:
                raise InvalidInput(f"You have entered invalid input 3 times for qustion {x.value}. Please restart the survey.")

        if QuestionEnum.ASK_HAS_PETS.value.ask().lower() == "yes":
            self.answers[QuestionEnum.ASK_HAS_PETS] = True
        else:
            self.answers[QuestionEnum.ASK_HAS_PETS] = False

        if self.answers[QuestionEnum.ASK_HAS_PETS]:
            self.get_pet_documentation()
        else:
            self.is_open_to_adopt()

    def get_pet_documentation(self):
        self.no_of_pets = QuestionEnum.ASK_NO_OF_PETS.value.ask()
        self.store_pet_info()

    def store_pet_info(self):
        for i in range(int(self.no_of_pets)):
            name = QuestionEnum.ASK_NAME_OF_PETS.value.ask()
            name = name.capitalize()
            type = QuestionEnum.ASK_TYPE_OF_PETS.value.ask()
            self.pet_dict[name] = type.lower()

    def is_open_to_adopt(self):
        self.open_to_adopt = QuestionEnum.ASK_OPEN_TO_ADOPT.value.ask()
        if self.open_to_adopt:
            self.issue = QuestionEnum.ASK_ISSUE.value.ask()
        else:
            self.change_mind = QuestionEnum.ASK_CHANGE_MIND.value.ask()

    def write(self):
        with open("collected_data.csv", 'a') as file:
            for x in self.answers.keys():
                file.write(f"{self.answers[x]},")
            if self.answers[QuestionEnum.ASK_HAS_PETS]:
                file.write(f"{self.no_of_pets}")
                for x in self.pet_dict.keys():
                    file.write(f",{x},{self.pet_dict[x]}")
            else:
                file.write(f"{self.open_to_adopt}")
                if self.open_to_adopt:
                    file.write(f",{self.issue}")
                else:
                    file.write(f",{self.change_mind}")

            file.write("\n")
