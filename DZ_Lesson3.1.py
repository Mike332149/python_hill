

# Запитуємо вхідні дані у користувача
number = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
action = str(input("Введіть одну з матиматичних дій:+,-,*,/: "))


if action == "+":
    result = number + number2
    print( result)
if action == "-":
    result = number - number2
    print(result)
if action == "*":
    result = number * number2
    print(result)
if action == "/" and number2 !=0:
    result = number / number2
    print(result)
else:print("Дільник не повинен дорівнювати 0!!! ")

