#File: Week 05 prove Assignment
#Purpose: Milestone Activity
#Author: Emediong Edet
print("A text based adventure game!") 
print()
print("You are walking through a dark forest and find two items: a MATCH and FLASHLIGHT.")
scenario_1 = input("Which one do you want to pick up?")
match = "match"
flashlight = "flashlight"
if scenario_1.lower() == match:
    response = "You pick up the match and strike it, and for an instant, the forest around you is illuminaed. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?"
else:
    response = "That's a different choice from the above."
    print(response)
if scenario_1.lower() == flashlight:
    response  = "You pick the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side.  Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise."
else:
    response = "The choice is not among the listed."
    print(response)
scenario_2 = input("Do you want to RUN or HIDE behind the tree?")
run = "run"
hide = "hide"
if scenario_2.lower() == run:
    response = "You run and get lucky to escape."
else:
    response = "None of the above"
    print(response)

if scenario_2.lower() == hide:
    response = "You hide and get caught."
else:
    response = "That's a different input."
    print(response)
scenario_3 = input("Do you want to FOLLOW the path or LOOK in the trees for the thing that made the niose?")
follow = "follow"
look = "look"
if scenario_3.lower() == follow:
    response = "You follow and discover a land full of treasures."
else:
    response = "Check the next version of the story."
    print(response)
if scenario_3.lower() == look:
    response = "You look for the thing that made the noise, and you collide with a fiercely lion."
    print(response)
else:
    response = "None of the above."
    print(response)