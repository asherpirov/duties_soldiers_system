from soldier_manager import *
from utils import *
from duty_manager import *
import data


def show_menu() -> None:

    print("Soldiers Duty Management System")
    print("===============================")
    print("1. Add soldier")
    print("2. Sub soldier")
    print("3. View all soldiers")
    print("4. Add duty")
    print("5. Update status duty")
    print("6. Show all duties")
    print("===============================")

    return None


def get_user_choice() -> str:
    choice = input("enter your choice: ")

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

        return None






def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    pass


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """


if __name__ == "__main__":
    main()