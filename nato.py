nato_map = {
    'a': 'alpha',
    'b': 'bravo',
    'c': 'charlie', 
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliet',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'x-ray',
    'y': 'yankee',
    'z': 'zulu'
}

user_codes = input("Type in the letters you wish to speak").lower()

# user codes 'abc9'

sentences = ""
for c in user_codes:
  word = nato_map.get(c)
  if word is None:
      word = c
  sentence = sentence + word + ' '

print('Then you should speak:', sentence)
