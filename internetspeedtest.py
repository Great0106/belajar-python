#Internet Speed Test
print("Internet Speed Test")
print("Welcome to the Internet Speed Test")
internetspeed = int(input("Please enter your internet speed."))

while internetspeed >0:
    if internetspeed >=25:
        print("Your Internet connection is good!")
        break
    elif internetspeed <25 and internetspeed >15:
        print("Your Internet connection is fine.")
        break
    elif internetspeed <=15:
        print("Your Internet is connection is bad.")
        break
else:
    print("Internet is down.")