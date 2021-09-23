#This is a program that gives the user a limited breakfast selection.

delivMes='It will be delivered shortly. Enjoy!'
#delivMes = delivery message. Will be used repeatedly, therefore it was stored in a variable.

rejectMes='Your choice is not available at the moment. If you want a special order, please visit the counter.'
#rejectMes = rejection message, when the input is not one of the presented choices. Will be used repeatedly, therefore it was stored in a variable.


print("> Please select your breakfast choice!")

mMenu=["Bacon and Eggs", "Toast/Pandesal", "Rice", "Pancakes"]
#mMenu= main menu

print("1. Bacon and Eggs")
print("2. Toast/Pandesal")
print("3. Rice")
print("4. Pancakes")
primsel=int(input("> Your choice:  "))
#primsel = primary selection

if (primsel==1):
    print("You've selected Bacon and Eggs! {}".format(delivMes))
    
elif (primsel==2):
    filling=["Hotdog", "Sunny Side Egg", "Sandwich Spread", "Cheese"]
    print("1. Hotdog (Hotdog Bun)")
    print("2. Sunny Side Egg")
    print("3. Sandwhich Spread")
    print("4. Cheese")
    subsel1=int(input("> Please select filling:  "))
    #subsel = sub selection 1
    if (subsel1==1):
        print("You've selected {}, with {} filling. {}".format(mMenu[1],filling[0],delivMes))
    elif (subsel1==2):
        print("You've selected {}, with {} filling. {}".format(mMenu[1],filling[1],delivMes))
    elif (subsel1==3):
        print("You've selected {}, with {} filling. {}".format(mMenu[1],filling[2],delivMes))
    elif (subsel1==4):
        print("You've selected {}, with {} filling. {}".format(mMenu[1],filling[3],delivMes))
    else:
        print(rejectMes)