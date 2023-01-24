#File: Week 05/06 Prove Assignment.py
#Purpose: Write a text based adventure Game
#Author: Emediong Edet



first = "match", "flashlight", "tent"
run_hide = "run", "hide"
scream_pray ="scream", "pray"
jump_crawl ="jump", "crawl"
follow_look = "follow", "look"
help_ignore = "help", "ignore"
save_kill = "save", "kill"
enter_passby = "enter", "passby"
water_wine = "water", "wine"
negotiate_fight = "negotiate", "fight"


print("Level 1")
print("Please answer the following questions!")
print("You are walking through a dark forest and find two items: a MATCH, FLASHLIGHT and a TENT.")
first = input("Which one do you want to pick up? ")

if (first.lower() == "match"):
    print("You pick up the match and strike it, and for an instant,"
    "the forest around you is illuminated. You see a large grizzly bear, and then the match "
    "burns out.")

    run_hide = input("Do you want to RUN, or HIDE behind a tree?: ")
    if (run_hide.lower() == "run"):
        print("You run and then all of a sudden you are trapped in a glass box with no means of escape.")
        
        scream_pray = input("Do you SCREAM or PRAY?: ")
        if (scream_pray.lower() == "scream"):
            print("You scream and keep screaming and there's no help.")

        elif (scream_pray.lower() == "pray"):
            print("You pray and the glass gets broken and you are free.")
        else:
            print("invalid input \nPlease try again!!!")
    
    elif (run_hide.lower() == "hide"):
        print("You hide and a bunch of bees apears with a pipe in front of you having a tunnel.")
        jump_crawl = input("Do you JUMP over the pipe or CRAWL through the tunnel?: ")

        if (jump_crawl.lower() == "jump"):
            print("You jump over the pipe and get landed in a valley.")
        elif (jump_crawl.lower() == "crawl"):
            print("You crawl through the tunnel, and it takes you to yoour dream country.")
        else:
            print("invalid input \nPlease try again!!!")
            
    else:
        print("invalid input \nPlease try again!!!")
       

elif (first.lower() == "flashlight"):
    print("You turn on the flashlight, and the path is lit up, but also you thought you"
    "heard some noises in the trees.")
    follow_look = input("Do you FOLLOW the path, or LOOK into the trees? ")
    
    if (follow_look.lower() == "follow"):
        print("You follow the path and then find a kid in need of help.")
        help_ignore = input("Do you HELP the kid or IGNORE?: ")
        
        if (help_ignore.lower() == "help"):
            print("You help the kid and get gifts from the parents.")

        elif (help_ignore.lower() == "ignore"):
            print("You ignore the kid and get killed by a deadly dinosuar.")

        else:
            print("invalid input \nPlease try again!!!")

    elif (follow_look.lower() == "look"):
        print("You look into the trees and find a fortune elf held in a trap. ")
        save_kill = input("Do you SAVE the elf or KILL it?: ")

        if (save_kill.lower() == "save"):
            print("You get all of lives fortunes.")
        
        elif (save_kill.lower() == "kill"):
            print("You kill the elf and then get attacked by other large number of elfs and get killed")
        else:
            print("invalid input \nPlease try again!!!")
            
    else:
        print("invalid input \nPlease try again!!!")
        

elif (first.lower() == "tent"):
    print("You approach the tent.")
    enter_passby =  input("Do you ENTER tent or PASSBY it?: ")

    if (enter_passby.lower() == "enter"):
        print("You enter the tent and find containers with WATER and WINE")
        water_wine = input("Do you drink the WATER or WINE?")

        if(water_wine.lower() == "water"):
            print("Drink water and get hydrated")
        
        elif(water_wine.lower() == "wine"):
            print("You drink the wine and get drunk")

    elif(enter_passby.lower() == "passby"):
        print("You passby and get an encounter with cannibals")
        negotiate_fight = input("Do you NEGOTIATE or FIGHT? ")

        if (negotiate_fight.lower() == "negotiate"):
            print("They get a bit educated and allow you spend the night")
        elif(negotiate_fight.lower() == "fight"):
            print("You got beaten and used for dinner")
        else:
            print("invalid input \nPlease try again!!!")
    
    else:
        print("invalid input \nPlease try again!!!")
         

else:
    print("invalid input \nPlease try again!!!")
    

