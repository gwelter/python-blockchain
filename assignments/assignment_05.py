from random import random
import datetime

print(random())
print(int((random() * 10) + 1))

print(datetime.datetime.fromtimestamp(random() * 10000000000))