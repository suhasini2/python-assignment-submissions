scores=[72, 45, 89, 30, 60]

for i in scores:
    if i<50:
        print("Fail")
        continue
    elif i>=50:
        print("Pass")