second = "car", "motorbike", "skateboard"
left_right = "left", "right"
run_stop = "run", "stop"
ride_get_down  = "ride", "getdown"
go_back = "continue", "go back"
join_ignore = "join", "ignore"
compete_watch = "compete", "watch"
time_money = "time", "money"
attend_skill = "college", "skill"
rent_spend = "rent", "spend"

print("Level 1 completed!")
print("Horray!!!")
print()
print("Level 2")
print("Please enter the following information")
print("You are at a point of making a decision and you are faced with three choices:"
"a CAR, MOTORBIKE, and a SKATEBOARD")
second = input("Which of these three do you choose?")

if (second.lower() == "car"):
    print("You choose the car, and as you start your journey you have to go either LEFT or RIGHT")

    left_right = input("Do you turn LEFT or RIGHT?")
    if (left_right.lower() == "left"):
        print("You turn left and meet with the cops.")

        run_stop = input("Do you RUN or STOP")
        if (run_stop.lower() == "run"):
            print("You run and gets cased by the cops, you are caught and get jailed.")

        elif (run_stop.lower() == "stop"):
            print("You stop and get cautioned by the police for not having a driving permitt then set free.")
        else:
            print("Invalid input \nPlease try again!!!") 

    elif (left_right.lower() == "right"):
        print("You turn right and meet with Zombies")
        ride_get_down  = input("Do you RIDE the car into their midst or GETDOWN and run?")

        if (ride_get_down.lower() == "ride"):
            print("You ride towards their midst and get stuck, and get bitten by the Zombie.")

        elif (ride_get_down.lower() == "getdown"):
            print("You get down and start running and then get saved by a hunter.")

        else:
            print("Invalid input \nPlease try again!!! ")
    else:
        print("Invali input \nPlease try again!!!")
    

elif (second.lower() == "motorbike"):
    print("You start you ride with the motorbike, and then on your way your lost.")
    go_back = input("Do you CONTINUE in the lost path, or GO BACK? ")

    if (go_back.lower() == "continue"):
        print("You continue the ride and find people on a picnic.")
        join_ignore = input("Are you gonna JOIN them or IGNORE them?")

        if (join_ignore.lower() == "join"):
            print("You join them in the picnic and then get help from them with your direction.")
        elif (join_ignore.lower() == "ignore"):
            print("You ignore them and continue with the ride, then you fall into a valley.")
        else:
            print("Invalid input \nplease try again!!!")

    elif(go_back.lower() == "go back"):
        print("You go back and meet with competing bikers.")
        compete_watch = input("Are you going to COMPETE with them or WATCH them?")
        
        if (compete_watch.lower() == "compete"):
            print("You compete with them and win a trophy.")

        elif (compete_watch.lower() == "watch"):
            print("You watch and enjoy the sport but go home without a trophy.")
        else:
            print("Invalid input \nPlease try again!!!")

    else:
            print("Invalid input \nPlease try again!!!")

elif (second.lower() == "skateboard"):
    print("Yo pick the skateboard, and as you tear open its carton, you see TIME and MONEY.")
    time_money = input("So are you choosing the TIME or MONEY?")

    if (time_money.lower() == "time"):
        print("Chosing the time, it is either you use the time period to attend COLLEGE or get a SKILL ")
        attend_skill = input("Are you using your time to attend COLLEGE or get a SKILL?")

        if (attend_skill.lower() == "college"):
            print("You attend college and study your dream career and excel with it.")
        elif (attend_skill.lower() == "skill"):
            print("You use your time to get a skill, and become one of the worlds most famous man.")
        

    elif (time_money.lower() == "money"):
        print("You choose the money, and it is either you use it to pay your HOUSE RENT or SPEND with friends.")
        rent_spend = input("Are you paying your house RENT or SPEND it with friends? ")

        if (rent_spend.lower() == "rent"):
            print("Pay your house rent and avoid the embarassment of being thrown out of the house.")

        elif (rent_spend.lower() == "spend"):
            print("Spend the money with friends and get thrown out of the house at the end of the day.")
        else:
            print("Invalid input \nPlease try again!!!")

    else:
        print("Invalid input \nPlease try again!!!")


else:
    print("Invalid input \nPlease try again!!!") 



    end = "end", "start"
    end = "end", "start"

    print("Level 2 completed")
    print("Congrats!!!")
    stop = input("----------")          














    


