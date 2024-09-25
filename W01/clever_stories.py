# Input the words here for the story
print('Please enter the following: \n')

adjective = input('adjective: ')
animal = input('animal: ')
verb = input('verb: ')
exclamation = input('exclamation: ')
verb1 = input('verb: ')
verb2 = input('verb: ')
# Creativity starts here
noun = input('noun: ')
verb_past = input('verb (past tense): ')
verb_past1 = input('another verb (past tense): ')
verb_cont = input('verb (continious tense): ')
verb_past2 = input('verb (past tense): ')
nickname = input('nickname: ')
verb_past3 = input('verb (past tense): ')

article = 'a'

if noun[0].lower() == 'a' or noun[0].lower() == 'e' or noun[0].lower() == 'i' or noun[0].lower() == 'o' or noun[0].lower() == 'u':
    article = 'an'
else :
    article = 'a'
# Creativity ends here

# This section prints the story after the inputs
print('\nYour story is:\n')
print(f'The other day, I was really in trouble. It all started when I saw a very\n{adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all\nI could think to do was to {verb1.lower()} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb2.lower()}\nright in front of my family.')
# Creativity printing starts here
print(f'My family was more than a little shocked, but I was just {verb_past.lower()}\nthat the {animal.lower()} had {verb_past1.lower()}. Little did I know, the {animal.lower()} was actually {article.lower()} {noun.lower()}\nand my {verb_cont.lower()} had simply {verb_past2.lower()} it.\nFrom then on, I was known as the "{nickname.title()}," and my family and\nfriends never {verb_past3.lower()} at me the same way again.\n')
# Creativity printing ends here
