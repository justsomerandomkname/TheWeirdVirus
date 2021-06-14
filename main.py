from tkinter import Tk
import random


randint = str(random.randint(50, 1000))
randint1 = str(random.randint(50, 500))

main=Tk()

main.geometry('+'+randint+'+'+randint)
main.geometry(randint1+'x'+randint1)


main.mainloop()