import random
import time
number = random.randint(1, 6)
counter = 1
print(f"Anzahl des Counters: {counter}")
time.sleep(2)
print(number)

time.sleep(2)

counter += 1
number = random.randint(1, 6)
print(f"Anzahl des Counters: {counter}")
time.sleep(2)
print (number)
