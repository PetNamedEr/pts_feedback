from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

# Backtrack to parent dir to prevent import problems
import os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0,parentdir)

from models.base import Base
from models.feedback import Feedback
from models.question import Question
from config.setup import engine


tablename = "answers"

class Answer(Base):
    __tablename__ = tablename

    # Mappers
    id_ = Column(Integer, primary_key=True)
    value_ = Column(String)
    created_at_ = Column(DateTime, nullable=False)

    # Answer is child of feedback
    feedback_id_ = Column(Integer, ForeignKey('feedbacks.id_'))
    feedbacks = relationship("Feedback", back_populates='answers')

    # Answer is child of question
    question_id_ = Column(Integer, ForeignKey('questions.id_'))
    questions = relationship("Question", back_populates='answers')

    def __init__(self, value_, feedback_id_, question_id_):
        self.value_ =  value_
        self.feedback_id_ = feedback_id_
        self.question_id_= question_id_
        self.created_at_ = datetime.datetime.now()

    def __repr__(self):
        return "<Id: {}, Value: '{}', Created_at: '{}', Question_id: {}, Feedback_id: {}>".format(self.id_, self.value_, self.created_at_, self.question_id_, self.feedback_id_)

    @property
    def serialize(self):
        return {
            'id' : self.id_,
            'value' : self.value_,
            'created_at' : self.created_at_.isoformat(),
            'question_id' : self.question_id_,
            'feedback_id' : self.feedback_id_
        }

if not engine.has_table(tablename):
    Base.metadata.create_all(engine)


