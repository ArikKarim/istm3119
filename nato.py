open('nato.json', file_mode())

user_codes = input("Type in the code you wish to speak: ").lower()

# user codes 'abc9'

sentences = ""
for c in user_codes:
  word = nato_map.get(c)
  if word is None:
      word = c
  sentence = sentence + word + ' '

print('Then you should speak:', sentence)
