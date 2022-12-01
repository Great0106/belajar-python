number = int(input("Enter the number you would like to multiply with:"))
limit = int(input("How many times do you want to multiply?"))

for limit in range(1,limit,+1):
    result = number*limit
    print(f"{number} x {limit} = {result}")