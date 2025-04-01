import json

# Load the JSON file
with open('nato.json', 'r') as file_ptr:
    data = json.load(file_ptr)
    nato_map = data["nato_map"] 

user_codes = input("Type in the code you wish to speak: ").lower()

sentence = ""

for c in user_codes:
    word = nato_map.get(c, c) 
    sentence += word + " "

print("Then you should speak:", sentence.strip())  
