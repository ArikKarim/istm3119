# validation function
def float_input(question, low, high):
  while True:
    try:
      x = float(input(question))
      if x < low or x > high:
        print('Cannot enter num <', low, 'or >', high, '- try again.')
      else:
        return x
    except ValueError:
      print('Invalid value for float - try again.')

# ask user for input and provide output
while True:
  score = float_input('Enter a score: ', 0, 100)
  print('You entered a score of', score)
  if score >= 90:
    letter_grade = 'A'
  elif score >= 80:
    letter_grade = 'B'
  elif score >= 70:
    letter_grade = 'C'
  elif score >= 60:
    letter_grade = 'D'
  else:
    letter_grade = 'F'
  print('Your letter grade is', letter_grade)

  # loop 
  again = input('Do you wish to loop again? Y/N: ').upper()
  if again == 'N':
    break  
