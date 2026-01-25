from pydantic import BaseModel, EmailStr

class Person(BaseModel):
    name: str
    age: int
    email: EmailStr

valid_data = Person(name="Kiran", age=28, email="kiran@gmail.com")

print(valid_data)