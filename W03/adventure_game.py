'''
Author:
Purpose:
'''

# The adventure game starts with an intro
# The intro is below:

# Stretch challenge -> stored all responsed into variables and passed them down into the program:
intro = 'You are an adventurer exploring the dense, misty forests of Eldergrove. Deep in the forest, you come across an ancient stone altar with a glowing amulet resting on top. You’ve heard legends of the Amulet of the Moon, said to grant incredible power, but at a great cost. The moment you approach the altar, the wind shifts, and a deep voice booms: “Choose wisely, for your fate is sealed.”'
# Option 1 details
if_take_1 = 'You grab the amulet. Immediately, the forest grows darker, and you hear howls in the distance. Something is coming. Do you:'
# Option 1.1 details
if_run_1_1 = "You run deeper into the woods, your heart pounding. The howls grow louder, but you find a hidden cave. You crawl inside, and the howling stops. As you explore the cave, you find a map etched into the stone walls. It shows the location of a hidden treasure."
# Option 1.1.1 details
if_follow_map_1_1_1 = 'You decide to follow the map, which leads you to an ancient, overgrown temple. Inside, you find a vast treasure hoard. However, the moment you touch it, the amulet flares with power, binding you to the temple as its eternal guardian. You become a spirit protector of the treasure, trapped for eternity.'
# Option 1.1.2 details
if_ignore_map_1_1_2 = 'You realize that the treasure may be another trap. Instead, you choose to stay hidden in the cave. Days pass, and eventually, you find a way out of the cave, but the amulet begins to drain your life. You escape the cave but live with a cursed life, aging rapidly as the amulet feeds on your soul.'
# Option 1.1.3 details
if_explore_1_1_3 =  'You decide to explore deeper into the cave, ignoring the map. As you venture into the dark, winding tunnels, you come across a glowing portal. Do you:'
# Option 1.1.3.1 details
if_step_in_1_1_3_1 = 'You step through the portal and are transported to another realm, a world of spirits and shadows. Here, the amulet gives you great power, but you are forever bound to this strange, ethereal plane. You become a powerful but isolated figure in a parallel world, unable to return to your own.'
# Option 1.1.3.2 details
if_turn_back_1_1_3_2 = 'You decide not to risk entering the portal and turn back toward the surface. When you emerge from the cave, the howling has stopped, and the forest is calm. However, the amulet’s power still clings to you, and strange occurrences seem to follow you wherever you go. You live a haunted life, constantly aware of the otherworldly forces watching over you.'
# Option 1.2 details
if_confront_1_2 = 'You stand your ground, gripping the amulet tightly. From the shadows, a massive wolf emerges, but instead of attacking, it kneels before you. The amulet has given you control over the forest’s creatures. You realize you now rule the forest.'
# Option 1.2.1 details
if_use_1_2_1 = 'You command the wolves and other beasts to attack nearby villages and expand your power. However, as you conquer more land, you become a tyrant feared by all. Your reign of terror grows, but the amulet slowly corrupts your mind, turning you into a monstrous being.'
# Option 1.2.2 details
if_protect_1_2_2 = 'You decide to use your newfound power to protect the forest from human invaders and poachers. Under your rule, the forest flourishes, and you become a beloved legend known as the Forest King. You live in peace and harmony, guarding the forest until the end of your days.'

# Option 2 details
if_leave_2 = 'You decide not to take the amulet, fearing its curse. As you turn to leave, a mysterious figure appears behind you. “Wise choice,” the figure says, revealing themselves to be an ancient forest guardian. They offer you another path. Do you: '
# Option 2.1 details
if_follow_2_1 = 'You follow the guardian deeper into the woods, where they lead you to a hidden grove. In return for your wisdom, the forest grants you eternal life as its protector.'
# Option 2.1.1 details
if_embrace_2_1_1 = 'You accept your role as the forest’s protector, living for centuries, maintaining peace between humans and nature.'
# Option 2.1.2 details
if_regect_2_1_2 = 'You choose to live a normal life and reject the offer of immortality. The forest grants you the power to communicate with animals, and you live a long, peaceful life, aiding the balance between nature and man. You live out your life as a respected figure, though with some regret of turning down immortality.'
# Option 2.2 details
if_ignore_2_2 = 'You turn away from the figure and leave the forest altogether, deciding that some mysteries are best left alone. As you walk away, the mist lifts, and the forest feels lighter. You return to your normal life, but the memory of the amulet haunts you.'
# Option 2.2.1 details
if_forget_2_2_1 = 'You live your life as normal, but the thought of the amulet never fully leaves your mind. Eventually, your curiosity gets the better of you, and you return to the forest years later, only to find it overrun with dark magic. The forest has fallen to evil forces, and you wonder if your refusal of the amulet was the right choice.'
# Option 2.2.2 details
if_tell_2_2_2 = 'You warn others about the amulet, becoming a famous storyteller, cautioning adventurers about the dangers of Eldergrove. Your story spreads, and many avoid the forest, saving them from a dark fate.'
# Death note terminates the game if user does not input the right option
death_note = '\n\nWRONG CHIOCE! You die the most painful death and are erased from existance\n\n GAME OVER!!!\n\n'

