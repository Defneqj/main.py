import random
chrs="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght=int(input("UZUNLUĞU GİRİN"))
password=""
for i in range(lenght):
    password+=random.choice(chrs)
print(password)