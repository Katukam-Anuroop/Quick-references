# print('hello anuroop, how are you ?')

# 1. ask user to enter first number
# 2. Choose the operator
# 3. Ask user to enter second number
# 4. click on equals to sign
# 5. check the output


# input("Choose the operator: ")

f_n = int(input("Enter first number: "))
s_n = int(input("Enter the second number: "))
output = f_n + s_n
print(f"first_number: {f_n} , second_number : {s_n}, addition_output = {output}")


# f_n = input("Enter first number: ")
# s_n = input("Enter the second number: ")
# print(int(f_n) + int(s_n))

# first_number: {f_n} , second_number : {s_n}, addition_output = {f_n + s_n}
# (first_number + second_number) * (third_number + fourth_number)

# f_n = 45
# s_n = 78
# print(f_n+s_n)

# print(7+10)

######################## Explaination of code ####################

f_n = int(input("enter first number"))
s_n = int(input("enter second number"))
output = f_n + s_n
print(f"first number:{f_n},second number:{s_n},addition output:{output}")


f_n = int(input("enter first number")) #- This line prompts the user to enter the first number, and then converts the input to an integer using the int() function. The result is stored in the variable f_n.

s_n = int(input("enter second number")) #- This line prompts the user to enter the second number, and then converts the input to an integer. The result is stored in the variable s_n.

output = f_n + s_n #- This line adds the two input numbers together and stores the result in the variable output.

print(f"first number:{f_n},second number:{s_n},addition output:{output}") #- This line uses an f-string to format and print the values of the first number, second number, and the addition output.