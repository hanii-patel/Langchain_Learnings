from pydantic import BaseModel , EmailStr, Field
from typing import Optional

#Basic Example
class Student(BaseModel):
    name : str
    age : int

#Default Input
class Student(BaseModel):
    name : str = 'Yash'
    age : int = 20

#Optional Field , Field Functions
class Student(BaseModel):
    name : str = 'Meet'
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field (gt=0 , lt=10)

new_student = Student(name='Hani' , age=22 , email='hani@gmail.com' , cgpa=9.5)
print(new_student)

