from decimal import Clamped
from typing import TypedDict

class Person(TypedDict):
      name : str
      age : int

New_Person : Person = {
    'name' : 'Hani',
    'age' : 22
}

print(New_Person)
