textbooks = {'Math' : '420', 'Science' : '375', 'Language Arts' : '423', 'Physics' : '381'}
textbooks['Physics'] = '200'
textbooks['Music'] = '350'
textbooks['Social Studies'] = '207'
cost = input("What is the subject you want to find the cost of?")
if cost == "Math":
    print(textbooks['Math'])
elif cost == "Science":
    print(textbooks['Science'])
elif cost == "Language Arts":
    print(textbooks['Language Arts'])
elif cost == "Physics":
    print(textbooks['Physics'])
elif cost == "Music":
    print(textbooks['Music'])
elif cost == "Social Studies":
    print(textbooks['Social Studies'])
else:
    print("Invalid response. Please try again.")

print(textbooks)



list = {'DragonE12' : 'iloveicecream', 'Pumpkinlover' : '452thanks', 'captainbob24' : 'pirates42', 'User249681' : 'passwordhi', 'izzyink' : 'hipeeps57', 'doggytrained' : '100dalmatians', 'Gravitando' : 'Houdini5016', 'Kapebeans' : 'dessertlover90', 'Olympicrunner': 'ivegottalent', 'penguinruler' : 'twoleftfeet'}
username = input("What is your username?")
if username not in list:
    print("Sorry that is not in the database. Please try again.")
elif username in list:
    password = input("What is your password?")
    if password == list[username]:
        print("You are logged in")
    else:
        print("That is not the password. Please try again.")




