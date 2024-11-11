import numpy as np

# e2e = 
# v2v = 
f2f = set()

for i in range(6):
    v = (i//3 * 2 - 1) * 2**(i%3)
    f2f.add(v)

print(f2f)