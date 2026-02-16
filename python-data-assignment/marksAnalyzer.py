marks=[78,85,90,65,35,88,92,80]
sum=0

print(f"Full list: {marks}")
print(f"First 3 marks: {marks[:3]}")
print(f"Last 3 marks: {marks[5:]}")

print(f"Max marks: {max(marks)}")
print(f"Min marks: {min(marks)}")

for i in marks:
    sum+=i
print(f"Average of marks: {sum/len(marks)}")