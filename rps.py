# hints / pseudo code

import random

# 3 strings for the 3 outcomes
tie = 'It is a tie'
won = 'Congrats, you won'
lost = 'You lost'

# ask the user for their choice
prompt = 'Enter 1 for Rock, 2 for Paper, or 3 for Scissors: '
# call the ask_user_for_int(prompt, 1, 3)

# if statement to decide what word to print
# based on what the user chose
if user == 1:
  print('You chose rock')
elif user == 2: 
  print('You chose paper')
else:
  print('You chose scissors')

# 'ask' the computer what they choose = randint
comp = random.randint(1, 3)
