contacts={"suhasini":"8885647898", "Gomathi":"9664578986", "Ravi": "9876543210"}
for key,value in contacts.items():
    print(key,value)

name=input("Enter name: ")
if name in contacts:
    print(contacts.get(name))
else:
    print("Contact not found")



