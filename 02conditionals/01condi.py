age = input("age : ")
age_int = int(age)

if (age_int<13) :
    print("User is Child")
elif(age_int<20):
    print("Teenager")
elif(age_int<60):
    print("Adult")
else:
    print("Senior")