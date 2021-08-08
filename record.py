import json

jdic, filename, dicsts, flnmsts = None, None, False, False

"""Called by <usrrcrd.py>"""
def actdic(dic):
    global jdic, dicsts
    jdic = json.dumps(dic)
    dicsts = True
    finlact()
    return True

def actfile(flnm):
    global filename, flnmsts
    filename = flnm
    flnmsts = True
    finlact()
    return True

def finlact():
    global dicsts, flnmsts, jdic, filename
    if dicsts and flnmsts:
        with open(filename, 'w') as a:
            a.write(jdic)
            a.close()

    else:
        pass

    return True
