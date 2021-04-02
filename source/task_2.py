class Person:
    def __init__(self, first_name, last_name, father) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.father}"


def print_information(person: object, depth:int):
    """prints the depth and field
    """
    fields = ['first_name', 'last_name', 'father']
    for field in fields:
        print(f"{getattr(person, field)} {depth}")

def print_depth(data: dict, depth: int=1):
    if isinstance(data, Person):
        print_information(data, depth)
        if isinstance(data.father, Person):
            print_depth(data.father, depth=1)
    elif isinstance(data, dict):
        for key in data:
            print(f"{key} {depth}")
            if isinstance(data[key], object):
                print_depth(data[key], depth + 1)



