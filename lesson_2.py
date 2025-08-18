# inmutable
# str String
# int Integer
# float 5.3
# bool Boolean

# mutable
# list List
# tuple
# dict Dictionary
# set


#some =[1]
#some2 =[1]
#print(id(some),id(some2))

#a = [1]
#b = [1]
#c = b
#print(id(a), id(b), id(c))

#greetings = ["Hello", "I'm Vova"]
#print(greetings[0])
#print(greetings[1])
#print(divmod(16,2))
#print(divmod(55,2))
#print(help(divmod))
#input_number = input("Enter number: ")
#input_number2 = input("Enter number2: ")

#print(type(input_number))
#print(input_number)

# Запитуємо вхідні дані у користувача
number = int(input("Введіть 4-х значне число: "))

# Витягуємо цифри за допомогою // та %
n1 = number // 1000               # тисячі
n2 = (number // 100) % 10         # сотні
n3 = (number // 10) % 10          # десятки
n4 = number % 10                  # одиниці

# Виводимо результат
print(type(number))
print(n1)
print(n2)
print(n3)
print(n4)
