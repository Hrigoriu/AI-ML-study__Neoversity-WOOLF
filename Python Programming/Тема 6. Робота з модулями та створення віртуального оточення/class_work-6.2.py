#============================================
""" 
Принцип KISS (Keep It Simple, Stupid)
"""
#============================================
def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

#============================================
def is_even(number: int) -> bool:
    return number % 2 == 0


#============================================
def is_palindrome(s: str) -> bool:
    new_s = ""
		for char in s:
		    if char.isalnum():
		        new_s += char.lower()
		
		s = new_s
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True


# Використання функції
print(is_palindrome("Козак з казок"))  # Виведе: True

#============================================
def is_palindrome(s: str) -> bool:
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower()

    s = new_s
    return s == s[::-1]


# Використання функції
print(is_palindrome("Козак з казок"))  # Виведе: True

#============================================
"""
Принцип DRY (Don't Repeat Yourself)
"""
#============================================
# Розрахунок площі 
length1, width1 = 5, 10
area1 = length1 * width1

# Багато різного коду

length2, width2 = 7, 12
area2 = length2 * width2


def calculate_area(length: float, width: float) -> float:
    return length * width


area1 = calculate_area(5, 10)
area2 = calculate_area(7, 12)


#============================================
def calculate_area(length: float, width: float) -> float:
    return length * width


area1 = calculate_area(5, 10)
area2 = calculate_area(7, 12)
print(f"Area 1: {area1}, Area 2: {area2}")


#============================================
# math_operations.py
def calculate_area(length, width):
    return length * width


#============================================
from math_operations import calculate_area

area1 = calculate_area(10, 5)
area2 = calculate_area(20, 15)
print(f"Area 1: {area1}, Area 2: {area2}")
#============================================
"""
Єдина точка входу проєкту
"""
#============================================
#main.py
from my_module import my_function


def main():
    my_function()


if __name__ == "__main__":
    main()

#============================================

#============================================

#============================================
