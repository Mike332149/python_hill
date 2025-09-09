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
#MY_CONST = 10

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

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# lst3 = lst1
#
# print(id(lst1), id(lst2), id(lst3))
# print(lst1 is not lst2)
# print(lst1 is lst3)



#some_value = 4
#some_value2 = 4.0
#print(some_value is some_value2)
#print(some_value == some_value2)

# some_int = 30
# some_int2 = 34
#
# if some_int < some_int2 or some_int == some_int2:
#     print(f"{some_int} is less than {some_int2}")
#
# elif some_int == some_int2:
#     print(f"{some_int} is equal to {some_int2}")
#
# else:
#     print(f"{some_int} is greater than {some_int2}")
#
# print("end")
#
# some_int = 19
# some_int2 = 20
#
# #some_value = 10 if some_int < some_int2 else 20
#
# if some_int < some_int2:
#     some_value = 10
# else:
#     some_value = 20
# print(some_value)

from copy import deepcopy
lst = [2,3.4, True, "hello", [1,4],6]
#lst1 = list()
#print(lst[5][0])
my_list = [1,2,3]
#print(my_list *3) #всі елементи з початку до 3-го включно
#print(my_list[2]) #другий елемент
#print(lst[-2]) #другий з кінця елемент списк
#print(lst[3:]) #друк всіх елементів починаючи з 3-го елемента

#my_list[2] = 10 #changing one of element in list
#del my_list[2] #deliting one of element of list

new_list = deepcopy(lst) + my_list
lst[2] = False #changing element1 in element4 on  value 5
lst[4][1] = 5
print(new_list)
print(lst)
print(my_list)
print ("hello" in lst)
print(len(lst))