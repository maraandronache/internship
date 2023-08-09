import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from AddAnswers import Answers
from sqlalchemy import and_

engine = create_engine("mysql+mysqlconnector://root:mara@localhost:3306/survey")

class AnalyzeData():
    def __init__(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        age_list = session.query(Answers.answer).filter(Answers.question_id == 1).all()
        self.age_list = [int(age[0]) for age in age_list]
        self.female_count = session.query(Answers.answer).filter(
            and_(Answers.question_id == 3, Answers.answer == 'female')).count()
        self.male_count = session.query(Answers.answer).filter(and_(Answers.question_id == 3,
                                                                    Answers.answer == 'male')).count()
        self.gender = [self.female_count, self.male_count]
        self.owners = session.query(Answers.answer).filter(and_(Answers.question_id == 5,
                                                                Answers.answer == 1)).count()
        self.non_owners = session.query(Answers.answer).filter(and_(Answers.question_id == 5,
                                                                    Answers.answer == 0)).count()
        self.has_pets = [int(self.owners), int(self.non_owners)]
        education_list = session.query(Answers.answer).filter(Answers.question_id == 4).all()
        self.education = [education[0].capitalize() for education in education_list]
        self.pet_names = session.query(Answers.answer).filter(Answers.question_id == 7).all()
        self.pet_types = session.query(Answers.answer).filter(Answers.question_id == 8).all()
        self.open_to_adopt = session.query(Answers.answer).filter(and_(Answers.question_id == 9,
                                                                       Answers.answer == 'yes')).count()
        self.not_open_to_adopt = session.query(Answers.answer).filter(and_(Answers.question_id == 9,
                                                                           Answers.answer == 'no')).count()
        self.is_open_to_adopt = [self.open_to_adopt, self.not_open_to_adopt]
        self.two_colors = ["#9BABB8", "#EEE3CB"]
        self.five_colors = ["#9BABB8", "#EEE3CB", "#967E76", "#D7C0AE", "#28536B"]


    def analyze_data(self):
        self.analyze_age()
        self.analyze_gender()
        self.get_education_distribution()
        self.analyze_owners_vs_non_owners()
        self.get_most_common_pet_names()
        self.get_most_common_pet_types()
        self.analyze_open_to_adopt()

    def analyze_age(self):
        plt.hist(self.age_list, edgecolor='black', width=0.3)
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.title('Age Distribution')
        plt.show()

    def analyze_gender(self):
        y = np.array(self.gender)
        labels = ["Female", "Male"]
        plt.pie(y, labels=labels, colors=self.two_colors)
        plt.title('Gender Distribution')
        plt.show()

    def analyze_owners_vs_non_owners(self):
        y = np.array(self.has_pets)
        labels = ["Has pets", "Does not have pets"]
        plt.pie(y, labels=labels, colors=self.two_colors)
        plt.title('Owners vs. Non-Owners')
        plt.show()

    def get_education_distribution(self):
        frequency = Counter(self.education)
        labels = list(frequency.keys())
        frequencies = list(frequency.values())
        plt.pie(frequencies, labels=labels, colors=self.five_colors)
        plt.legend(loc='upper left')
        plt.title('Education Distribution')
        plt.show()

    def get_most_common_pet_names(self):
        frequencies = Counter(self.pet_names)
        most_common = frequencies.most_common(5)
        counts = [x[1] for x in most_common]
        labels = [x[0][0] for x in most_common]
        plt.pie(counts, labels=labels, colors=self.five_colors, autopct=lambda p: '{:.0f}'.format(p * sum(counts) / 100))
        plt.legend(loc='upper left')
        plt.title('Most common pet names')
        plt.show()

    def get_most_common_pet_types(self):
        frequencies = Counter(self.pet_types)
        most_common = frequencies.most_common(5)
        counts = [x[1] for x in most_common]
        labels = [x[0][0] for x in most_common]
        plt.pie(counts, labels=labels, colors=self.five_colors, autopct=lambda p: '{:.0f}'.format(p * sum(counts) / 100))
        plt.legend(loc='upper left')
        plt.title('Most common pet types')
        plt.show()

    def analyze_open_to_adopt(self):
        y = np.array(self.is_open_to_adopt)
        labels = ["Open to adopt", "Not open to adopt"]
        plt.pie(y, labels=labels, colors=self.two_colors)
        plt.title('People open to adopting pets vs. people not open to adopting pets')
        plt.show()





