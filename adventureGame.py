# adventure game exploring som logic operators

print("Welcome to Balivanich Community Playpark")
print("You go on an evening stroll by the dunes")
print("You can pick one item to take with you")
print("map(m), torch(t), food(f), rope(r), or a stick(s): ")
item = input("what will you choose? ")
print("You hear a humming sound.")
choice1 = input("Do you follow the sound? Enter y or n: ")
if choice1 == "y":
    print("You keep moving towards the sound")
    direction  = input("which direction do you go? north, south, east, west: ")
    if direction == 'north':
        print("You reach and abandoned boat")
        if item == 'm':
            print("you use the map and find your way back to the swings")
            print("Congratulations! You won the game")
        else:
            print("If you had a map, you could find your way back to the swings from here")
            print("You are still lost, you lost the game")
elif direction == 'south':
    print("You reach a bog with a sheep stuck in it")
    if item == 'r' or item == 's':
        print( "you choose an item that can help here")
        print("you help the sheep out of the bog and it guides you back to the swings")
        print("Congratulations you won the game")
    else:
        print ("If you had a poe or a stick, you could help the sheep")
        print("you are still lost. You lost the game")

else:
    print("Good idea, you're not taking risks")

    action = input("Do you start running (r), or stop to make a call (c)?: ")
    while action == 'c':
        print("The call does not go through")
        action = input("Do you want to run (r), or try calling again (c)?: ")
    print("you are running fast. the sound gets really loud")
