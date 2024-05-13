
"""
find the average of given list:
a = [1,2,3,4,5]
average = (1+2+3+4+5)/5 ---> (sumof numbers in a list) / len(list)
"""
# a = [1,2,3,4,5]
# sum_=0
# for i in a:
#     sum_+=i
# print(int(sum_/len(a)))

"""
find the missing number in a list [1,2,3,4,6,7] --> expected output --> 5 is missing
"""
"""a[0] = 1 ----> 0 --i
a[1] = 2 ----> 1 --i+1"""
# a = [1,2,3,4,6,7]
# for i in range(0,len(a) -1):
#     print(f"index : {i}, iterative number in list : {a[i]}, number +1 : {a[i]+1}, next index number {a[i+1]}")
#     if a[i] +1 == a[i+1]:
#         print("no missing number")
#
#     else:
#         print(f"missing number is {a[i]+1}")



"""


string_ = "Anu has 10 mangoes, abhi has 5 , gnana has 3 , thirumalesh has 8 , trinetra has 4 , mokshagna has 2"
sum all the numbers in the string and print the sum.
expected output --> 32

split() ---> split the string into list of words
"""
string_ = "Anu has 10 mangoes, abhi has 5 , gnana has 3 , thirumalesh has 8 , trinetra has 4 , mokshagna has 2"
# print(string_.split(' '))
# print('100000'.isdigit())
sum_=0
for i in string_.split(' '):
    if i.isdigit():
        sum_ += int(i)
print(sum_)
"""
check if the given strings are anagrams or not.
"""
"silent" "listen"




"""
max([15,20,89,12,45,67]) -- find max number without sorting the list.

"""

"""
lst_1 = [1,2,3,4,5]
lst_2 = [1,2,3,4,5]
output = [2,4,6,8,10]
"""
lst_1 = [1,2,3,4,5]
lst_2 = [1,2,3,4,5]
result = []
for i in range(len(lst_1)):
    print(i, lst_1[i],lst_2[i])
    result.append(lst_1[i] + lst_2[i])
print(result)

result = []
for i,j in zip(lst_1, lst_2):
    result.append(i+j)

"""
a - [12,23,26,3,5,6]
output - list of corresponding alphabets.

"""

## codechef
## hackerearth
## hackerrank
## leetcode