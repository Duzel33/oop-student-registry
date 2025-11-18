import re

class Student:
    def __init__(self, name, age = 13, grade = "12th"):
        self._name = name
        self._age= age
        self._grade = grade

    def __str__(self):
        return f"Student 1: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"
    
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
    @property
    def grade(self):
        return self._grade
    
    @name.setter
    def name(self, student_name):
        if type(student_name) == str and len(student_name) >= 3 and student_name.isalpha() == True and student_name == student_name.title():
            self._name = student_name
            print(self._name)
        else:
            print("Please try again, name must be greater than 3 characters with no spaces or special characters, and the first letter capitalized")

    @age.setter
    def age(self, student_age):
        if type(student_age) == int and 11 <= student_age <= 18:
            self._age = student_age
        else:
            print("Please try again, age must be a number between 11 and 18")

    @grade.setter
    def grade(self, student_grade):
        grade = ["9th", "10th", "11th", "12th"]
        if student_grade in grade:
            self._grade = f"{student_grade}"
        else:
            print("Please try again, grade must be 9th, 10th, 11th, or 12th")

    def study(self, subject):
        return f"{self.name} is studying {subject}"
    
    def advance(self,num_advance):
        numbers = re.findall(r'\d+', self.grade)
        self._grade = int(numbers[0]) + num_advance        
        return f"{self.name} has advanced to the {self.grade}th grade"
    


student = Student("john", 10, "13th")
# print(student)
# student.name = "Jimmy"
# student.age = 18
student.grade = 9
# print(student.study("Math"))
print(student.advance(5))