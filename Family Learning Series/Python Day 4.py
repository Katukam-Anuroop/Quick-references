# Strings
#
name = "Anuroop"
# """
# Anuroop
# 0123456
#
# """
print(len(name))
print("by inbuilt method",name[0:3])
for i in range(0,3):
    print(name[i],end='')
print("\n")
for i in range(0,len(name)):
    if i <3:
        print(name[i], end='')



print(name[0:7:2])
print("defualt", name[::2])
print(name[::-1])


# print("check",name[7:0])

for i in range(6,-1,-1):
    print(name[i],end = '')


#
# print(name[1])


a = 0
while a < 7:
    print(name[a])
    a +=2

a = 6
while a>=0:
    print(a, name[a])
    a -=1

for i in range(0,len(name),2):
    print(name[i])

# A n u r o o p
# A u o p

sen = "very Good morningggggggg hellogggggg world hi bye good GOod, GOOD" # n words n-1 spaces will be present.

# # index_of
count=0
for i in sen.lower():
    if i=='g':
        count+=1
print(count)

count=0
for i in range(0, len(sen)):
    if sen[i].lower() == 'g':
        if sen[i:i+4].lower() == 'good':
            count+=1

print(count)

count = 1
for i in sen:
    if i==' ':
        count+=1

print(count)




print(sen.upper())
print(sen.title())
print(sen.capitalize())
print(sen.lower())
#


a = [10,20,30,40,50,28,24,12,15]
print(a[2:9:2])
# print(a[-1])
# print("len",len(a))
for i in range(0,len(a)):
    print("indexing method",i,a[i])
#
for i in a:
    print("element method",i,i)

for i in range(0, len(a)):
    if a[i] == 30:
        print("index",a[i:])

for i in a:
    if i ==30:
        get_index = a.index(i)
        print(a[get_index:])
        print("element method",i,i)


a = ['Anuroop','Abhighna','Gnana SAi','Thirumalesh','Trinetra','Mokshagna']
b = [] #append
#
# b = 30
#
# print(type(b),b) # type(b) returns the datatype of the element
for i in range(0,len(a)):
    b.append(a[i].upper())
#
for i in a:
    b = i
    print(f"each iteration {i}",b.upper())
    b.append(i.upper()) # will return a list of all the elements in upper case

print(b)
fn = 2
sn = 3

single_if_cond =  fn if fn>sn else sn
print("if condi",single_if_cond)

single_for_list = [i.upper() for i in a]
print(single_for_list)

list_of_numbers = [2,3,4,5,6,7,3,4,5,6,7,8,3]

even_count = 0
odd_count = 0

for i in list_of_numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(even_count, odd_count)


even = []
odd = []

for i in list_of_numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even, odd)

for i in list_of_numbers:
    if i % 2 == 0:
        print(i)


even = [i for i in list_of_numbers if i % 2 == 0]
odd = [i for i in list_of_numbers if i % 2 == 1]

print("one liners",even, odd)



# for i in name:
#     print(i)
#     if i == 'u':
#         break





