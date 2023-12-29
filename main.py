meters = float(input("Введіть кількість метрів: "))
choice = int(input("Оберіть одиницю вимірювання (1 - милі, 2 - дюйми, 3 - ярди): "))

if choice == 1:
    print(meters * 0.000621371192)
elif choice == 2:
    print(meters * 39.3700787)
elif choice == 3:
    print(meters * 1.0936133)
else:
    print("Невірний вибір одиниці вимірювання.")
