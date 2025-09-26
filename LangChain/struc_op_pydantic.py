import modelspydantic
from modelspydantic import BaseModel,EmailStr
from typing import Optional
#The ** (double asterisk) is called dictionary unpacking in Python.
class student(BaseModel):

    name: str= 'anshu ' # default values can be also set hereBy 
    age:Optional[int]= None
    email:EmailStr 

student_1={
 'age':46   ,
 'name':'kripa',
 'email':"anshu@gmail.com"
}

std= student(**student_1)
print(std)
