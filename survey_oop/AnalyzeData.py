import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from AddAnswers import Answers
from sqlalchemy import and_
from sqlalchemy.orm import aliased

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

    def create_pie_chart(self, frequency, labels, colors, title):
        plt.pie(frequency, labels=labels, colors=colors, autopct=lambda p: '{:.0f}'.format(p * sum(frequency) / 100))
        plt.legend(loc='upper left', bbox_to_anchor=(-0.40, 1))
        plt.title(title)
        plt.show()


    def analyze_data(self):
        self.analyze_age()
        self.analyze_gender()
        self.get_education_distribution()
        self.analyze_owners_vs_non_owners()
        self.get_most_common_pet_names()
        self.get_most_common_pet_types()
        self.analyze_open_to_adopt()
        self.write_report()

    def analyze_age(self):
        plt.hist(self.age_list, edgecolor='black', width=0.3)
        mean_age = np.mean(self.age_list)
        plt.axvline(mean_age, color='r', linestyle='dashed', linewidth=1)
        plt.text(mean_age, plt.ylim()[1] * 0.9, 'Average Age: {:.2f}'.format(mean_age), color='r')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.title('Age Distribution')
        plt.show()

    def analyze_gender(self):
        y = np.array(self.gender)
        labels = ["Female", "Male"]
        self.create_pie_chart(y, labels, self.two_colors, "Gender Distribution")

    def analyze_owners_vs_non_owners(self):
        y = np.array(self.has_pets)
        labels = ["Has pets", "Does not have pets"]
        self.create_pie_chart(y, labels, self.two_colors, "People who are pet owners vs. those who are not")

    def get_education_distribution(self):
        frequency = Counter(self.education)
        labels = list(frequency.keys())
        frequencies = list(frequency.values())
        self.create_pie_chart(frequencies, labels, self.five_colors, "Education Distribution")

    def get_most_common_pet_names(self):
        frequencies = Counter(self.pet_names)
        most_common = frequencies.most_common(5)
        counts = [x[1] for x in most_common]
        labels = [x[0][0] for x in most_common]
        self.create_pie_chart(counts, labels, self.five_colors, "5 most common pet names")

    def get_most_common_pet_types(self):
        frequencies = Counter(self.pet_types)
        most_common = frequencies.most_common(5)
        counts = [x[1] for x in most_common]
        labels = [x[0][0] for x in most_common]
        self.create_pie_chart(counts, labels, self.five_colors, "5 most common pet types")

    def analyze_open_to_adopt(self):
        y = np.array(self.is_open_to_adopt)
        labels = ["Open to adopt", "Not open to adopt"]
        self.create_pie_chart(y, labels, self.two_colors, "People who are open to adopt versus those who are not")

    def most_common_cities(self):
        pass

    def average(self, values_list):
        sum = 0
        for x in values_list:
            sum += int(x)
        return round(sum/len(values_list), 2)

    def percentage(self, a, b):
        return round(a * 100 / (a + b), 2)

    def write_report(self):
        Session = sessionmaker(bind=engine)
        session = Session()

        no_of_respondents = len(self.age_list)
        file = open("report.txt", "a")
        file.write(f"A total of {no_of_respondents} have taken this survey, out of which {self.male_count} "
                   f"({self.percentage(self.male_count, self.female_count)}%) are male, while {self.female_count} "
                   f"({self.percentage(self.female_count, self.male_count)}%) are females.\n")
        avg_age = self.average(self.age_list)
        min_age = min(self.age_list)
        max_age = max(self.age_list)
        file.write(f"The average age of the respondents is {avg_age}, with the minimum age being {min_age} and the "
                   f"maximum age being {max_age}.\n")
        file.write(f"{self.owners} ({self.percentage(self.owners, self.non_owners)}%) people are pet owners and "
                   f"{self.non_owners} ({self.percentage(self.non_owners, self.owners)}%)are not.\n")
        subquery = session.query(Answers.survey_id).filter(Answers.question_id == 5, Answers.answer == 1).subquery()
        subquery_alias = aliased(subquery)
        query = session.query(Answers.answer).filter(
            Answers.question_id == 1,
            Answers.survey_id.in_(session.query(subquery_alias.c.survey_id))
        )
        owners_age = [x[0] for x in query.all()]
        subquery = session.query(Answers.survey_id).filter(Answers.question_id == 5, Answers.answer == 0).subquery()
        subquery_alias = aliased(subquery)
        query = session.query(Answers.answer).filter(
            Answers.question_id == 1,
            Answers.survey_id.in_(session.query(subquery_alias.c.survey_id))
        )
        non_owners_age = [x[0] for x in query.all()]
        file.write(f"The average age of those who are pet owners is {self.average(owners_age)}, while the average age "
                   f"of those who are not is {self.average(non_owners_age)}.\n")

