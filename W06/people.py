# Declear list
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
name = ''
age = None
youngest_name = ''
youngest_age = None

for person in people:
    print(person)
    person = person.split()
    name = person[0]
    age = int(person[1])
    print(f'Name: {name}\nAge: {age}\n')

    if youngest_age == None or youngest_age > age:
        youngest_age = age
        youngest_name = name

print(f'The youngest is {youngest_name}. He is {youngest_age} years old\n')
