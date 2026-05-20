"""menu.py"""

def menu() -> None:
    """
    Presents a menu to the user and processes their input.

    Prompts the user to select an option.
     Raises a ValueError if the selected
    number is out of range,and a
     TypeError if the input is non-numeric.

    Returns:
        None
    """
    pass

"""soldiers_manager"""

def handle_add_soldier():
    """
    Creates a new soldier and adds them to the system.

    Calls the `add_soldier` function to check if the soldier already exists.
    Displays a success message upon creation, or an error message if they do.

    Args:
        name (str): The name of the soldier.
        soldier_id (int or str): The ID of the soldier.

    Raises:
        ValueError: If the provided name or ID is invalid.
    """
    pass

def add_soldier(name, id):
    """
Adds a soldier to the system data
 using parameters from the input handler.

Args:
    name (str): The soldier's name.
    soldier_id (str or int): The soldier's ID.
    """
    pass

def sub_soldier(name, id):
    """
    Removes a soldier from the data based on the provided inputs.

    Verifies whether the soldier exists in the system. If the soldier is found,
    they are removed. If the soldier is not found, an error is issued.

    Args:
        name (str): The soldier's name.
        soldier_id (str or int): The soldier's ID.
    """
    pass


"""duty_manager.py"""

def handle_add_duty():
    """
    Handles user input to create a new duty assignment.

    Prompts the user for a specific day and soldier ID to create a task,
    and subsequently calls the `add_duty` function to process the assignment.
    """
    pass

def add_duty(id, day, duty):
    """
    Assigns a specific duty to a soldier for a given day.

    Validates the input using day and duty verification functions.
    If all validations pass, it updates the duty dictionary with the new assignment.

    Args:
        id (str or int): The unique ID of the soldier.
        day (str): The assigned day for the duty.
        duty (dict or str): The duty details or the dictionary to be updated.
    """
    pass

"""soldiers_manager"""

def is_day(day, possible_days):
    """
    Validates if a given day is within the allowed list of days.

    Args:
        day (str): The specific day to check.
        possible_days (list): A list containing the valid days for duty.

    Returns:
        bool: True if the day is in the list of possible days, False otherwise.
    """
    # הערה: הוספתי כאן את הפרמטרים לפונקציה בהתאם לתיאור שכתבת
    pass

def is_duty(duty):
    """
    Checks if a soldier is currently assigned to a duty.

    Args:
        duty (dict or str): The duty record to evaluate.

    Returns:
        bool: True if the soldier is on duty, False otherwise.
    """
    pass

def is_solider(id, name):
    """
    Checks whether a specific soldier exists in the system.

    Args:
        id (str or int): The unique ID of the soldier.
        name (str): The name of the soldier.

    Returns:
        bool: True if the soldier exists in the system, False otherwise.
    """
    pass

def view_solider():
    """
    Displays the details of the soldiers in the system.

    This function retrieves and prints the information of the soldiers
    currently stored in the database. It does not require any input parameters.

    Returns:
        None
    """
    pass

def view_duty(soldier_details):
    """
    Displays the duty assignments of a specific soldier.

    Args:
        soldier_details (dict or str): The details or ID of the soldier whose duties are to be viewed.

    Returns:
        None
    """
    pass