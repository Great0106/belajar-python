student = ("Jaka", 15, "Tangerang")
print(f"Nama saya adalah {student[0]}")
print(f"Umur saya adalah {student[1]}")
print(f"Saya tinggal di {student[2]}")

fruits = ("apple", "banana", "cherry", "melon", "kiwi")
print(fruits[2]) #hanya index 2
print(fruits[1:4]) #index 1 sampai 4
print(fruits[1:5:2]) #index 1 sampai 5, 2 step
print(fruits[:4]) #hanya memanggil stop
print(fruits[::2]) #hanya memanggil step
print(fruits[-5:-1]) #index -5 sampai -1

find = "dragon fruit"
if find in fruits:
    print(f"There is {find} in fruits.")
else:
    print(f"There is no {find} in fruits.")