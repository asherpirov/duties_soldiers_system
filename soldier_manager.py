import data
from data import soldier_list
from utils import *

def add_soldier(soldier_id: int, name: str) -> None:
        try:
            if not name.isalpha():
                raise ValueError(f"Name '{name}' must contain only letters.")
            if find_soldier_by_id(soldier_id) is not None:
                raise ValueError(f"Soldier with ID {soldier_id} already exists!")
            soldier_dict = dict(name=name, soldier_id=soldier_id, duty=[])
            soldier_list.append(soldier_dict)
            print(f"Success: Soldier '{name}' added.")
        except (AttributeError,KeyError,ValueError) as e:
            print(f"invalid input {e}")
        return None


def remove_soldier(soldier_id: int) -> None:
    try:
        for dct in soldier_list:
            if find_soldier_by_id(soldier_id):
                soldier_list.remove(dct)
                print(f"Success: Soldier '{dct}' removed.")
            else:
                print(f"Soldier with ID {soldier_id} not exists!")
    except ValueError as e:
        print(f"invalid input {e}")
    return None

def get_all_soldiers() -> list:
    return soldier_list


