
print("|| Welcome to Treasure Island.||")
print("Your mission is to find the treasure.")
choice1 = input('You\'re about to enter a dense forest. There are 3 paths in front of you. \n'
                'Which one do you want to go to? "Straight", "Left" or "Right"\n').lower()
if choice1 == "right":
    choice2 = input('Great! you are on the right path.'
                    'Now, there\'s a river in front of you. \n'
                    'How do you want to cross that? Type "Swim" to swim through or type'
                    '"Boat" to wait for the boat and then cross.\n').lower()
    if choice2 == "swim":
        choice3 = input('Nice! you are doing really well.Now you gotta go to another cliff.\n'
                        'There\'s a bridge already and a brand new helicopter parked.\n'
                        'What would you choose to reach the cliff on the other side? \n'
                        'Type "Bridge" to use the bridge or type "Helicopter" to use the helicopter.\n').lower()
        if choice3 == "helicopter":
            choice4 = input('Wonderful! you\'re almost there. \nNow, you\'ve got two caves in front of you.\n'
                            'The one looks very old and abandoned and the other seems new. Which one would you enter? '
                            '\nType "Old" for the old one and "New" for the new one.\n').lower()
            if choice4 == "old":
                print("#######---Congratulations.. You won!! you've found the treasure.#######")
            elif choice4 == "new":
                print("The beast in the forest got bored with old cave and recently shifted to the new one! XD Game Over!")
            else:
                print("wrong input. try again.")
        elif choice3 == "bridge":
            print("uggghh..wrong choice. The bridge has collapsed being too old")

    if choice2 == "boat":
        print("You got attacked by a bear while waiting for the boat. Game Over!")
    else:
        print("Wrong input")
elif choice1 == "left":
    print("There was a Lion hiding & waiting for it's christmas meal. Game Over!")
else:
    print("You have become a delicious meal to a hungry Python. XD Game Over!")
