"""
Приклад. Для кава-брейків на конференції закуплено круасани, стаканчики та пакунки кави. Ціна круасана — $1.04, ціна стаканчика — $0.34, ціна пакунка кави — $4.42. Потрібно класти програму, яка обчислює, скільки повних доларів пішло на закупівлю їжі для кава-брейків і яка її повна вартість у центах.
"""
# Встановлюємо ціни на продукти
price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffee_pack = 4.42

# Кількість кожного продукту
num_croissants = int(input("Введіть кількість круасанів: "))
num_glasses = int(input("Введіть кількість склянок: "))
num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# Обчислення загальної вартості
total_cost = num_croissants * price_per_croissant + \
             num_glasses * price_per_glass + \
             num_coffee_packs * price_per_coffee_pack

# Визначаємо кількість повних доларів і центів
total_dollars = int(total_cost)
total_cents = int(total_cost * 100)

# Вивід результату
print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
print(f"Загальна вартість у центах: {total_cents} центів")
