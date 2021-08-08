import random
import time
import game
import object

"""Called by <usrlgn.py>"""
class action:

    def __init__(self):

        content, task = ['game', 'photo', 'music', 'exit'], 'null'

        while task != 'exit':
            print('\n\t', content, '\nto exit the interface just type exit\n')
            task = input('\t> ').lower()
            if task == "game":
                time.sleep(.5)
                print("so yOu WaNna PlaY GaMe; lEts gO.")
                game.play()
                time.sleep(random.randint(1, 5))

            elif task == "photo":
                print("GoOd cHoIse")
                time.sleep(.1)
                object.action(task)
                time.sleep(random.randint(1, 5))

            elif task == "music":
                print("lEst's DaNCe!")
                time.sleep(.2)
                object.action(task)
                time.sleep(random.randint(1, 5))

            elif task == "exit":
                print("Okay, haVe a NiCE tImE oUt oF mE")
                time.sleep(random.randint(5, 8))
                break

            else:
                print("New fEaturEs On near FutuRe!")
                time.sleep(1)
                print("New fEaturEs On near FutuRe!")
                time.sleep(1)
                print("New fEaturEs On near FutuRe!")
                time.sleep(1)
