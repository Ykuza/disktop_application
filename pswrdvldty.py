import re

lower = "[a-z]"
uper = "[A-Z]"
spchar = "[.,!@#$%&*?/]"
num = "\d"

"""Called by <pswrd.py>"""
def match(pas, cnfrm, nm):
    if pas == cnfrm:
        return True

    else:
        return False

"""Called by <pswrd.py>"""
def search(pas, nm):
    x = re.findall(lower, pas) and re.findall(uper, pas) and re.findall(spchar, pas) and re.findall(num, pas)
    if x and len(pas) >= 8:
        return True

    else:
        print("\nAttention {0}:\nPassword must contain more than 8 character at lest one spacial character (. , ! @ # $ % & * ? /), numbers, uppercase and lowercase alphabets.\nTry again {0}".format(nm))
        return False
