# names = ['anuroop','Abhighna','Gnana SAi','Thirumalesh','Trinetra','Mokshagna', 'sky','trotten']

"""
expected output ['pooruna','anhgihba']
Hint : str[::-1]
"""
# result = []
# for str in names:
#     result.append(str[::-1])
# print(result)
#
# result = [str[::-1] for str in names]
"""
Question 2: Count the number of vowels in each string and return a list of integers
"""
# count_vowels = [0,0,0,0,0,0,0,0]
# for i in range(len(names)):
#     for j in names[i]:
#         if j.lower() in 'aeiou':
#             count_vowels[i] += 1
#
# print(count_vowels)
#
# count_vowels = [0,0,0,0,0,0,0,0]
# for i in range(len(names)):
#     for j in names[i]:
#         if j.lower() == 'a' or j.lower() == 'e' or j.lower() == 'i' or j.lower() == 'o' or j.lower() == 'u' :
#             count_vowels[i] += 1
#
# print(count_vowels)

"""
Exercise : Find the count of consonants in each string and return a list of integers.
"""
"""
Question 3: Find the sum of numbers in a list.
a = [1,2,3,4,5] Hint : sum += i
"""
# a = [1,2,3,4,5]
# sum_=0
# for i in a:
#     sum_+=i
# print(sum_)
#
# print(sum(a))
"""
Exercise : Find the product of numbers in a list., 
Exercise : Find sum of odd numbers and even numbers in a list.
"""

"""
Question 4: Can you check if the given list is in ascending order?
[1,2,3,4,5] range(0,len(list)-1)
"""
# a= [1,2,5,4,3]
# for i in range(0,len(a)-1):
#     if a[i] < a[i+1]:
#         print("yes")
#     else:
#         print("not in ascending order")
#         break
#
# a= [1,2,5,4,3]
# for i in range(0,len(a)-1):
#     if a[i] > a[i+1]:
#         print("not in ascending order")
#         break
#
#     else:
#         print("Ascending Order")





"""
Question 5: Find the second largest number in the list. -- Exercise
[1,4,3,2,5] --> [1,2,3,4,5]
"""
"""          0          1             2         3           4           5          6       7      """
names = ['anuroop','Abhighna','Gnana SAi','Thirumalesh','Trinetra','Mokshagna', 'sky','trotten']
count = [0,0,0,0,0,0,0,0]
"""      0 1 2 3 4 5 6 7       """

# for name in names:
#     print(name)
#     for chr in name:
#         print(chr)
#         if chr == 'a' or chr =='e' or chr =='i' or chr =='o' or chr =='u':
#             print("yes")
#             # count+=1

# vowels = ['a','a','e','i','o','u']
# for index in range(len(names)):
#     print(index, names[index])
#     for chr in names[index]:
#         if chr.lower() == 'a' or chr.lower() =='e' or chr.lower() =='i' or chr.lower() =='o' or chr.lower() =='u': ## if chr in vowels:
#             count[index] = count[index] + 1 ## count[index] +=1
#             print(chr,count)
#
# print(count)



# count = [0,0,0,0,0,0,0,0]
# # count[0] = count[0]+1
# # count[1] = count[1]+1
# # count[2] = count[2]+1
# # count_ex =[]
# # for i in count:
# #    count_ex.append(i+1)
# # print("element method", count_ex)
#
# for i in range(len(count)):
#     count[i] = count[i]+1



"""
check if the given string is palindrome or not.
11011
Extension -- take a list of palindromes and not palindromes. and count number of palindromes == ['11011','1111']
"""
a ="11011"
if a == a[::-1] :
    print("palindrome")
else:
    print("not palindrome")

"""
list_nums = ["123", "456", "789"]
output = ["6","15","24"]
"""
list_nums = ["123", "456", "789","1234","12345"]
output = []

for number in list_nums:
    print(number, type(number))
    sum_ = 0
    for char in number:
        sum_ = sum_ + int(char)
    output.append(str(sum_))

print(output)








