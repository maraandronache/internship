from UsedBase import Base
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine("mysql+mysqlconnector://root:mara@localhost:3306/survey")


class Surveys(Base):
    __tablename__ = 'surveys'
    id = Column(Integer, primary_key=True)
    date_taken = Column(Date)

class AddDate():
    def add():
        date = datetime.today().date()
        Session = sessionmaker(bind=engine)
        session = Session()
        new_date = Surveys(date_taken=date)
        session.add(new_date)
        session.commit()
        session.close()


