from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'vishwa', 'age':'25'}

print(new_person)