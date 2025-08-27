#не зміний
#int
#complex
#float
#str
#bool
#tuple


#Змінний
#list
#dict
#set

#Оператори порівняння ### <, >, >=, <=, ==(равно), != (не равно), is, in, not

#and, or
MY_CONST = 10

#some_value = 2
#some_value2 = 4

#print(some_value)
#print(some_value2)
#print(some_value>some_value2)

#some_string = "Hello"
#some_string2 = "Hellooou"
#print(some_string)
#print(some_string2)
#print(some_string ==some_string2)

#some_value = 4
#some_value2 = 4.0
#print(some_value is some_value2)
#print(some_value == some_value2)

some_int = 34
some_int2 = 34

if some_int < some_int2 or some_int == some_int2:
    print(f"{some_int} is less than {some_int2}")

elif some_int == some_int2:
    print(f"{some_int} is equal to {some_int2}")

else:
    print(f"{some_int} is greater than {some_int2}")

print("end")