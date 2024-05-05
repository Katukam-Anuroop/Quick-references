# Strings
#
# name = "Anuroop"
# """
# Anuroop
# 0123456
#
# """
# # print(len(name))
# # print("by inbuilt method",name[0:3])
# # for i in range(0,3):
# #     print(name[i],end='')
# # print("\n")
# # for i in range(0,len(name)):
# #     if i <3:
# #         print(name[i], end='')
#
#
# #
# # print(name[0:7:2])
# # print("defualt", name[::2])
# # print(name[::-1])
# #
# #
# # print("check",name[7:0])
# #
# # for i in range(6,-1,-1):
# #     print(name[i],end = '')
#
#
# #
# # print(name[1])
#
#
# a = 0
# while a < 7:
#     print(name[a])
#     a +=2
#
# a = 6
# while a>=0:
#     print(a, name[a])
#     a -=1
#
# for i in range(0,len(name),2):
#     print(name[i])

# A n u r o o p
# A u o p

sen = "very Good morningggggggg hellogggggg world hi bye good GOod, GOOD" # n words n-1 spaces will be present.

# # index_of
# count=0
# for i in sen.lower():
#     if i=='g':
#         count+=1
# print(count)

count=0
for i in range(0, len(sen)):
    if sen[i].lower() == 'g':
        if sen[i:i+4].lower() == 'good':
            count+=1

print(count)

# count = 1
# for i in sen:
#     if i==' ':
#         count+=1
#
# print(count)




# print(sen.upper())
# print(sen.title())
# print(sen.capitalize())
# print(sen.lower())
#
# a = [10,20,30,40,50]
#
# for i in range(0,len(a)):
#     print(a[i])
#
# for i in a:
#     print(i)
#
# for i in name:
#     print(i)
#     if i == 'u':
#         break





