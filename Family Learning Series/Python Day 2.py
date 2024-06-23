# # input("Choose the operator: ")
# # import time
# # start_time = time.time()
#
f_n = int(input("Enter first number: "))
operator = input("Choose the operator: ")
s_n = int(input("Enter the second number: "))

output =0
print(f_n,s_n,operator)
# assume that i am giving an input as '+' to operator variable
# operator will have '+'

if operator == '+':
    print(" i am inside if condition, i will only here if operator has '+' ")
    output = f_n + s_n
    print("first condition")
elif operator == '-':
    print(" i am inside if condition, i will only here if operator has '-' ")
    output = f_n - s_n
    print("second condition")
elif operator == '*':
    print(" i am inside if condition, i will be only here if operator has '*' ")
    output = f_n * s_n
    print("third condition")
elif operator == '/':
    print(" i am inside if condition, i will only here if operator has '/' ")
    output = f_n / s_n
    print("fourth condition")

# elif operator == '*':
#     print(" i am inside if condition, i will be only here if operator has '*' ")
#     output = f_n * s_n
#     print("fifth condtion")

print(f"first_number: {f_n} , second_number : {s_n}, addition_output = {output}")

# end_time = time.time() - start_time
# print(end_time)
# f_n = 3
# s_n = 2
#
# if f_n == s_n:
#     print("both are equal")
# elif f_n > s_n:
#     print("first is greater")
# else:
#     print("second is greater than first")

# print(3%2)

"""
if any given number is completely divisible by 2 ( which returns remainder 0 ) then it is a even number.. else odd.
if number%2 ==0:
    even number
else:
    odd number

ex1 : f_n = 3, s_n = 3 output = 6 (+)
ex2 : f_n = 2, s_n = 4 output = 8 (*)
"""

#


print(10//3)



f_n = int(input("Enter first number: "))
s_n = int(input("Enter the second number: "))
if f_n % 2 == 0 and s_n %2 ==0 :
    print(f_n*s_n)
elif f_n % 2 != 0 and s_n %2 !=0 :
    print(f_n+s_n)

count=0
for i in range(1,100):
    if i % 2 !=0 :
        count+=1
        print(count)
        if i == 50:
            break