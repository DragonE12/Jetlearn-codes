cars = {'Honda' : 'Civic', 'Toyota' : 'Camry', 'Nissan' : 'Leaf', 'Hyundai' : 'Ioniq', 'Chevorlet' : 'Corvette'}
print(cars['Honda'])
cars['Mercedez'] = 'Benz'
print(cars['Mercedez'])
print(cars.keys())
print(cars.values())
print(len(cars))
print('Mercedez' in cars)
del cars['Honda']
print(cars)
cars['Mercedez'] = 'Audi'
print(cars)
cars1 = []
for car in cars:
    cars1.append(car)
cars1.sort()
print(cars1)


game = {'Hockey' : 'Hockey is a fantastic sport to play and watch on the ice', 'Tennis' : 'Tennis is an amazing sport to play with the suspenseful action on the different types of courts', 'Soccer' : 'Soccer is a worldwide sport that everyone loves to watch on the field', 'Baseball' : 'Baseball is a exciting sport in the US that will keep fans intrigued all the time'}
game['Volleyball'] = 'Volleyball is a great sport to see the exceptionally good playing!'
game['Cricket'] = 'Cricket is a sport with eleven members.'
game['Cricket'] = 'Cricket is a sport with a flat wooden bat.'



choice = input("What sport would you like to research about?")

if choice == 'Hockey':
    print(game['Hockey'])
elif choice == 'Tennis':
    print(game['Tennis'])
elif choice == 'Soccer':
    print(game['Soccer'])
elif choice == 'Baseball':
    print(game['Baseball'])
elif choice == 'Volleyball':
    print(game['Volleyball'])
elif choice == 'Cricket':
    print(game ['Cricket'])
else:
    print("That is not a valid answer. Please try again.")



import random


classroom = {'Ethan ' : {
'age' : 12,
'marks' : [20,35,67,18,92]
}, 'Bhavana' : {
'age' : 32,
'marks' : [37,59,28,90,86]
}}
for student in classroom:
    random.shuffle(classroom[student]['marks'])

print(classroom)


string = input("Type a sentence:")
character_count = {}

for letters in string:
    if letters in character_count:
        character_count[letters] += 1
    else:
        character_count[letters] = 1

for character,count in character_count.items():
    print(character,count)    



string = input("Type a sentence:")
if_pangram = {}

for letters in string:
    if letters in if_pangram:
        if_pangram[letters] += 1
    else:
        if_pangram[letters] = 1

print(if_pangram)
if len(if_pangram) == 27:
    print("It is a pangram")
else:
    print("it is not a pangram")
    print(len(if_pangram)) 
