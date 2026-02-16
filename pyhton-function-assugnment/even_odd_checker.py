def evenodd(num):
    if num%2==0:
        return 1
    else:
        return 0

number=5 
result=evenodd(number)
if result==1:
    print(f"Number is Even")
else:
    print("Number is Odd")