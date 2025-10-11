this_is_string = "Hi there!"

the_same_string = 'Hi there!'

this_is_string == the_same_string  # True
#====================================================================

text = """This is first line
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''
#====================================================================

one_line_text = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
#====================================================================

one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."
#====================================================================
("spam " "eggs") == "spam eggs"  # True
#====================================================================

one_line_text = ("Textual data in Python is handled with str objects,"
                " or strings. Strings are immutable sequences of Unicode"
                " code points. String literals are written in a variety "
                " of ways: single quotes, double quotes, triple quoted.")
#====================================================================

query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")
#====================================================================

print("Hello\nWorld")
#====================================================================

print("Hello\tWorld")
#====================================================================

print("Hello my little\rsister")
#====================================================================

print("Hello\bWorld")
#====================================================================

print("Hello\\World")
#====================================================================

print('It\'s a beautiful day')
print("He said, \"Hello\"")
#====================================================================

s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end))  # 5
print(s.find("q"))  # -1
#====================================================================

s = 'Some words'

print(s.find("o"))
print(s.rfind('o'))
#====================================================================

s = 'Some words'

print(s.index("o"))
print(s.rindex('o'))
#====================================================================

text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']
#====================================================================

text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']
#====================================================================

list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'
#====================================================================

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'
#====================================================================

clean = '   spacious   '.strip()
print(clean)  # spacious
#====================================================================

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) 
#====================================================================

text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)  
#====================================================================

text = "Hello, world!"
new_text = text.replace(" world", "")
print(new_text)
#====================================================================

print('TestHook'.removeprefix('Test'))  # Hook
print('TestHook'.removeprefix('Hook'))  # TestHook
#====================================================================

print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))
#====================================================================

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)
#====================================================================

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)
#====================================================================

number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False
#====================================================================

user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")
#====================================================================

for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")
#====================================================================

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example"
print(str.translate(trantab))
#====================================================================

intab = "aeiou"
trantab = str.maketrans('', '', intab)

str = "This is string example"
print(str.translate(trantab))
#====================================================================

symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]

MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

result = "34 DF 56 AC".translate(MAP)
print(result)
#====================================================================
"""
Наступний приклад, це розробити програму, яка перетворює вхідний текстовий рядок на відповідний код мови Морзе.
"""
morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# Перетворення ключів словника на Unicode коди
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "Hello world"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)
#====================================================================

string = "Hello world"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)
#====================================================================

for i in range(8):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)
#====================================================================

price = 19.99
quantity = 3
total = f"Total: {price * quantity:.2f}"
print(total)
#====================================================================

width = 5
for num in range(12):
    print(f'{num:^10} {num**2:^10} {num**3:^10}')
#====================================================================

name = "Alice"
formatted = f"{name:>10}"
print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)
#====================================================================
"""
Вирівнювання визначає, як вміст буде вирівняний всередині вказаної ширини поля. Можливі варіанти вирівнювання:
<: Вирівнювання вмісту по лівому краю.
>: Вирівнювання вмісту по правому краю.
^: Вирівнювання вмісту по центру.
=: Використовується для вирівнювання чисел, при цьому знак (якщо він є) відображається зліва, а число - по правому краю поля.
"""
#====================================================================
completion = 0.756
formatted = f"{completion:.1%}"
print(formatted)  # Виведе: '75.6%'

#====================================================================
progress = 0.5
formatted = f"{progress:.0%}"
print(formatted)
