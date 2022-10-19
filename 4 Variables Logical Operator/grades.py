name = str(input("Input student's name here."))
subject = str(input("Input subject of exam here."))
grades = int(input("Input the student's grade."))

if grades >= 80:
    print(name+" passes the "+subject+" exam")
else:
    print(name+" has failed the "+subject+" exams. Their grade is too low and require a Remedial session.")