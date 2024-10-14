from datetime import datetime, timedelta

def future_date(days_from_now):
    """
    Возвращает дату, которая наступит через указанное количество дней от текущей даты.
    :param days_from_now: Количество дней от текущей даты.
    :return: Отформатированная дата в формате YYYY-MM-DD.
    """
    # Получение текущей даты и времени
    today = datetime.now()
    
    # Вычисление будущей даты через указанное количество дней
    future_date = today + timedelta(days=days_from_now)
    
    # Форматирование будущей даты в строку в формате YYYY-MM-DD
    return future_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    days = 30  # Количество дней для вычисления
    print(f'Date {days} days from now: {future_date(days)}')
