from record import actdic

name, age, job, pswrd, psrd, dtl = None, None, None, None, False, False
form, lst, dctnry = ["name", 'age', 'job', "pswrd"], list, dict

"""Called by <details.py>"""
def rcrd(nm, ag, jb):
    global age, job, name, dtl
    name, age, job, dtl = nm, ag, jb, True
    action()
    return True

"""Called by <pswrd.py>"""
def pas(pas):
    global pswrd, psrd
    pswrd, psrd = pas, True
    action()
    return True

def action():
    global dtl, psrd
    if dtl and psrd:
        global lst, dctnry
        lst = [name, age, job, pswrd]
        dctnry = dict(zip(form, lst))
        actdic(dctnry)

    else:
        pass

    return True
