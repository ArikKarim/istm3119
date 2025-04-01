import random

# 3 strings for the 3 outcomes
tie = 'It is a tie'
won = 'Congrats, you won'
lost = 'You lost'

# Choices tuple
choices = ('rock', 'paper', 'scissors', 'lizard', 'spock')

# Outcomes table
rules = (
    (tie, lost, won, won, lost),  # rock
    (won, tie, lost, lost, won),  # paper
    (lost, won, tie, won, lost),  # scissors
    (lost, won, lost, tie, won),  # lizard
    (won, lost, won, lost, tie)   # spock
)

# Ask the user for their choice
user = int(input("Enter your choice: 1 - Rock, 2 - Paper, 3 - Scissors, 4 - Lizard, 5 - Spock: "))
print('You chose', choices[user - 1])

# Get computer's choice
comp = random.randint(1, 5)
print('Computer chose', choices[comp - 1])

# Determine outcome from the game
print(rules[user - 1][comp - 1])
