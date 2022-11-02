def decToBinary(decimal):
    binary = bin(decimal)
    print(binary.replace("0b", ""))

decimal = int(input("Input the decimal number: "))
decToBinary(decimal)