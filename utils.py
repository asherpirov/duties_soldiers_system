from data import soldier_list


def is_valid_id(id_str: str) -> bool:
    """
    בודקת אם ה-ID שהוקלד תקין (לא ריק, מכיל רק ספרות ובאורך הגיוני).

    סוג: פונקציית validation (בדיקת תקינות)
    מקור קלט: מקבלת מחרוזת (str) לפני ההמרה למספר, כדי למנוע קריסה.
    """
    clean_id = id_str.strip()

    if not clean_id:
        return False

    if not clean_id.isdigit():
        return False

    if len(clean_id) < 6 or len(clean_id) > 9:
        return False

    return True


def find_soldier_by_id(soldier_id: int) -> dict | None:
    try:
        for soldier in soldier_list:
            if soldier["soldier_id"] == soldier_id:
                return soldier
    except KeyError:
        return None


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    """
    מחפשת תורנות לפי שם ברשימת תורנויות.

    סוג: פונקציית עזר (Helper Function)

    מקבלת:
        duties (list): רשימת תורנויות
        duty_name (str): שם התורנות לחיפוש

    מחזירה:
        dict | None: מילון של התורנות אם נמצאה, None אם לא נמצאה

    זורקת: כלום - מחזירה None במקרה שלא נמצא

    למה הפונקציה קיימת:
    פונקציה זו משמשת במספר מקומות (הוספת תורנות, עדכון סטטוס).
    הפרדה של לוגיקת החיפוש למקום אחד.
    מחזירה None במקום לזרוק exception - מאפשרת גמישות.
    """
    if duty_name in duties:
        return


def is_valid_status(status: str) -> bool:
    """
    בודקת אם סטטוס הוא חוקי.

    סוג: פונקציית validation (בדיקת תקינות)

    מקבלת:
        status (str): הסטטוס לבדיקה

    מחזירה:
        bool: True אם הסטטוס חוקי (pending/completed/missed)
              False אם לא חוקי

    זורקת: כלום - תמיד מחזירה bool

    למה הפונקציה קיימת:
    בדיקת תקינות של סטטוס משמשת במספר מקומות.
    במקום לחזור על הבדיקה, יש פונקציה אחת.
    גם מקל על שינוי הסטטוסים החוקיים בעתיד.
    פונקציות validation מחזירות bool ולא זורקות exceptions.
    """

    status_lst = ["pending", "completed", "missed"]
    return status in status_lst



def is_valid_name(name: str) -> bool:
    """
    בודקת אם שם הוא תקין (לא ריק).

    סוג: פונקציית validation (בדיקת תקינות)

    מקבלת:
        name (str): השם לבדיקה

    מחזירה:
        bool: True אם השם תקין (לא ריק)
              False אם ריק

    זורקת: כלום - תמיד מחזירה bool

    למה הפונקציה קיימת:
    בדיקת תקינות של שם משמשת במספר מקומות.
    הפרדה של לוגיקת הבדיקה למקום אחד.
    בעתיד אפשר להוסיף בדיקות נוספות (אורך מינימלי, תווים חוקיים).
    פונקציות validation מחזירות bool ולא זורקות exceptions.
    """
    if not name:
        return False
    return True


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    """
    בודקת אם לחייל יש תורנות עם שם מסוים.

    סוג: פונקציית validation (בדיקת תקינות)

    מקבלת:
        soldier (dict): מילון של חייל
        duty_name (str): שם התורנות לבדיקה

    מחזירה:
        bool: True אם התורנות קיימת לחייל
              False אם לא קיימת

    זורקת: כלום - תמיד מחזירה bool

    למה הפונקציה קיימת:
    בדיקה זו משמשת בהוספת תורנות (למנוע כפילויות).
    הפרדה של הלוגיקה למקום אחד.
    פונקציות validation מחזירות bool ולא זורקות exceptions.
    """
    for duty in soldier["duty"]:
        if duty["duty_name"] == duty_name:
            return True
    return False


def is_valid_day(day: str) -> bool:
    lst_days = ["sunday","monday","tuesday","wednesday","thursday"]
    return day.lower() in lst_days
