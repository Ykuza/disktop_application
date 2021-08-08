import os, sys, subprocess

"""Called by <tsk.py>"""
def action(tsk):
    print("Yeaaaaaa")
    if tsk == 'photo':
        tsk = "photo/sa.png"

    else:
        tsk = "music/Rampampam.mp3"

    if sys.platform == "win32":
        os.startfile(tsk)

    else:
        pltfrm = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([pltfrm, tsk])
