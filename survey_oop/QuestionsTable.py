from UsedBase import Base
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

engine = create_engine("mysql+mysqlconnector://root:mara@localhost:3306/survey")

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String)