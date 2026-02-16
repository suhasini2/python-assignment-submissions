sum=0
number=-1
print("Enter numbers to sum them up. Enter 0 to finish:")
while number!=0:
    number=int(input("Enter number: "))
    if number==0:
        break
    sum+=number
    
print(sum)

