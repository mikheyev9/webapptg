from datetime import datetime, date

def calculate_time_until_birthday(birth_date: date) -> dict:
    now = datetime.now()
    next_birthday = datetime(now.year, birth_date.month, birth_date.day)
    if next_birthday < now:
        next_birthday = datetime(now.year + 1, birth_date.month, birth_date.day)
    delta = next_birthday - now
    return {
        "days": delta.days,
        "hours": delta.seconds // 3600,
        "minutes": (delta.seconds // 60) % 60
    }