import random
import datetime


#  This function generates six random numbers
def random_number(num):
    list_random = list()
    while num < 6:
        list_random.append(random.randint(1, 6))
        num += 1

    print(list_random)
    return list_random

#  This function adds the six numbers together
def sum_up(list_sum):
    total = 0
    for item in list_sum:
        total += item
        #  total = total + item Another way to do line 103
    return total

# This function takes the player's name
def get_name():
    name = input("Enter your name: ")
    return name

# This compares the scores to tell who won
def compare_scores(p1, p2):
    if player1 > player2:
        print("Player 1 wins")
    else:
        print("Player 2 wins")

# This function is a countdown til Easter
def time_stamp():
    today = datetime.date.today()
    future = datetime.date(2021, 4, 4)
    b_day = datetime.date(2021, 4, 16)
    birth = b_day - today
    diff = future - today
    print(diff.days, "days til Easter! Happy Easter and", birth.days, "til my Birthday!", "Happy Coding")
    return diff.days

# This is the dictionary where the "name" and sum of the random numbers are stored
mydict = dict()


# This For loop puts the "name" and total of the six random numbers in a dictionary
for x in range(2):
    name = get_name()
    mydict[name] = sum_up(random_number(0))

# This pulls the values of dictionary
values = mydict.values()

# This pulls the values of mydict.values into a list
values_list = list(values)

# This stores the first player's value in
player1 = values_list[0]

player2 = values_list[1]


print()  # added a blank line to more some separation
print(mydict)
compare_scores(player1, player2)
time_stamp()










