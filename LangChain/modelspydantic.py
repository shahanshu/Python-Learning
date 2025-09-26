import modelspydantic
from modelspydantic import EmailStr,BaseModel,Field
from typing import Optional


'''
class student(BaseModel):
    name:Optional[str] ='anshu'
    email:EmailStr

std1=student(
    name='kripa',
    email='anshu@gmail.com'
)
print(std1
      )

The other way using the dict is- 

'''
class student(BaseModel):
    name:str
    age: int = Field(20, gt=18, lt=50,description='age ')
    
std1={
    'name':'kripa',
    'age':45
    
}
ip1=student(**std1)
ip1_dict=dict(ip1)
print((ip1_dict))
print(ip1_dict['name'])

if (ip1_dict['age']) > 20:
    print('age is invalid')
    input_age= int(input("enter new age "))
    if input_age < 20:
        ip1_dict['age']=input_age


print(f"new age is {ip1_dict}")