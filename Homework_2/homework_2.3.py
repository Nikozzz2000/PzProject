# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

n = input("введите номер месяца в виде целого числа:")

month = ["0", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
         "Декабрь"]
season = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
          10: "Осень", 11: "Осень", 12: "Зима"}

while True:
    if type(n) != int:
        try:
            n = int(n)
        except ValueError:
            print("Неправильно ввели!")
            n = input("Введите число от 1 до 12: ")
    elif n > 12:
        print("Неправильно ввели!")
        n = int(input("введите номер месяца от 1 до 12:"))
        continue
    elif n <= 0:
        print("Неправильно ввели!")
        n = int(input("введите номер месяца от 1 до 12:"))
        continue
    else:
        print(month[n], "это", season.get(n))
        break
