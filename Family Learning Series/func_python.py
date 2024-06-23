def name_of_function(username):

    """
    Docstring explains what the function does
    """
    print("Hello {}, What can i do for you ?".format(username))
    print(f"Hello {username}, What can i do for you ?")

name_of_function('anuroop')

def name_test(age,username = 'there',user_ethnicity = 'Asian'):

    """
    Docstring explains what the function does
    """
    print("Hello {},{} {}, What can i do for you ?".format(username,user_ethnicity,age))
    print(f"Hello {username} {user_ethnicity} {age}, What can i do for you ?")

name_test(25)
name_test('Dinesh')
name_test('Dinesh','Indian')
name_test(user_ethnicity='Indian')
name_test('Indian')


def square(x):
   a = x*x # a is a local variable
   return a



# a = square(5)
# print("a ",a)
# print("the result is ",square(5))

def custom_number_of_args(*args):
    return sum(args)

# print(custom_number_of_args(1,2,3,4,5,56,7,8,90))


def key_word_args(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

# key_word_args(name = 'anuroop',age='25',city='blr')

# lambda
square = lambda x: x * x
print(square(10))

add = lambda x,y,z: x+y+z
print(add(2,3,5))



#map
numbers = [1,2,3,4,5]
squared = map(square,numbers)
# print(list(squared))
#filter
def is_even(x):
    return x%2==0


numbers = [1,2,3,4,5,6,7,8]
filtered_even = filter(is_even,numbers)
# print(list(filtered_even))

def ln(x):
    return 'Th' in x


# a = ['Anuroop','Abhighna','Gnana SAi','Thirumalesh','Trinetra','Mokshagna']
# filtered_names = filter(ln,a)
# print(list(filtered_names))
#
# a = ['Anuroop','Abhighna','Gnana SAi','Thirumalesh','Trinetra','Mokshagna']
# filtered_names = filter(lambda x:len(x)>8,a)
# print(list(filtered_names))

from functools import reduce

numbers = [1,2,3,4,5]

def add(x,y):
    return x+y

# x=1,y=2 -- add -- x= 3,y=3 --- add --- x =6,y =4 --- add --- x=10,y=5 --- add --- 15

# add(2,3,4)
result = reduce(add,numbers)
print(result)

result_lambda = reduce(lambda x,y:x+y,numbers)
print(result_lambda)

def prod(x,y):
    return x*y

result = reduce(prod,numbers)
print(result)

result = reduce(lambda x,y :x*y,numbers)
print(result)



numbers = [1,2,5,7,3,6]

def max(x,y):
    if x>y:
        return x
    else:
        return y

result = reduce(max,numbers)
print(result)

result_lambda = reduce(lambda x,y : x if x>y else y,numbers)
print(result_lambda)

names = ['Abhighna','Manjula',"Anuroop",'Ganesh','Madhu']

result_lambda = reduce(lambda x,y:x + " " + y,names)
print(result_lambda)


students = [
    {'name':"anu",'marks':90},
    {'name':"abhi",'marks':92},
    {'name':"Manju",'marks':94},
    {'name':"Ganesh",'marks':96},
    {'name':"Madhu",'marks':98}
]














#
# str = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# l = list(str)
# for i in range(4,len(str),4):
#     print(i)
#     l.insert(i,'\n')
# print(l)
# print(''.join(l))


# raw = '7 21'
# raw_1 = raw.split()
# N= int(raw_1[0])
# M= int(raw_1[1])
# for i in range(N//2):
#     print(('.|.'*((2*i)+1)).center(M, '-'))
# print('WELCOME'.center(M,'-'))
# for i in reversed(range(N//2)):
#     print(('.|.'*((2*i)+1)).center(M, '-'))




