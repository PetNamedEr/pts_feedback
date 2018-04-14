from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

# Backtrack to parent dir to prevent import problems
# made by Saija, not sure if working properly 29.3.2018
import os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0,parentdir)

from models.base import Base
from models.feedback import Feedback
from config.setup import engine

tablename = "questions"

class Question(Base):
    __tablename__ = "questions"

    # Mappers
    id_ = Column(Integer, primary_key=True,autoincrement=True)
    type_ = Column(String)
    title_ = Column(String)

    # Question is child of survey
    survey_id_ = Column(Integer, ForeignKey('surveys.id_'))
    survey = relationship("Survey", back_populates="questions")

    # Question is parent to answers
    answers = relationship("Answer", back_populates="questions")

    # Question is parent to question choices
    question_choices = relationship("QuestionChoice", back_populates="questions")


    def __init__(self, id_, type_, title_, survey_id_):
        self.id_ = id_
        self.type_ = type_
        self.title_ = title_
        self.survey_id_ = survey_id_


    def __repr__(self):
        return "<Id: {},Type: '{}', Title: '{}', Survey_id {}>".format(self.id_, self.type_, self.title_, self.survey_id_)

    @property
    def serialize(self):
        return {
            'id' : self.id_,
            'type' : self.type_,
            'title' : self.title_,
            'survey' : self.survey_id_
        }

if not engine.has_table(tablename):
    Base.metadata.create_all(engine)
