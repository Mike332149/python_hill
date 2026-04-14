import random

# Створюємо список із 10 випадкових чисел (наприклад, від 1 до 100)
numbers = [random.randint(1, 100) for _ in range(10)]

# Формуємо новий список:
# 1-й елемент -> numbers[0]
# 3-й елемент -> numbers[2]
# 2-й з кінця -> numbers[-2]
new_list = [numbers[0], numbers[2], numbers[-2]]

print("Початковий список:", numbers)
print("Новий список:", new_list)