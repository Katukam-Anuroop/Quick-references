a = (1,2,3,4,5,6,7,8,9,10)

# a = () empty tuple
a = (1,) #single element tuple

a=(1)
# print(a)
a = ("anuroop", "shahid", "sajid", "shahid")

print(a[0:2])
print(a[0],a[-1])

# count
# index

a= ("anuroop","test")



print("count", a.count("shahid")) ## shahid is present 2 times
print("index", a.index("sajid")) ## 2 -- index of the first occurance - sajid is 2

#
tup_1 = (1,2,3)
tup_2 = (4, 5, 6)

print(tup_1 + tup_2)
#
print(tup_1*3) #(1,2,3,1,2,3,1,2,3)
## casting in python
a = 1
b = float(a)
c = str(a)
print(b,c)

a = [1,2,3]
b = tuple(a)
print(b) #(1, 2, 3)

# len
# max
# min
# sum
# sorted
#
# Sets
names = {"anuroop", "shahid", "sajid", "shahid"}
print(names)
set_m = {"anuroop",1,3.0,True}
# print(set_m[0])
for i in names:
    print(i)

# print(names[0])
# for i in range(len(names)):
#     print(names[0])


print('anuroop' in names)
# #
names.add("abhighna")
names.remove("abhighna") # removes - throws error if element is not present
names.discard("abhighna") # removes - does not throw error if element is not present
names.pop() # removes random element
names.clear() # removes all elements


list_1 = [1,2,3,4,5,6]
list_2 = [1,2,3,4,5,6] # union -- 1,2,3,4,5,6,7,8,9



#union -
#intersection
#subset
#difference
#symmetric difference
#superset

set_1 ={1,2,3,4,5}
set_2 ={3,4,5,6,7}



print("union",set_1.union(set_2))
print("intersection",set_1.intersection(set_2))

print("difference", set_1.difference(set_2))
print("difference", set_2.difference(set_1))

print("subset", set_1.issubset(set_2))
print("superset", set_2.issuperset(set_1))

print("symmetric difference", set_1.symmetric_difference(set_2))

# #len
# #min
# #max
#
# Dictionaries {"names":["anuroop","abhighna","sajid"],number_to_search : 5}
# key - value

anuroop = {"age":25,"gender":"male","name":"Anuroop Katukam","marks":[50,60,70,0]}
print(anuroop['name'])
objects= ["pen", "pencil", "eraser"]
colors = ["red", "blue", "green"]


eg = dict([("color","red"),('name','anuroop')])
print(eg)

anuroop["age"] = 31
anuroop["email"] = "anuroop@gmail.com"
print(anuroop)

print(anuroop.keys())
print(anuroop.values())
print(anuroop.items())
# anuroop = {"age":25,"gender":"male","name":"Anuroop Katukam","marks":[50,60,70]}
print(anuroop.get("marks",'no name available'))

for key in anuroop.keys():
    print("keys",key, anuroop[key])

for key, value in anuroop.items():
    print("items",key, value)

for value in anuroop.values():
    print(value)

anuroop['marks'].append(80)
anuroop['marks'][3] = 90
print(anuroop)

def words_cnt(words):
    words_count = {}

    for word in words.split():
        print(word, "each iteration")
        if word not in words_count:
            print(word, "initialising count")
            words_count[word] = 1
        else:
            print(word, "incrimenting count")
            words_count[word] += 1
    print(words_count)
    return words_count

def cnt_2():
    words = words_cnt("today today yesterday")
    for word in words.keys():
         if words[word] == 2:
             print(word)
             return(word)

cnt_2()
number_o_iterations = int(input("iterations "))
for i in range(number_o_iterations):
    a = int(input("a "))
    b = int(input("b "))
    print(a+b)

a = input()
print(a.split())
b = []
for i in a.split():
    b.append(int(i))
print(b)