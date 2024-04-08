class Concert:
    def __init__(self, name, band, times, venue, price_per_ticket):
        self.name = name
        self.band = band
        self.times = times
        self.venue = venue
        self.price_per_ticket = price_per_ticket

class Customer:
    def __init__(self, name):
        self.name = name
        self.total_cash = 0

    def buy_ticket(self, concert, time, seat_type, quantity, payment_method):
        total_price = concert.price_per_ticket * quantity
        print(f"{self.name} приобрестает {quantity} билет(ов) на концерт {concert.name} исполнителя {concert.band} в {time} на посадочном месте: {seat_type}.")
        print(f"Общая стоимость: ${total_price}")

        if payment_method.lower() == "карта":
            print(f"Оплачено методом: карта")
        elif payment_method.lower() == "наличка":
            while True:
                try:
                    cash_amount = float(input("Введите сумму наличными: $"))
                    self.total_cash += cash_amount  # Добавляем введенную сумму к общей сумме наличных
                    if self.total_cash < total_price:
                        print(f"Вам не хватает ${total_price - self.total_cash}.")
                    else:
                        change = self.total_cash - total_price
                        print(f"Сдача: ${change}")
                        break
                except ValueError:
                    print("Пожалуйста, введите корректную сумму.")

        print("Спасибо! Оплата прошла. Наслаждайтесь концертом.")


customer_name = input("Здравствуйте, представьтесь, пожалуйста: ")
customer = Customer(customer_name)

# Создаем объекты концертов с разными временами и ценами
concert1 = Concert("Light Night", "Alfie Jukes", ["19:00", "21:00"], "Manchester", 50)
concert2 = Concert("Pop Sensation Showcase", "Taylor Swift", ["20:00", "22:00"], "London", 60)
concert3 = Concert("Country Revolution Concert", "Lana Del Ray", ["18:00", "20:00"], "USA", 100)

# Предлагаем пользователю выбрать концерт и время
print("Доступные концерты:")
print("1. Light Night - Alfie Jukes - Manchester - 50$")
print("2. Pop Sensation Showcase - Taylor Swift - London - 60$")
print("3. Country Revolution Concert - Lana Del Ray - USA - 100$")

concert_choice = input("Выберите номер концерта, на который хотите пойти (1/2/3): ")

if concert_choice == "1":
    selected_concert = concert1
elif concert_choice == "2":
    selected_concert = concert2
elif concert_choice == "3":
    selected_concert = concert3
else:
    print("Некорректный выбор концерта.")
    exit()

print(f"Доступное время для концерта {selected_concert.name}:")
for i, time in enumerate(selected_concert.times):
    print(f"{i+1}. {time}")

time_choice = input("Выберите время концерта (1/2): ")
try:
    time_index = int(time_choice) - 1
    selected_time = selected_concert.times[time_index]
except (ValueError, IndexError):
    print("Некорректный выбор времени.")
    exit()

while True:
    seat_type = input("Выберите тип места (Площадка/Танцпол): ")
    if seat_type.lower() not in ["площадка", "танцпол"]:
        print("Некорректный выбор типа места. Пожалуйста, введите 'Площадка' или 'Танцпол'.")
    else:
        break

while True:
    try:
        quantity = int(input("Укажите количество билетов: "))
        if quantity <= 0:
            print("Количество билетов должно быть больше нуля.")
        else:
            break
    except ValueError:
        print("Пожалуйста, введите целое положительное число для количества билетов.")

while True:
    payment_method = input("Укажите метод оплаты (карта/наличка): ")
    if payment_method.lower() not in ["карта", "наличка"]:
        print("Некорректный метод оплаты. Пожалуйста, введите 'карта' или 'наличка'.")
    else:
        break

# Эмулируем покупку билетов
customer.buy_ticket(selected_concert, selected_time, seat_type, quantity, payment_method)
