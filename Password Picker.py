import random
import string

adjectives = ['boiling', 'fluffy', 'sharp', 'freezing', 'shaggy', 'melted', 'silky', 'flaky', 'painful', 'greasy', 'slippery', 'prickly', 'dusty', 'hot', 'loose', 'encrusted', 'rough', 'tender']

nouns = ['woman', 'city', 'dog', 'shoe', 'man', 'mountain', 'ocean', 'state', 'country', 'building', 'cat', 'website', 'table','cloth', 'eye', 'glasses', 'sock', 'baby', 'hero']

print('Welcome to password picker!')

while True:
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print('Your new password is: %s' % password)

    response = input ("Would you like another password? Type y or n: ")

    if response == 'n':
        break
