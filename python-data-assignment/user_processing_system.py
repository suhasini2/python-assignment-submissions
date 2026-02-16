#from typing import List, Dict, Union, Set
users= [
    {
        "name":"Suhasini",
        "scores":[45,67,89],
        "roles":{"viewer"},
    },
    {
        "name":"Gomathi",
        "scores":[30,56],
        "roles":{"admin"},
    }
    ]

def userName():
    for i in users:
        print(f"Name: {i["name"]}")

def avgScore():
    for i in users:
            sum=0
            score=i["scores"]
            for j in score:
                sum+=j
                avg=sum/len(score)
            print(f"Average Score: {avg}")

def userRole():
    for i in users:
        role=i["roles"]
        if "admin" in role:
            print(f"Admin Access: {"True"}")
        else:
            print(f"Admin Access: {"False"}")

def main():
    userName()
    avgScore()
    userRole()

main()






