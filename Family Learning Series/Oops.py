"""
Animal - eats, sleeps, hunt, drink
Human  - eats ,sleeps, work, drink
"""
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        return f'{self.name} is eating'

    def sleep(self):
        return 'i am sleeping'

    def hunt(self):
        return ' i am on a hunt'

    def drink(self):
        return ' i am drinking'
class Human(Animal):

    def work(self):
        return f'{self.name} is working'

class birds(Human):
    def fly(self):
        return ' i am flying'

a = Human('Anuroop')
print(a.eat())

b = birds('parrot')
print(b.work())
print(b.drink())


















# class Car:
#     def __init__(self, max_speed):
#         self.__max_speed = max_speed # private variable -- this varaible cannot be accessed outside the class nor be overrided
#         self.max_vel = max_speed
#
#     def drive(self):
#         return f'Driving at {self.__max_speed} km/h'
#
#     def set_max_speed(self,speed):
#         if speed > 0:
#             self.__max_speed = speed
#
# BMW_ = Car(200)
# print(BMW_.__max_speed)

# class Bank:
#     def __init__(self, balance, account):
#         self.__balance = balance
#         self.__account = account
#
#     def get_balance(self):
#         return self.__balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return f'deposited {amount} , current balance {self.__balance}'
#
#     def withdraw(self,amount):
#         if amount > 0  and amount <= self.__balance and amount <= 10000:
#             self.__balance -= amount
#             return f'withdrawl of {amount} , current balance {self.__balance}'
#         else:
#             return 'you cannot withdraw above 10,000 at once Max denomination available is 500, max notes disbursed is 20 notes'
#
# new_account = Bank(30000,12345667)
# # print(new_account.deposit(5000))
# # print(new_account.withdraw(10000))
# # print(new_account.get_balance())
#
# # print(new_account.__account)













# print(BMW_.max_vel)
# print(BMW_.drive())
# BMW_.set_max_speed(240)
# print(BMW_.drive())













#
#
#
#
#
#
# class person:
#     msg = 'the name and age of the person are : '
#     def __init__(self, name, age):
#         self.name = name
#         self.age  = age
#
#     def get_age(self):
#         return f'the person age is {self.age}'
#
#     def get_name(self):
#         return f'the person name is {self.name}'
#
#     def get_both(self):
#         return self.msg+f'{self.name, self.age}'
#
# person_class = person('Anuroop', 25)
# print(person_class.get_age())
# print(person_class.get_name())
# print(person_class.get_both())
# print(person_class.name, person_class.age)



#
#
#
#
#
#
#
#
#
#
#
#
# class arithmetic:
#     msg = 'addition of two numbers'
#
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return f'{self.msg}:{self.a}, {self.b} = {self.a + self.b}'
#
#     def mul(self):
#         return self.a*self.b
#
#     def sub(self):
#         return self.a-self.b
#
#
# class logical:
#     def greater_than(self,a,b):
#         return a if a>b else b
#
#     def add(self,a,b):
#         return b-a
#
#
#
# a = arithmetic(2,3)
# print(a.add())
# print(a.mul())
# print(a.sub())
# b = logical()
# print(b.add(12,6))
