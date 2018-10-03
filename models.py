from bottle import install
from bottle.ext import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine, Date, ForeignKey, UniqueConstraint, cast, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()
engine = create_engine('sqlite:///app.db')
create_session = sessionmaker(bind=engine, autoflush=False)
plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    create=True
)
install(plugin)


class Quarter(Base):
    """Model for quarters"""
    __tablename__ = 'quarters'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    quarter = Column(String(2), nullable=False)

    statistics = relationship("Statistic", back_populates="quarter")

    UniqueConstraint('year', 'quarter', name='quarters_uix_1')

    @hybrid_property
    def name(self):
        return f"{self.year} - {self.quarter}"

    @name.expression
    def name(cls):
        return cast(cls.year, Text) + " - " + cls.quarter

    @classmethod
    def title(cls):
        return cls.__name__

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Subject(Base):
    """Model for subjects"""
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)

    statistics = relationship("Statistic", back_populates="subject")

    UniqueConstraint('name', name='subjects_uix_1')

    @classmethod
    def title(cls):
        return cls.__name__

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Room(Base):
    """Model for rooms"""
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    statistics = relationship("Statistic", back_populates="room")

    UniqueConstraint('name', name='rooms_uix_1')

    @classmethod
    def title(cls):
        return 'Class'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    """Model for students"""
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
    birth = Column(Date, nullable=False)

    statistics = relationship("Statistic", back_populates="student")

    UniqueConstraint('name', 'birth', name='students_uix_1')

    @classmethod
    def title(cls):
        return cls.__name__

    def as_dict(self):
        as_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        as_dict['birth'] = self.birth.strftime('%d-%m-%Y')
        return as_dict


class Statistic(Base):
    """Model for statistics"""
    __tablename__ = 'statistics'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    quarter_id = Column(Integer, ForeignKey('quarters.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    value = Column(Integer, nullable=False)

    student = relationship("Student", back_populates="statistics")
    room = relationship("Room", back_populates="statistics")
    quarter = relationship("Quarter", back_populates="statistics")
    subject = relationship("Subject", back_populates="statistics")

    UniqueConstraint('student_id', 'room_id', 'quarter_id', 'subject_id', name='statistics_uix_1')

    @property
    def student_name(self):
        return self.student.name

    @property
    def room_name(self):
        return self.room.name

    @property
    def quarter_name(self):
        return self.quarter.name

    @property
    def subject_name(self):
        return self.subject.name

    def as_dict(self):
        as_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        as_dict['student_name'] = self.student_name
        as_dict['room_name'] = self.room_name
        as_dict['quarter_name'] = self.quarter_name
        as_dict['subject_name'] = self.subject_name
        return as_dict
