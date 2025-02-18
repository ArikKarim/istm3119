# tools module for roll_die.py

import math
import random

def float_validate_input(prompt, low, high):
   while True:
       user_input = input(prompt)
       try:
           value = float(user_input)
           if value < low or value > high:
               print("Error. Number is outside the given range (",low, " - ",high, "). Please try again")
           else:
               return value
       except ValueError:
           print('Error. Please enter a number')

def int_validate_input(prompt, low, high):
   while True:
       unput = input(prompt)
       try:
           value = int(unput)
           if value <= low and value >= high:
               print("Error. Number is outside the given range (",low, " - ",high, "). Please try again")
           else:
               return value
       except ValueError:
           print('Error. Please enter a number')
