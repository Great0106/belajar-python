class student:
    def __init__(self,name,address,phone):
        self.name = name
        self.addr = address
        self.phoneNumber = phone

    def welcome(self):
        print(f"Welcome {self.name}")
        print(f"Your address is {self.addr}")
        print(f"Your phone number is {self.phoneNumber}")

student1 = student("Jaka", "Jakarta", "012345")
student1.welcome
print("\n")
student2 = student("Heru", "Aceh", "543210")
student2.welcome
