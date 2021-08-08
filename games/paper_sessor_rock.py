import time
import random

"""This is some forgeiner's game which works like <<paper, sissors, rock>> game which I don't know its methode.
I appreciated if you discover the methode for ur self."""

def play():
    player_points=0
    computer_points=0
    out_of_cards=False
    max_no_of_turns=5
    no_of_turns=0
    
    name=input("Enter your name here:")
    print()
    time.sleep(.9)
    print("Welcome to the game, ", name, "!")
    print()
    time.sleep(1.3)
    print("How to play: ")
    time.sleep(1.2)
    print("1.You can only use the cards that you have.")
    time.sleep(2)
    print("2.Everytime the result is draw, you will\n  get card.")
    time.sleep(2)
    print("3.The first player who got highest score after\n  5 turns will win the game.")
    time.sleep(2)
    print("4.If you enjoy the game don't FORGET to\n  click the star button.")
    print()
    time.sleep(2)
    
    print("Game loading...10%")
    time.sleep(1.2)
    print("Game loading...29%")
    time.sleep(1.5)
    print("Game loading...48%")
    time.sleep(2)
    print("Game loading...69%")
    time.sleep(1)
    print("Game loading...88%")
    time.sleep(1)
    print("Game loading...99%")
    time.sleep(2)
    print("Game loading...100")
    time.sleep(.7)
    print ()
    print("Game Started")
    time.sleep(.3)
    print()
    print("Player points: " +str(player_points))
    print("Computer points: " +str(computer_points))
    print()
    card=["rock","paper","scissor","rock","paper","scissor"]
    player_card=random.sample(card,k=5)
    computer_card=random.choices(card,k=5)
    
    print()
    while no_of_turns != max_no_of_turns:
        time.sleep(1.3)
        print("Your card: ")
        print(str(player_card))
        print()
        player_attack=input("Enter your attack here: ")
        print()
        time.sleep(1)
        print("You used: ")
        print(player_attack)
        time.sleep(1)
        computer_attack=random.choice(computer_card)
        print()
        print("Computer used: ")
        print (computer_attack)
        time.sleep(1)
    
        if player_attack=="paper" and computer_attack=="rock":
          try:
            print()
            time.sleep(1)
            print("You earn 1 point, you win!!")
            print()
            player_points+=1
            player_card.remove(player_attack)
            time.sleep(1.5)
            print("Your score: " + str(player_points))
            print("Computer score: " + str(computer_points))
            no_of_turns+=1
            print()
          except:
            time.sleep(1.3)
            print("Attack doesn't exist on your card")
            print()
             
        elif player_attack=="rock" and computer_attack=="paper":
          try:
            print()
            computer_points+=1
            player_card.remove(player_attack)
            time.sleep(1)
            print("Computer earn 1 point, computer win!!")
            print()
            time.sleep(1.5)
            print("Your score: " + str(player_points))
            print("Computer score: " + str(computer_points))
            no_of_turns+=1
            print()
          except:
            time.sleep(1.3)
            print("Attack doesn't exist on your card")
            print()
        elif player_attack=="scissor" and computer_attack=="paper":
          try:
            print()
            time.sleep(1)
            print("You earn 1 point, you win!!")
            print()
            player_points+=1
            player_card.remove(player_attack)
            time.sleep(1.5)
            print("Your score: " + str(player_points))
            print("Computer score: " + str(computer_points))
            no_of_turns+=1
            print()
          except:
            time.sleep(1.3)
            print("Attack doesn't exist on your card")
            print()
        elif player_attack=="paper" and computer_attack=="scissor":
          try:
            print()
            time.sleep(1)
            print("Computer earn 1 point, computer win!!")
            print()
            computer_points+=1
            player_card.remove(player_attack)
            time.sleep(1.5)
            print("Your score: " + str(player_points))
            print("Computer score: " + str(computer_points))
            no_of_turns+=1
            print()
          except:
            time.sleep(1.3)
            print("Attack doesn't exist on your card")
            print()
        elif player_attack=="scissor" and computer_attack=="rock":
          try:
            time.sleep(1)
            print()
            print("Computer earn 1 point, computer win!!")
            print()
            computer_points+=1
            player_card.remove(player_attack)
            time.sleep(1.5)
            print("Your score: " + str(player_points))
            print("Computer score: " + str(computer_points))
            no_of_turns+=1
            print()
          except:
            time.sleep(1.3)
            print("Attack doesn't exist on your card")
            print()
        elif player_attack=="rock" and computer_attack=="scissor":
          try:
            print()
            player_points+=1
            player_card.remove(player_attack)
            time.sleep(1)
            print("You earn 1 point, you win!!")
            print()
            time.sleep(1.5)
            print("Your score: " + str(player_points))
            print("Computer score: " + str(computer_points))
            no_of_turns+=1
            print()
          except:
            time.sleep(1.3)
            print("Attack doesn't exist on your card")
            print()
       
        elif player_attack==computer_attack:
          try:
            print()
            time.sleep(1.3)
            print("It is draw")
            time.sleep(1)
            print()
            print("You draw 1 card")
            player_card=player_card+random.sample(card, k=1)
            print()
          except:
            print("You don't have this card")
        
        else:
          print()
          time.sleep(1.3)
          print("invalid attack")
          print()                              
      
        
    if player_points>computer_points:
      time.sleep(.9)
      print()
      print("Congatulations!, you win!")
      time.sleep(1)
      print("Don't forget to click the star button!")
      print("Thank you")
    elif player_points<computer_points:
      time.sleep(.9)
      print()
      print("Computer win!")
      time.sleep(1)
      print("Try again to play to win!")
      time.sleep(.5)
      print("Don't forget to click the star button!")
      print("Thank you!")
