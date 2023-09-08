# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    tasks = relationship("Task", back_populates="category")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="tasks")

engine = create_engine("sqlite:///taskly.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()