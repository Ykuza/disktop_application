import json
import tsk

"""Called by <lgn.py>"""
data = None
def srch(usrnm, pas):
    f = "usrs/usr" + usrnm + ".json"
    try:
        global data
        with open(f) as opn:
            data = json.load(opn)

    except:
        print('hel')
        print("Wow\nUsername or password was wrong\nTry again with more accuracy")
        return False

    else:
        if data["pswrd"] == pas:
            tsk.action()

        else:
            print("Username or password was wrong\nTry again with more accuracy")
            return True
