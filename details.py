import usrnmvldty as us
import usrrcrd as rcrd
from pswrd import act
import lgn

"""Called by <mainpg.py>"""
def rgstr():

    print("Type ur compelit name:\n\t>>", end=' ')
    nm = input()
    print("Well How Old ru {}:\n\t>>".format(nm), end=' ')
    age = input()
    print("Okay {} what do u do for aliving:\n\t>>".format(nm), end=' ')
    job = input()

    u = False
    print("\nOkay {}\nChose a username for your self:".format(nm))
    while not u:
        print("\t>>", end=' ')
        usrnm = input()
        usrnm = usrnm.lower()
        u = us.chck(usrnm, nm)

    else:
        rcrd.rcrd(nm, age, job)
        act(nm)
        print("Congrats {}\nYou have been registered successfully".format(nm))
        lgn.action()

    return True
