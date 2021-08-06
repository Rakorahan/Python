import random
print("Your Generated Password is")
x = "abcdefghijklmnopqrstuvwxyz@#$-/*-+"

password = "".join(random.sample(x, 10))
print(password)
