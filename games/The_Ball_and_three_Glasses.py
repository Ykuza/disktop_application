import random
from time import sleep

"""This is a GAME made by me
you need to find the ball which is under one of three glasses."""

global candy
global answer
global wrong

def play():
    print("\nWe have three glasses")
    sleep(0.2)
    print("glass A, B and C")
    sleep(0.3)
    print("\n\tThere is one CANDY under one glass and by each rond the candy will replace")
    sleep(0.5)
    print("\tyou should find it\n")
    sleep(0.2)
    
    answer = 0
    wrong = 1
    candy = 'z'
    randnum = random.randint(1, 3)
    
    if randnum == 1:
        candy = 'A'
    
    elif randnum == 2:
        candy = 'B'
    
    elif randnum == 3:
        candy = 'C'

    
    print("For now its under <<{}>> glass." .format(candy))
    sleep(0.1)
    print("Now we wanna shake them")
    sleep(0.2)
    print("\tHung ooonnnn....\n")
    sleep(0.3)
    
    while True :
        
        if wrong > 1:
            print("For now its under <<{}>> glass." .format(candy))
            sleep(0.1)
            print("Shaking again....")
    
        sleep(2)
    
        randnum = random.randint(1, 3)
        randnum = random.randint(1, 3)
        randnum = random.randint(1, 3)
        randnum = random.randint(1, 3)
        randnum = random.randint(1, 3)
    
        if randnum == 1:
            candy = 'A'
    
        elif randnum == 2:
            candy = 'B'
    
        elif randnum == 3:
            candy = 'C'
    
        ansr = input("\nNow find it!\nTell me wich glass has the candy\n>> ")
        ansr = ansr.upper()
    
        if ansr == 'A' and 1 == randnum:
            print("\ncongratulations You gat the CANDY\nIt was under the <<{}>> glass" .format(candy))
            break
    
        if ansr == 'B' and 2 == randnum:
            print("\ncongratulations You gat the CANDY\nIt was under the <<{}>> glass" .format(candy))
            break
    
        if ansr == 'C' and 3 == randnum:
            print("\ncongratulations You gat the CANDY\nIt was under the <<{}>> glass" .format(candy))
            break
    
        else :
            sleep(0.3)
            print("\nOops Nothing was in it\nTry Next\n")
            wrong += 1
    
        sleep(0.2)
    
    print("\nYou have tryed <<{}>> rounds till finding the candy.\nCongratulations for finding it." .format(wrong))
    sleep(10)
