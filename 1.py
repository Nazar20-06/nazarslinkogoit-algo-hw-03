from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка у дату
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Поточна дата (без часу)
        today = datetime.today().date()
        # Різниця в днях
        delta = today - input_date
        return delta.days
    except ValueError:
        # Якщо дата в неправильному форматі
        print("Неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'.")
        return None
