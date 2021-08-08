import time

""""This an IQ game just for fun"""

def train():
    time.sleep(1.4)
    print("\nWe have an electronic train running from West to East by 459 km/h speed;")
    time.sleep(6)
    print("The wind comes from North by 15 km/h of speed;")
    time.sleep(4)
    print("Now by the ratio speed of train and wind, tell me where it's Smoke Go?")
    time.sleep(5.6)
    print("Note!    Your at the roof of train!")
    time.sleep(3)
    print("\n\tHere is a list of choices:")
    time.sleep(3.4)
    #print()
    #time.sleep(.2)

    list_of_choices = ["West", 'West South', 'up']
    for g in list_of_choices :
        print(g)

    choice = input("\n> ")
    if choice == "west" :
         print("You'r score is 8/10")

    elif choice == "west south" :
        print("You'r score is 5/10")

    elif choice == "up" :
        print("You'r score is 2/10")

    else :
        print("Welldone you'r score is 10/10")

def play():
    print("Hi vega;\n\thappy birthday")
    time.sleep(2)
    
    print("\nHere is som IQ questions,",
        "\nIt's more like a game than a quiz;",
        "\nTheyrs All main",
        "\n will you play it?")

    answer = input("\n> ")

    if answer == 'yes' or 'ok' :
        print("Ok let't goooooooooo\n")
        time.sleep(.5)
        train()

    else :
        print("\n\tSo see you next time")
        time.sleep(1)
