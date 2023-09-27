#!/usr/bin/env python3

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, distinct

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    # Table columns
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    student_email = Column(String())
    grade = Column(Integer())

    def __repr__(self):
        return f"Student name: {self.name}, "\
            + f"Student email: {self.student_email}, "\
            + f"Grade: {self.grade}"
    

if __name__ == "__main__":
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    joel = Student(
        name = "Joel Nyongesa",
        student_email = "joelnyongesa@students.com",
        grade = 7
    )

    kayzer = Student(
        name = "Mercy Kayzer",
        student_email = "mercy.kayzer@student.com",
        grade = 6
    )

    # session.bulk_save_objects([joel, kayzer])
    # session.commit()

    # Querying our database
    # students = [student for student in session.query(Student)]
    # print(students)

    # grade_5_students = [student.name for student in session.query(Student).filter(Student.grade == 5).order_by(Student.name)]
    # print(grade_5_students)

        # Query for distinct grades
    distinct_grades = session.query(distinct(Student.grade)).order_by(Student.grade).all()

    # Extract distinct grades from the result
    distinct_grades = [grade[0] for grade in distinct_grades]
    print(distinct_grades)