import lgn
import details

def mainpg():
    a, lst = None, ['yes', 'no', 'exit']
    print("Wellcom\nlet us know if you have account or not?")
    while a != 'exit':
        print("Chose from list: ", lst, "\n\t>>", end=' ')
        a = input().lower()
        if a == "yes":
            lgn.action()
            return True
        elif a == 'no':
            print('So lets make some')
            details.rgstr()
            return True
        elif a == 'exit':
            return True
        else:
            print('\nError:')
mainpg()
