#import hashlib

#password = input("Type your password: ")
#encodedPassword = password.encode("utf-8")
#hashed = hashlib.md5(encodedPassword).hexdigest()
#print(hashed)

import platform
detail = platform.release()
name = platform.system()
processor = platform.processor()
architecture = platform.architecture()

MyLaptop = {
    "OS Name": name,
    "OS Details": (f"{name} {detail}"),
    "Processor": processor,
    "Architectural Detail": architecture,
}

for key,value in MyLaptop.items():
    print(f"{key} = {value}")