import random



# 3 strings for the 3 outcomes
tie = 'It is a tie'
won = 'Congrats, you won'
lost = 'You lost'

# tuples that are helpful for our code
choices = ('rock, paper, scissors')

rules = ((tie, lost, won),
        (won, tie, lost),
        (lost, won, tie))

# ask the user for their choice but instead of using an if statement to print the word
print('You chose', choices[user - 1])

# for the comp choicem, do the same thing

# determine the outcome from the game 
print()
