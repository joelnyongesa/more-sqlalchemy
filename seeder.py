from faker import Faker
from main import Student
import random
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
fake = Faker()
engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

students = [
    Student(
        name = fake.name(),
        student_email = fake.email(),
        grade = random.randint(1,13)
    )
    for i in range(50)
]

session.bulk_save_objects(students)
session.commit()