# Data Types
"""
1. String - str -- eg
2. Integer - int -- eg
3. Decimal - float
4. complex numbers - complex (5+i8)
5. List - list    --- sequence / DS
6. Tuples - tuple ---- seq / DS
7. Range - range --- seq -- eg
8. Dictionary - dict --- DS / mapping
9. Set - set --- Set type / DS
10. Boolean --- bool ---- True / False
"""

# Operators

"""
1. Arithmetic Operators --  +,-,*,/,%,//
2. Assignment operators -- =,+=,-=,*=,/=,%=,//=
3. Comparison Operators -- ==,>,<,>=,<=,!=
4. Logical Operators -- and, or , not
5. Identity Operators -- is , is not
6. Membership Operators --  in , not in 
6. Bitwise Operators -- & , | , ^ , ~ , << ,>>

"""

# f_n = 3
# s_n = 3
#
#
# if (f_n%2==0) and (s_n % 2 == 0):
#     print(f_n * s_n)
#
# if f_n%2 == 1 and s_n % 2 == 1:
#     print(f_n + s_n)
#
# if f_n%2 == 0 and s_n % 2 == 1:
#     print(f_n / s_n)
#
# if f_n%2 == 1 and s_n % 2 == 0:
#     print(f_n - s_n)



#### Loops
# 1. for loop
# 2. While Loop
# print by default prints numbers in new line because of a escape character \n
# for counter in range(1,101):
#     print(counter , end = "-")
"""
use for loop and if condition together to print first 50 odd numbers.
"""
# Any number when divided by two leaves either 0 or 1 as a remainder. So, if the remainder is 1, then the number is odd.
# for number in range(1,100):
#     if number%2 == 1: # (condition for odd)
#         print(number)
#
# for number in range(1,100):
#     if number%2 != 0: # (Not an even)
#         print(number)

# PEP guidelines
# count = 0
# for number in range(425,1000):
#     print("i am inside the loop")
#     if number%2 == 1:  # (condition for odd)
#         print(" I am the odd condition")
#         #count = count + 1 # or count +=1
#         count += 1
#         print(f'number - {number} : count - {count}')
#         if count == 50:
#             print(" i am here at 50")
#             break


# count = 0
# for number in range(1,1000):
#     print("i am inside the loop")
#     if number%2 == 1 and count <= 50: # (condition for odd)
#         print(" I am the odd condition")
#         #count = count + 1 # or count +=1
#         count += 1
#         print(f'number - {number} : count - {count}')
#     else:
#         break

"""
number =0
while number<=100:
    print("anuroop",number)
    number += 1
    
"""

# number =0
# while True:
#     if number <=100:
#         print("anuroop _ if",number)
#         number += 1
#     else:
#         break

# while True:
#     f_n = int(input("Enter first number: "))
#     operator = input("Choose the operator: ")
#     s_n = int(input("Enter the second number: "))
#
#     output = 0
#     print(f_n, s_n, operator)
#     # assume that i am giving an input as '+' to operator variable
#     # operator will have '+'
#
#     if operator == '+':
#         print(" i am inside if condition, i will only here if operator has '+' ")
#         output = f_n + s_n
#         print("first condition")
#     elif operator == '-':
#         print(" i am inside if condition, i will only here if operator has '-' ")
#         output = f_n - s_n
#         print("second condition")
#     elif operator == '*':
#         print(" i am inside if condition, i will be only here if operator has '*' ")
#         output = f_n * s_n
#         print("third condition")
#     elif operator == '/':
#         print(" i am inside if condition, i will only here if operator has '/' ")
#         output = f_n / s_n
#         print("fourth condition")
#
#     print(f"first_number: {f_n} , second_number : {s_n}, output = {output}")

# for i in range(0,2):
#     f_n = int(input("Enter first number: "))
#     operator = input("Choose the operator: ")
#     s_n = int(input("Enter the second number: "))
#
#     output = 0
#     print(f_n, s_n, operator)
#     # assume that i am giving an input as '+' to operator variable
#     # operator will have '+'
#
#     if operator == '+':
#         print(" i am inside if condition, i will only here if operator has '+' ")
#         output = f_n + s_n
#         print("first condition")
#     elif operator == '-':
#         print(" i am inside if condition, i will only here if operator has '-' ")
#         output = f_n - s_n
#         print("second condition")
#     elif operator == '*':
#         print(" i am inside if condition, i will be only here if operator has '*' ")
#         output = f_n * s_n
#         print("third condition")
#     elif operator == '/':
#         print(" i am inside if condition, i will only here if operator has '/' ")
#         output = f_n / s_n
#         print("fourth condition")
#
#     print(f"first_number: {f_n} , second_number : {s_n}, output = {output}")


"""
1,100
numbers divisible by 5 less than 100 : 5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95
hint : if number%5 ==0: then that number is divisible by 5

numbers divisible by 3 less than 60 : 3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57

hint : if number%3 ==0: then number is divisible by 3
exe : 5/3,10/6,15/9,20/12,25/15,30/18,35/21,40/24,45/27,50/30,55/33,60/36....
output : sum(exe)

"""

# a = 1
# b = 1
# c = 0
# for i in range(1, 100):
#     if i % 5 == 0:
#         a = i
#     if i % 3 == 0 and i < 60:
#         b = i
#     c = c + a/b
#     print(f"a - {a}, b - {b}, output= {a/b}")
# print(f"c - {c}")

"""
starting from 1990, 2024. print all leap years
if the year ends with 0 or 00 then it has to be divisible by 100 or 400

check dividing with 4, for those year which doesnt end with 00, else divide by 400
"""

for year in range(1800, 2000):
    if (year % 4 == 0 and year%100 !=0) or (year % 400 == 0):
        print(year)


"""
a,b,c three sides of a triangle

1. Equilateral triangle : all sides are equal
2. Isosceles triangle : 2 sides are equal
3. Scalene triangle : all sides are different

"""
a=2
b=2
c=2

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or c == a:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


"""
1,100
5,15,25,35,45,55,65,75,85,95
2,12,22,32,42,52,62,72,82,92
exe : 5/2,15/12,25/22,35/32,45/42,55/52,65/62,75/72,85/82,95/92
output : sum(exe)

"""
