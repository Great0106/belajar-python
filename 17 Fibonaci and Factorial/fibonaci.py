number = int(input("Enter the number:"))

i = 0
firstvalue = 0
secondvalue = 1

while i < number:
    if i <= 1:
        nextvalue = 1
    else:
        nextvalue = firstvalue + secondvalue
        firstvalue = secondvalue
        secondvalue = nextvalue
    print(nextvalue)
    i = i + 1