# requires tools.py module for code to function

import random
import math
import tools

def roll_many():
    num_times = tools.int_validate_input('How many times do you want to roll the die?', 1, 20)

    for x in range(num_times):
        result = random.randint(1,6)
        print('Roll #', x + 1, 'You rolled a ', result)

def roll_many_and_keep_count():
  #  print('Hey I am in the roll_many_and etc')
    side1 = 0; side2 = 0; side3 = 0; side4 = 0; side5 = 0; side6 = 0
    for x in range(6000):
        result = random.randint(1,6)
        if result == 1:
            side1 += 1
        elif result == 2:
            side2 +=1
        elif result == 3:
            side3 +=1
        elif result == 4:
            side4 += 1
        elif result == 5:
            side5 += 1
        elif result == 6:
            side6 += 1
    print('Side 1 was rolled', side1, 'times (', (side1/6000)*100,'% of the time)')
    print('Side 2 was rolled', side2, 'times (', (side2/6000)*100,'% of the time)')
    print('Side 3 was rolled', side3, 'times (', (side3/6000)*100,'% of the time)')
    print('Side 4 was rolled', side4, 'times (', (side4/6000)*100,'% of the time)')
    print('Side 5 was rolled', side5, 'times (', (side5/6000)*100,'% of the time)')
    print('Side 6 was rolled', side6, 'times (', (side6/6000)*100,'% of the time)')

def main():
    roll_many()
    roll_many_and_keep_count()

main()
