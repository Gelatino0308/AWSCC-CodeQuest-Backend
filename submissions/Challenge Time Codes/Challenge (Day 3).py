def ending (num):
    if num == 0:
        return print("=== GAME OVER X< ===")
    else:
        return print("=== YOU WIN!!! ===")

print("> You need to venture through the dangerous woods towards the city in the middle of the night to buy medicine for your sick grandma.\n")
print("> What instrument will you bring with you? [Enter 1 or 2]")
print("1 - Gas Lamp")
print("2 - Torch")
light = int(input(">> "))

print("\n> You see a beautiful girl running towards you in the woods on your way back.")
print("> When she saw you, she asked if you can help her hide as she was being chased by dangerous people.")
print("> A few men with torches are already approaching your way.\n")

print("What will you do? [Enter 1 or 2]")
print("1 - Help her hide")
print("2 - Wait for the men to arrive and ask what is their business with her")
hide = int(input(">> "))

if hide == 1:
    print("\n> You managed to hide her in a pit and the men went past you two.")
    print("> However, she suddenly tried to attack you out of nowhere. Turns out, she's the village's vampire.\n")
    
    print("You're tired from dodging her. What will you do now? [Enter 1 or 2]")
    print(f"1 - Throw the instrument you brought to her")
    print("2 - Run away")
    fight = int(input(">> "))

    if fight == 1:
        if (light == 1):
            print("\n> Since you threw a gas lamp, it didn't affect the vampire. You tried to run but she catches and bit you!")
            ending(0)
        else:
            print("\n> Throwing the torch set her on fire. She eventually burned away and you're safe!")
            ending(1)
    else:
        print("\n> You run away but she managed to catch and bit you!")
        ending(0)
else:
    print("\n> The villagers told you she's a vampire, and now they also suspect that she already bit you.")
    print("> They don't believe your denial, so they eventually burned both of you with their torches!")
    ending(0)




