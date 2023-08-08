from UsedBase import Base
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
from SurveysTable import Surveys
from QuestionsTable import Question

engine = create_engine("mysql+mysqlconnector://root:mara@localhost:3306/survey")


class Answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    answer = Column(String)
    question_id = Column(Integer, ForeignKey('questions.id'))
    survey_id = Column(Integer, ForeignKey('surveys.id'))

class AddAnswer():
    def __init__(self, answer, question_id, survey_id):
        self.answer = answer
        self.question_id = question_id
        self.survey_id = survey_id

    def add_answers(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        new_answer = Answers(answer=self.answer, question_id=self.question_id, survey_id=self.survey_id)
        session.add(new_answer)
        session.commit()
        session.close()


