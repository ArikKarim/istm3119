import math
import random
import tools

def roll_many_and_keep_count():
    
    # create a list of 6 int, set each to 0
    counters = [0, 0, 0, 0, 0, 0]
    
    for x in range(6000):
        result = random.randint(1,6)
        
    # add one to the appropriate counter in our list
    counters[result - 1] += 1

    # print the report
    for index in range(6):
      # print the two messages
      print('Side', index + 1, 'was rolled', counters[index], 'times')
      print('Side', index + 1, 'was rolled', counters[index] / 6000, '% of the time')

    print()
    print('Here is a report of how many times each side was rolled')

def main():
    roll_many_and_keep_count()

main()
