# step 1: open the file
file_ptr = open('coffee.csv', 'r')

# step 2:
headers = file_ptr.readline()

for line in file_ptr:
  line = line.strip()
  fields = line.split(',')
  print(fields[0], 'oz drink of', fields[1], 'is $', fields[2])

#step 3: close the file
file_ptr.close()
