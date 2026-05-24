"""https://github.com/asherpirov/duties_soldiers_system.git"""

from soldier_manager import *
from utils import *
from duty_manager import *
import data


def show_menu() -> None:
    while True:
        print("Soldiers Duty Management System")
        print("===============================")
        print("1. Add soldier")
        print("2. Sub soldier")
        print("3. View all soldiers")
        print("4. Add duty")
        print("5. Update status duty")
        print("6. Show all duties")
        print("7. Exit")
        print("===============================")

        return None


def get_user_choice() -> str:
    choice = input("Enter your choice (1-7): ")

    return choice


def handle_add_soldier() -> None:
    while True:
        id_input = input("enter id soldier: ")

        if not is_valid_id(id_input):
            print("ID must be between 6 and 8 numbers only")
            continue

        soldier_id = int(id_input)

        name = input("enter the soldier name: ")

        try:
            add_soldier(soldier_id, name)
            print("Soldier added successfully ✓")
            break
        except ValueError as e:
            print(f"ERROR {e}")
            print("Please try again")

    return None



def handle_remove_soldier() -> None:
    while True:
        id_input = input("enter id soldier: ")

        if not is_valid_id(id_input):
            print("ID must be between 6 and 8 numbers only")
            continue

        soldier_id = int(id_input)

        try:
            remove_soldier(soldier_id)
            break
        except ValueError as e:
            print(f"ERROR {e}")
            print("Please try again")

    return None

def handle_view_soldiers() -> None:
   get_all_soldiers()
   return None

def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    while True:
        id_input = input("enter id: ")

        if not is_valid_id(id_input):
            print("ID must be between 6 and 8 numbers only")
            continue

        soldier_id = int(id_input)
        duty = input("enter duty: ")
        day = input("enter a day: ")

        try:
            add_duty_to_soldier(soldier_id, duty, day)
            print("Duty added successfully ✓")
            break
        except(ValueError, KeyError) as e:
            print(f"ERROR: {e}")
            print("Please try again.\n")

    return None


def handle_update_duty_status() -> None:
    while True:
        id_input = input("enter id soldier: ")

        if not is_valid_id(id_input):
            print("ID must be between 6 and 8 numbers only")
            continue

        soldier_id = int(id_input)
        duty_name = input("enter duty: ")
        status = input("enter a status: ")

        try:
            update_duty_status(soldier_id, duty_name, status)
            print("Status updated successfully ✓")
            break

        except (ValueError, KeyError) as e:
            print(f"ERROR: {e}")
            print("Please try again.\n")

    return None

def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    while True:
        id_input = input("enter id soldier: ")

        if not is_valid_id(id_input):
            print("ID must be between 6 and 8 numbers only")
            continue

        soldier_id = int(id_input)

        try:
            duties = get_soldier_duties(soldier_id)

            if not duties:
                print("This soldier has no duties yet.")
            else:
                print(f"Duties for Soldier ID {soldier_id}")
                for duty in duties:
                    print(f"Duty: {duty['duty_name']}, Day: {duty['day']}, Status: {duty['status']}")
            break

        except KeyError as e:
            print(f"ERROR: {e}")
            print("Please try again.\n")

    return None


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    while True:
        show_menu()
        choice = get_user_choice()
        if choice == "1":
            handle_add_soldier()
        elif choice == "2":
            handle_remove_soldier()
        elif choice == "3":
            handle_view_soldiers()
        elif choice == "4":
            handle_add_duty()
        elif choice == "5":
            handle_update_duty_status()
        elif choice == "6":
            handle_view_soldier_duties()
        elif choice == "7":
            print("Exiting system. Goodbye!")
            break  # שובר את הלולאה ומסיים את התוכנית
        else:
            print("Invalid choice. Please select a number between 1 and 7.")
if __name__ == "__main__":
    main()