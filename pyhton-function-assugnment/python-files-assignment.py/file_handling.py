sum=0
with open("python-files-assignment.py/numbers.txt","r") as file:
    lines=file.readlines()

total_numbers_lines=len(lines)

for number in lines:
    sum+=int(number)

avg=sum/total_numbers_lines


with open("results.log","a") as logs:
    logs.write("File opened successfully\n")
    logs.write(f"Read {total_numbers_lines} numbers\n")
    logs.write(f"Sum: {sum}\n")
    logs.write(f"Average: {avg}\n")
    logs.write("Processing completed\n")
