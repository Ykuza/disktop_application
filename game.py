from games import paper_sessor_rock
from games import The_Ball_and_three_Glasses
from games import vega

"""Called by <tsk.py>"""
"""This is a terminal for games
much ever games we had will be listed here ready to be chosen"""
def gmply(prmtr):
    if prmtr == 'a':
        paper_sessor_rock.play()

    elif prmtr == 'b':
        The_Ball_and_three_Glasses.play()

    elif prmtr == "exit":
        return True

    elif prmtr == "c":
        vega.play()

    else:
        print("\nNew features are at next edition")
        
def play():
    prmtr = None
    print("Which game do you wanna play?")
    while prmtr != "exit":
        print("""\tType <a> for game (rock paper sessor)
        Type <b> for game (guessing the ball is under which glass)
        Type <c> for an IQ game
        Type <exit> for exit\n\t>>""", end=' ')
        prmtr = input()
        prmtr.lower()
        gmply(prmtr)
