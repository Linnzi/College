from math import *
from tabulate import tabulate

a, b, h = map(float, input("Введите начало, конец и шаг через пробел: ").split())

results = []
current_x = a

# Расчет значений в цикле
# Добавляем h/10 к верхней границе, чтобы из-за погрешности не потерять точку b
while current_x <= b + (h / 10):
    f_x = current_x - sin(current_x)
    
    # Сохраняем значения в список для таблицы
    results.append([round(current_x, 4), round(f_x, 6)])
    
    current_x += h

# Вывод готовой таблицы
headers = ["x", "F(x) = x - sin(x)"]
print("\nТаблица значений функции:")
print(tabulate(results, headers=headers, tablefmt="grid"))
# При значениях a = 0; b = 2; h = 0,5
# x = 0.0 == 0 - sin(0), вывод - 0.0
# x = 0.5 == 0.5 - sin(0.5), вывод - 0.0205744614 (калькулятор)
# x = 1.0 == 1 - sin(1), вывод - 0.158529015 (калькулятор)
# x = 1.5 == 1.5 - sin(1.5), вывод - 0.502505013 (калькулятор)
# x = 2.0 == 2 - sin(2), вывод - 1.09070257 (калькулятор)