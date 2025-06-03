marks = int(input("Your marks: "))
if marks>=101:
    print("Please write correct no.")
    exit()
if (90<=marks<=100):
    print("Your grade is 'A' ")
elif (marks>=80):
    print("B")
elif (marks>=70):
    print("C")
elif (marks>=60):
    print("D")
else:
    print("F") 