from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path('/path/to/file.txt')

# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')
