import random
import string
char = ["!","@","#","$","%","^","&","*","(",")"]
val = []

c=1
while c== 1:
    n = int(input("Enter the desire length of the password: "))
    for i in range(n//2):
        val.append(random.choice(string.ascii_uppercase))
        val.append(random.choice(string.ascii_lowercase))
        val.append(random.choice(string.digits))
        val.append(random.choice(char))
    random.shuffle(val)
    final = ""
    for i in range(n):
        final = final + val[i]
    print(final)
    print("Press 1 TO Continue")
    print("Press 0 To Exit")
    c =int(input())
    