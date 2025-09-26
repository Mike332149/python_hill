
#Program List cutter

list_original = [1,2,6,8,5,44,"top"]
x = len(list_original)
big_half =[]
small_half = []

if x % 2 == 0 :
    big_half = list_original[:len(list_original)//2 ]
    small_half = list_original[(len(list_original)//2):]
else:
    big_half = list_original[:(len(list_original) // 2 )+1]
    small_half = list_original[ (len(list_original) // 2 +1) :]

list_after_cut =[big_half] +[small_half]

print(list_original)
print(x)
print(list_after_cut)
