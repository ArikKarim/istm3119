import math

def float_input(prompt):
  while True:
    try:
      x = float(input(prompt))
      # if we get to this line, then we are good
      if x <= 0:
        print('Cannot enter negative number or zero - try again.')
      else:
        return x
  except ValueError:
    print('Invalid value for float - try again.')

# ask the user for the radius
radius = float_input('Enter the radius of the cylinder: ')
print('The radius is', radius)

# ask the user for the height
height = float_input('Enter the height of the cylinder: ')
print('The height is', height)

# do the math calc to calc the sa of a cylinder
sa = ((2 * math.pi * radius * height) + (2 * math.pi * (radius ** 2)))

# print the output to the user
print('The surface area is', sa) # raw form
print('The surface area is {:.2f}'.format(sa))
