age=int(input("Enter the age: "))
id=bool(input("Have a ID card (Yes/No): "))

if age>=18 and id==True:
    print("Entry allowed")
else:
    print("Entry not allowed")