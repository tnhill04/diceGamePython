import random
from datetime import datetime

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
        print(list_random)
    return list_random

def sum_up(list_sum):
    total = 0
    for item in list_sum:
        total += item
        #total = toal + item Another way to do line 103
    return total

def get_name():
    name = input("Enter your name: ")
    return name

def compare_scores(p1, p2):
    if player1 > player2:
        print("Player 1 wins")
    else:
        print("Player 2 wins")

def time_stamp():
    today = datetime.date.today()
    future = datetime.date(2021, 4, 4)
    diff = future - today
    print(diff.days)
    # return diff.days

    # game_start = datetime.today().strftime('%b-%d-%Y')
    # print(game_start)
    # return game_start


mydict = dict()


for x in range(2):
    name = get_name()
    mydict[name] = sum_up(random_number(0))


values = mydict.values()

values_list = list(values)


player1 = values_list[0]

player2 = values_list[1]



print(mydict)
print(values_list)
compare_scores(player1, player2)
time_stamp()










