import random
from datetime import datetime

# die1 = random.randint(1,6)
# die2 = random.randint(1,6)
# die3 = random.randint(1,6)
# die4 = random.randint(1,6)
# die5 = random.randint(1,6)
# die6 = random.randint(1,6)
#
# print(die1)
# print(die2)
# print(die3)
# print(die4)
# print(die5)
# print(die6)
#
# print('-'*40)
#
# total = die1 + die2 + die3 + die4 + die5 + die6
#
# print(total)

#---------------------------------------------------------------

# def random_dice():
#     random_number = random.randint(1, 6)
#     print(random_number)
#
# random_dice()

#----------------------------------------------------------------

# for x in range(10):
#     random_number = random.randint(1, 6)
#
#     print(random_number)

#--------------------------------------------------------------------

# class Parent:
#
#     def __init__(self):
#         self.random_number1 = random.randint(1, 6)
#         self.random_number2 = random.randint(1, 6)
#         self.random_number3 = random.randint(1, 6)
#         self.random_number4 = random.randint(1, 6)
#         self.random_number5 = random.randint(1, 6)
#         self.random_number6 = random.randint(1, 6)
#
#     def Function1(self):
#         print("Your First random number: ", self.random_number1)
#         print("Your Second random number: ", self.random_number2)
#         print("Your Third random number: ", self.random_number3)
#         return
#
#
# class Child(Parent):
#
#     def Function2(self):
#         self.Function1()
#         print("Your Fourth random number: ", self.random_number4)
#         print("Your Firth random number: ", self.random_number5)
#         print("Your Sixth random number: ", self.random_number6)
#         number = self.random_number1 + \
#                  self.random_number2 + \
#                  self.random_number3 + \
#                  self.random_number4 + \
#                  self.random_number5 + \
#                  self.random_number6
#         print(number)
#         return
#
#
#
#
# Object1 = Parent()
# Object2 = Child()
# Object2.Function2()
#
#
# today = datetime.date.today()
# future = datetime.date(2021, 9, 20)
# diff = future - today
# print(diff.days)



#------------------------------------------------------------------


def random_number(num):
    list_random = list()
    while num < 6:
        list_random.append(random.randint(1, 6))
        num += 1
    return list_random

def sum_up(list_sum):
    total = 0
    for item in list_sum:
        total += item
        #total = toal + item Another way to do line 103
    return total

def get_name():
    name = input("Enter your first name: ")
    return name

def compare_scores(score1, score2):
    if score1 > score2:
        print("You win")
    else:
        print("The other player wins")

def time_stamp():
    game_start = datetime.today().strftime('%b-%d-%Y')
    print(game_start)
    return game_start

mydict = dict()


for x in range(2):
    name = get_name()
    mydict[name] = sum_up(random_number(0))


values = mydict.values()

values_list = list(values)

add_list = sum(values_list)


time_stamp()


print(mydict)
print(values_list)
print(add_list)












