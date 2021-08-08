from os.path import exists
from record import actfile as fl

"""Called by <usrnmvldty.py>"""
def chck(usr, snm):
    x = 'usrs/usr' + usr + '.json'
    y = exists(x)
    if y:
        print("Error:\nWe are sorry {} but username already exist\nplz try another".format(snm))
        return False

    else:
        fl(x)
        return True

#chck('bk119', 'bk')