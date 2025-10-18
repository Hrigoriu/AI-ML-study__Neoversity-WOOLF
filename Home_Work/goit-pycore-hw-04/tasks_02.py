"""
Завдання 2
У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:

60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5

Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

Вимоги до завдання:
Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
Функція має повертати список словників, де кожен словник містить інформацію про одного кота.

Рекомендації для виконання:
Використовуйте with для безпечного читання файлу.
Пам'ятайте про встановлення кодування при відкриті файлів
Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
Опрацьовуйте можливі винятки, пов'язані з читанням файлу.

Критерії оцінювання:
Функція має точно обробляти дані та повертати правильний список словників.
Повинна бути належна обробка винятків і помилок.
Код має бути чистим, добре структурованим і зрозумілим.

Приклад використання функції:
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)

Очікуваний результат:
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
"""

import os


def get_cats_info(path: str) -> list[dict]:
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:               
                clean_line = line.strip()  # Видалимо зайві пробіли на початку та в кінці рядка
                if not clean_line:
                    continue  # Пропустимо порожні рядки

                try:
                    # Розділимо рядок на три частини
                    parts = clean_line.split(',')
                    if len(parts) == 3:
                        cat_id, name, age = parts
                        cats_list.append({
                            "id": cat_id,
                            "name": name,
                            "age": age
                        })
                    else:
                        print(f"Попередження: Неправильний формат рядка, рядок ігноровано: '{clean_line}'")
                except ValueError:
                    print(f"Попередження: Не вдалося розпакувати дані, рядок ігноровано: '{clean_line}'")

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася непередбачувана помилка: {e}")
        return []

    return cats_list

# --- Створимо тестовий файл та папки поруч зі скриптом ---
# 1. Отримаємо шлях до папки, де знаходиться цей скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Створимо шлях до папки 'data'
data_dir_path = os.path.join(script_dir, 'data')

# 3. Створимо папку 'data', якщо її не існує
if not os.path.exists(data_dir_path):
    os.makedirs(data_dir_path)

# 4. Створимо повний шлях до файлу 'cats_file.txt'
file_path = os.path.join(data_dir_path, 'cats_file.txt')

# 5. Запишемо дані у файл
with open(file_path, 'w', encoding='utf-8') as f:
    f.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
    f.write("60b90c2413067a15887e1ae2,Vika,1\n")
    f.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
    f.write("BrokenLine,Simon\n")  # Пошкоджений рядок для тестування
    f.write("60b90c3b13067a15887e1ae4,Simon,12\n")
    f.write("\n")  # Порожній рядок для тестування
    f.write("60b90c4613067a15887e1ae5,Tessi,5\n")

print(f"Тестовий файл успішно створено: {file_path}")

# --- Створимо приклад використання функції ---
print("\n--- Результат роботи функції ---")
cats_info = get_cats_info(file_path)
print(cats_info)

# --- Створимо приклад з неіснуючим файлом ---
print("\n--- Спроба прочитати неіснуючий файл ---")
non_existent_path = os.path.join(data_dir_path, "non_existent_cats.txt")
get_cats_info(non_existent_path)
