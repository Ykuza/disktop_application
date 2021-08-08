import usrlgn

"""Called by <mainpg.py>"""
"""Called by <details.py>"""
def action():
    sts = False
    while not sts:
        print("\nFor LOGIN:\nType your username plz:\n\t>>", end=" ")
        usnm = input()
        usnm = usnm.lower()

        print("\nType your password now:\n\t>>", end=' ')
        pas = input()

        sts = usrlgn.srch(usnm, pas)
