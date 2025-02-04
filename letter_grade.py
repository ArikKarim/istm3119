# validation function
def float_input(question):
  while True:
    try:
      x = float(input(question))
      if x < 0:
        print('Cannot enter negative number - try again.')
      else:
        return x
    except ValueError:
      print('Invalid value for float - try again.')

# call the validation function
score = float_input('Enter a score: ')
print('You entered a score of', score)

# determine the letter grade - if statement
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

# print the letter grade
print('Your letter grade is', letter_grade)

