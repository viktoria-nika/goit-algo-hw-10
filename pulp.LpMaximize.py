# Імпортуємо бібліотеку PuLP

from pulp import *

# Для вирішення задачі створюємо модель, задача максимізації
model = LpProblem("Maximize_Drinks_Production", LpMaximize)

# Визначаємо рішення для кількості виробленого напою. 
# Створюємо змінні для кількості "Лимонаду" та "Фруктового соку", які можуть бути тільки невід’ємними цілими числами.
lemonade = LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість "Лимонаду"
juice = LpVariable('Juice', lowBound=0, cat='Integer')   # Кількість "Фруктового соку"

# Визначаємо цільову функцію, яку потрібно максимізувати
model += lemonade + juice, "Total_Production"

# Встановлюємо всі необхідні обмеження для ресурсів
model += 2 * lemonade + juice <= 100, "Water_Constraint"    # Вода
model += lemonade <= 50, "Sugar_Constraint"            # Цукор
model += lemonade <= 30, "Lemon_juice_Constraint"          # Лимонний сік
model += 2 * juice <= 40, "Fruit_puree_Constraint"             # Фруктове пюре

# Розв'язуємо модель
model.solve()

# Виводимо результати
print(f"Status: {LpStatus[model.status]}")
print(f"Кількість виробленого 'Лимонаду': {value(lemonade)}")
print(f"Кількість виробленого 'Фруктового соку': {value(juice)}")
print(f"Загальна кількість продуктів: {value(lemonade) + value(juice)}")