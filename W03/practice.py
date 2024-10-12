answer = input('\nHow are you? \n1 - I am fine\n2 - I am not fine\n\n')


if answer.lower() == 'i am fine':
    print('\nWe are happy for you\n')
elif answer.lower() == 'i am not fine':
    print('\nSorry about that\n')
else:
    print('\nI do not have an answer to that\n')