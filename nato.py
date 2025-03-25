nato_map # copied over

user_codes = input("Type in the letters you wish to speak").lower

# user codes 'abc9'

sentences = ""

for c in user_codes:
  word = nato_map.get(c)
  sentence = sentence + word + ""
