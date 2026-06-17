import random
r = random.randint(1,5)
while True :
    gusse = int(input("ENTER YOUR GUSSE: "))
    if gusse == r:
        print("YOUR GUSSE IS RIGHT")
        break
    else:
        print("THAT IS A WRONG NUMBER")




