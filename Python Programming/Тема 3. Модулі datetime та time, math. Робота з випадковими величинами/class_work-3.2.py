# Один мільйон
a = 1_000_000
print(a)  # Виведе 1000000

# Десять мільйонів
b = 10_000_000
print(b)  # Виведе 10000000

# Один мільярд
c = 1_000_000_000
print(c)  # Виведе 1000000000
#=======================================================
"""
метод, наприклад, підходить для симуляції кидка кубика:
"""
import random

dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")
#=======================================================

import random

num = random.random()
print(num)
#=======================================================

import random

fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")
#=======================================================

import random
print(random.randrange(10))  # Верхня межа є 10, але не включається
#=======================================================

import random

target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")
#=======================================================

import random

cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

random.shuffle(cards)

print(f"Перемішана колода: {cards}")
#=======================================================

import random

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))
#=======================================================

import random

items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
print(chosen_item)  
#=======================================================

import random

numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers)
#=======================================================

import random

colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)  
#=======================================================

import random

participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")
#=======================================================

import random

price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")
#=======================================================

