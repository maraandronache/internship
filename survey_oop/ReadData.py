from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from AddAnswers import Answers
from AnalyzeData import AnalyzeData

engine = create_engine("mysql+mysqlconnector://root:mara@localhost:3306/survey")

class ReadData():
    def __init__(self):
        self.age_values = {}
        self.pet_names = []
        self.pet_types = []
        self.has_pets = []
        self.cities = []
        self.gender = []
        self.education = []
        self.no_of_pets = []

    def get_data(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        self.age_values = session.query(Answers.answer).filter(Answers.question_id == 1).all()
        self.cities = session.query(Answers.answer).filter(Answers.question_id == 2).all()
        self.gender = session.query(Answers.answer).filter(Answers.question_id == 3).all()
        self.education = session.query(Answers.answer).filter(Answers.question_id == 4).all()
        self.has_pets = session.query(Answers.answer).filter(Answers.question_id == 5).all()
        self.no_of_pets = session.query(Answers.answer).filter(Answers.question_id == 6).all()
        self.pet_names = session.query(Answers.answer).filter(Answers.question_id == 7).all()
        self.pet_types = session.query(Answers.answer).filter(Answers.question_id == 8).all()
        m = AnalyzeData(self.age_values, self.gender)
        m.analyze_gender()


