# Task 1:
place  = input("Choose a place: forest or a cave? ")

if place == "forest":
    action = input("climb a tree of cross a river? ")
    if action == "climb a tree":
        print("You found a birds nest!")
    elif action == "cross a river":
        print ("You found a boat!")
elif place == "cave":
    print("you find a hidden treasure!")

# Task 2:
place = input("choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("you found a birds nest!")
    elif action == "cross a river":
        print("you found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("With the torch, you find acient cravings on the wall!")
    elif action == "proceed in the dark":
        print("In the darkness you stumble upon a hidden treasure!")

# Task 3:
if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("you found a birds nest!")
    elif action == "cross a river":
        print("you found a boat!")
    else:
        print("Invalid choice. Please choose a valid action next time.")
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("With the torch, you find acient cravings on the wall!")
    elif action == "proceed in the dark":
        print("In the darkness you stumble upon a hidden treasure!")
    else:
        print("Invalid choice. Please choose a valid option next time.")
        pass
else:
    print("Invalid choice. Please choose either 'forest' or 'cave'.")
    pass

