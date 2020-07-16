from random import *
n = input('pasword length ')
n = int(n)
mixchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&amp;*().,?0123456789"
randompass = "".join(choice(mixchars) for x in range(n))
print("Your Random Password is: ", randompass)
