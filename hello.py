import numpy as np

msg = "Roll a dice!"
msg1 = "Roll another dice!"

print(msg)
print(np.random.randint(1,9))

print(msg1)
x = np.random.randint(1,6)
print(x)

if x < 10:
    print('smaller')

if x > 20:
    print('biger')

print('Finish')