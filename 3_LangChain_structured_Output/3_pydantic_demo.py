from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'vishwa' #default value = vishwa
    age: Optional[int] = None #optional fields if nothing inside a age value it will through none
    email: EmailStr #builtin datatype in pydantic , to validate a email,
                     #for example if you assign value like email = "vishwa" it will through an error that it is not valid email address
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')  #field funtion : to add constants,contraints,description or regular expressions


new_student = {'age':'25', 'email':'vishwa@gmail.com'} #also pydantic supports coerce that means even if  you pass string in 'age':'25', 
                                                        #it will able to fatch that it is interger not string ,it will typecast it and change the type

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()