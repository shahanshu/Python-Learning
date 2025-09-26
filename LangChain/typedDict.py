from typing import TypedDict

class profile(TypedDict,profile=False):
    name:str
    slr:int

user:profile={

    "name":"anshu kumar sha ",
    "slr":12345
}
print(user)