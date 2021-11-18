# son 100 va 100 oralig'idami
from termcolor import colored

son = int(input("Son kiriting: "))

if son < 0:
    son = son * -1

if 100 < son < 1000:
    print(colored("100 hamda 1000 oraliqida 👍", 'green'))
else:
    print(colored("Afsuski yo'q 🙅‍️", 'red'))