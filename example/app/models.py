"""Declare an SQLAlchemy model for Person"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

Base = declarative_base()


class Person(Base):
    """Person model"""

    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

    @classmethod
    def all(cls, session: Session) -> list["Person"]:
        """Get all persons."""
        return session.query(cls).all()

    def __str__(self) -> str:
        """Get string representation of Person."""
        return f"{self.first_name} {self.last_name} ({self.age})"


engine = create_engine("sqlite:///example.db", echo=True)

# create engine and create all tables in a local file
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
