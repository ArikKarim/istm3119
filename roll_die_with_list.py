import random

def roll_many_and_keep_count():
    # create a list of 6 int, set each to 0
    counters = [0, 0, 0, 0, 0, 0]

    # roll the die 6000 times and count the occurrences
    for x in range(6000):
        result = random.randint(1, 6)
        # Add one to the appropriate counter in our list
        counters[result - 1] += 1

    print('Here is a report of how many times each side was rolled')

    # use a for loop to print from the list
    # loop 6 times (for each die side)
    for index in range(6):
        print('Side', index + 1, 'was rolled', counters[index], 'times')
        print('Side', index + 1, 'was rolled', counters[index] / 6000 * 100, '% of the time')

    print()

def main():
    roll_many_and_keep_count()

main()
