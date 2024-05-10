# list_of_numbers = [2,3,4,5,6,7,3,4,5,6,7,8,3]
# # print(list_of_numbers[-5:])
# # list_of_numbers[0:5] = [1,2,3,4,5]
# print(list_of_numbers[0])
#
# list_of_numbers.sort()
#
# print("sorted",list_of_numbers)
# list_of_numbers.sort(reverse = True)
# print("descending",list_of_numbers)
#
# import random
# random.shuffle(list_of_numbers)
# print("random", list_of_numbers)

"""
list = [1,2,3,4,5]
        0,1,2,3,4
random_index = [3,2,1,0,4]
shuffled_list = [4,3,2,1,5]
"""

names = ['anuroop','Abhighna','Gnana SAi','Thirumalesh','Trinetra','Mokshagna', 'sky','trotten']
# exercise for today -- get the strings/words which starts_with (a and t) and store it a new list or return a new list
# String methods - startswith & endswith


# result_con = []
# for i in names:
#     if i.startswith('a') or i.startswith('A'):
#         result_con.append(i)
# print(result_con)
#
# result_low = []
# for i in names:
#     if i.lower().startswith('a'):
#         result_low.append(i)
# print(result_low)
#
# result_low = []
#
# for i in names:
#     if i.lower().startswith('a') or i.lower().startswith('t'):
#         result_low.append(i)
# print(result_low)
result = []
for i in names:
    for j in i:
        if j.lower()=='a':
            print(j,i)
            result.append(i)
            break

print("nested for loop",result)
result = []
for i in names:
    if 'a' in i:
        print('without nested',i)
        result.append(i)

print(result)


a = [1,1,2,2,3,3,4,4,5,6,6]
unique = []
for i in a:
    if i in unique:
        print("its already there: duplicate", i)
    else:
        unique.append(i)

print("unique", unique)

unique_var = []
for i in a :
    if i not in unique_var:
        unique_var.append(i)
    else:
        print("duplicate", i)

print(unique_var)


a = [1,1,2,2,3,3,4,4,5,6,6]

count = []
for i in a:
    if a.count(i) ==1: # count the number of times the number is repeated
        print(i)

from collections import Counter

count = Counter(a)

for i, count in count.items():
    if count == 1:
        print(i)


# names.sort()
# print(names)
#
# names.sort(key = str.lower)
# print("lower", names)
#
# names.reverse()
# print("reverse", names)


# append()
# extend()
# remove()
#  pop()
#  del()
#  clear()
#  insert()
# sort()
# sort(reverse = True)
#  reverse()




# random -- independent package


# for i in range(0,5):
#    list_of_numbers[i] = i+1

### insert
#
# list_of_numbers.insert(9,"Anuroop")
#
# print(list_of_numbers)
#
# list_1 =[1,2,3]
# list_2 = [4,5,6]
#
# for i in list_2:
#     list_1.append(i)
#
# print("append",list_1)
# a = list_1 + list_2
#
#
#
# print("before extend",a)
# list_1.extend(list_2)
# #
# # print(list_1)
# #
# #
# a = list_1 + list_2
#
# print("after extended",a)
# list_1 =[1,1,2,2,6,6]
# print("list_1",list_1)
# list_1.remove(6)
# print("updated",list_1)
# list_1.pop(1)
# print("pop", list_1)
# del list_1[-1]
# print("del", list_1)
# list_1.clear()
# print("clear", list_1)