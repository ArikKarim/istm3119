# lists
var1 = list()
var1.append('June')
var1.append('Zahir')
var1.append('Ann')
print(var1[0])

print(len(var1))

print(var1.index('June'))

print('June' in var1)

print('Joe' in var1)

var1.sort()
print(var1[0])

for x in var1:
  print(x)

print(min(var1))

print(max(var1))

var1.reverse()
print(var1[0])

var1.append('Ann')
print(var1.count('Ann'))
