import datetime
from dateutil.relativedelta import relativedelta
import csv

def read_data(filename, product_name):
    data = []
    today = datetime.date.today()
    last_month_date = today - relativedelta(months=1)
    print(f"Аналіз даних з {last_month_date} до {today}")  # Для відладки

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            product, date_str, price = line
            date = datetime.datetime.strptime(date_str.strip(), '%Y-%m-%d').date()
            if product.strip() == product_name:
                data.append((date, float(price)))
                if date >= last_month_date:
                    print(f"Додано: {product} {date} {price}")  # Для відладки

    data.sort()
    return [item for item in data if item[0] >= last_month_date]  # Фільтрація за датою знову

def analyze_price_changes(data):
    if not data:
        return "Немає даних за останній місяць для цього товару."

    start_price = data[0][1]
    end_price = data[-1][1]
    price_change = end_price - start_price
    return f"Зміна ціни: {price_change:.2f}. Початкова ціна: {start_price:.2f}, Кінцева ціна: {end_price:.2f}"
filename = 'data.txt'
product_name = 'Milk'
data = read_data(filename, product_name)
result = analyze_price_changes(data)
print(result)