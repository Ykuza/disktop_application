import pswrdvldty as ps
from usrrcrd import pas

"""Called by <details.py>"""
def act(nm):
    c = False
    while c != True:

        u, pswrd, cnfps= False, None, None
        print('\nOk', nm, "We need a password also\nit must contain 8 characters encluding spacial characters, numbers, uppercase and lowercase.", end='')
        while u != True:
            print("\n\t >> ", end=" ")
            pswrd = input()
            u = ps.search(pswrd, nm)

        print("\nTime for confirm password:\n\t>>", end=' ')
        cnfps = input()
        c = ps.match(pswrd, cnfps, nm)
        if c:
            pas(pswrd)

        else:
            print("They didnt match but no problem lets try again")

    else:
        pass

    return True
