def greetingName():
    name=input("Enter name: ")
    return f"Hello, {name}"

def avgScore(sub,scores):
    sum=0
    for i in scores:
        sum+=i
    return sum/sub


def result(avg):
    if avg>=50:
        return "Pass"
    else:
        return "Fail"
    
noSub=3
scores=[25,60,78]
def main():
    message=greetingName()
    print(message)
    print(f"Subjects: {noSub}")
    avg=avgScore(noSub,scores)
    print(f"Average Score: {avg}")
    print(f"Result: {result(avg)}")

main()
    
