from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
import datetime

# Backtrack to parent dir to prevent import problems
# made by Saija, not sure if working properly 29.3.2018
# Modified by Inka 14.4.2018

import os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0,parentdir)

from models.base import Base
from config.setup import engine

tablename = "questions"

class Question(Base):
    __tablename__ = tablename

    # Mappers
    id_ = Column(Integer, primary_key=True, autoincrement=True)
    type_ = Column(String)
    title_ = Column(String)
    optional_ = Column(Boolean)

    # Question is child of survey
    survey_id_ = Column(Integer, ForeignKey('surveys.id_'))
    surveys = relationship("Survey", back_populates="questions")

    # Question is parent to answers
    answers = relationship("Answer", back_populates="questions")

    # Question is parent to question choices
    questionchoices = relationship("QuestionChoice", back_populates="questions")


    def __init__(self, type_, title_, survey_id_, optional_):
        self.type_ = type_
        self.title_ = title_
        self.survey_id_ = survey_id_
        self.optional_ = optional_


    def __repr__(self):
        # return "<id_: {}, type_: '{}', title_: '{}', survey_id_: {}>".format(self.id_, self.type_, self.title_, self.survey_id_)
        return "<Id: {}, Type: '{}', Title: '{}', Survey_id: {}, optional_: {}>".\
            format(self.id_, self.type_, self.title_, self.survey_id_, self.optional_)

    @property
    def serialize(self):
        return {
            'id_' : self.id_,
            'type_' : self.type_,
            'title_' : self.title_,
            'survey_' : self.survey_id_,
            'optional_' : self.optional_
        }

if not engine.has_table(tablename):
    Base.metadata.create_all(engine)