# The game begins here
choice = input(f'\nThere is one rule to this game!\n- Type the exact phrase of chioce (ie: The ones in all CAPS!) or DIE!\n\n{intro}\n\n1 - TAKE THE AMULET\n2 - LEAVE THE AMULET \n\n')

if choice.lower() == 'take the amulet': # if user chooses to take the amulet
    choice = input(f'\n{if_take_1}\n\n1 - RUN DEEPER INTO THE FOREST\n2 - CONFRONT WHATEVER IS COMING\n\n')
    if choice.lower() == 'run deeper into the forest': # if user chooses to run deeper
        choice = input(f'\n{if_run_1_1}\n\nWill you:\n1 - FOLLOW THE MAP\n2 - IGNORE THE MAP AND STAY HIDDEN\n3 - EXPLORE DEEPER INTO THE CAVE\n\n')
        if choice.lower() == 'follow the map': # if user chooses to follow the map
            print(f'\n{if_follow_map_1_1_1}\n\nTHE END\n')
        elif choice.lower() == 'ignore the map and stay hidden': # if user chooses to ignore the map
            print(f'\n{if_ignore_map_1_1_2}\n\nTHE END\n')
        elif choice.lower() == 'explore deeper into the cave': # if user chooses to expore deeper
            # Stretch challenge added one more level to this option
            choice = input(f'\n{if_explore_1_1_3}\n\n1 - STEP THROUGH THE PORTAL\n2 - TURN BACK\n\n')
            if choice.lower() == 'step through the portal': # if user chooses to step through
                print(f'\n{if_step_in_1_1_3_1}\n\nTHE END\n')
            elif choice.lower() == 'turn back': # if user chooses to turn back
                print(f'\n{if_turn_back_1_1_3_2}\n\nTHE END\n')
            else:
                print(death_note)
            # Stretch challenge
        else:
            print(death_note)
    elif choice.lower() == 'confront whatever is coming': # if user chooses to confront
        choice = input(f'\n{if_confront_1_2}\n\nWhat will you use your power for:\n1 - EXPAND YOUR POWER\n2 - PROTECT THE FOREST\n\n')
        if choice.lower() == 'expand your power': # if user chooses to expand power
            print(f'{if_use_1_2_1}\n\nTHE END\n')
        elif choice.lower() == 'protect the forest': # if user chooses to protect the forest
            print(f'{if_protect_1_2_2}\n\nTHE END\n')
        else:
            print(death_note)
    else:
        print(death_note)
elif choice.lower() == 'leave the amulet': # if user chooses to leave amulet
    choice =  input(f'\n{if_leave_2}\n\n1 - FOLLOW THE GUARDIAN\n2 - IGNORE THE GUARDIAN\n\n')
    if choice.lower() == 'follow the guardian': # if user chooses to follow the guardian
        choice = input(f'\n{if_follow_2_1}\n\nWill you:\n1 - EMBRACE IT\n2 - REJECT IT\n\n')
        if choice.lower() == 'embrace it': # if user chooses to embrace it
            print(f'\n{if_embrace_2_1_1}\n\nTHE END\n')
        elif choice.lower() == 'reject it': # if user chooses to reject it
            print(f'\n{if_regect_2_1_2}\n\nTHE END\n')
        else:
            print(death_note)
    elif choice.lower() == 'ignore the guardian': # if user chooses to ignore
        choice = input(f'\n{if_ignore_2_2}\n\nDo you\n1 - TRY TO FORGET\n2 - TELL OTHERS\n\n')
        if choice.lower() == 'try to forget': # if user chooses to try to forget
            print(f'\n{if_forget_2_2_1}\n\nTHE END\n')
        elif choice.lower() == 'tell others': # if user chooses to tell others
            print(f'\n{if_tell_2_2_2}\n\nTHE END\n')
        else:
            print(death_note)
    else:
        print(death_note)
else:
    print(death_note)

 