# randomtest.py

import random

result = []
while len(result) < 6:
    a = random.randint(1, 45)
    if a not in result:
        result.append(a)

print(result)
        
