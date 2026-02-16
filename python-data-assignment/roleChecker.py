employee_data=(12,"Suhasini","admin")
roles={"admin","sales","editor","viewer"}
print(f"Employee ID: {employee_data[0]}")
print(f"Name: {employee_data[1]}")
print(f"Department: {employee_data[2]}")

if employee_data[2] in roles:
    print("Admin Access Yes")
else:
    print("Admin Access NO")
        