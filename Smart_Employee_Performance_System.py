"""
Smart Employee Performance & Bonus Evaluation System
Single-file working version (Phases 1-3 concepts)

Concepts:
- Variables, data types, input/output
- if/elif/else
- while, for
- Functions
- Lists and dictionaries
"""

employees=[]

def get_positive_float(msg):
    while True:
        try:
            v=float(input(msg))
            if v<0:
                print("Enter a positive value.")
            else:
                return v
        except ValueError:
            print("Invalid number.")

def get_score(q):
    while True:
        try:
            s=float(input(f"{q} Score (0-100): "))
            if 0<=s<=100:
                return s
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid score.")

def register():
    emp_id=input("Employee ID: ").strip()
    if any(e["id"]==emp_id for e in employees):
        print("Employee ID already exists.")
        return
    employees.append({
        "id":emp_id,
        "name":input("Name: ").title(),
        "department":input("Department: ").title(),
        "salary":get_positive_float("Salary: "),
        "experience":int(get_positive_float("Experience (years): ")),
        "performance":{},
        "average":0,
        "grade":"Not Assigned",
        "bonus":0
    })
    print("Employee registered.")

def grade(avg):
    if avg>=90:
        return "Outstanding"
    elif avg>=80:
        return "Excellent"
    elif avg>=70:
        return "Good"
    elif avg>=60:
        return "Average"
    return "Needs Improvement"

def bonus(salary,g):
    pct={"Outstanding":0.20,"Excellent":0.15,"Good":0.10,"Average":0.05}.get(g,0)
    return round(salary*pct,2)

def add_performance():
    emp_id=input("Employee ID: ")
    for e in employees:
        if e["id"]==emp_id:
            scores={q:get_score(q) for q in ("Q1","Q2","Q3","Q4")}
            e["performance"]=scores
            e["average"]=round(sum(scores.values())/4,2)
            e["grade"]=grade(e["average"])
            e["bonus"]=bonus(e["salary"],e["grade"])
            print("Performance updated.")
            return
    print("Employee not found.")

def report():
    emp_id=input("Employee ID: ")
    for e in employees:
        if e["id"]==emp_id:
            print("\n--- REPORT ---")
            for k,v in e.items():
                print(k,":",v)
            return
    print("Employee not found.")

def all_emp():
    for e in employees:
        print(e["id"],e["name"],e["grade"],e["average"])

while True:
    print("\n1.Register\n2.Add Performance\n3.Report\n4.Display All\n5.Exit")
    c=input("Choice: ")
    if c=="1": 
        register()
    elif c=="2": 
        add_performance()
    elif c=="3": 
        report()
    elif c=="4": 
        all_emp()
    elif c=="5": 
        break
    else: 
        print("Invalid choice.")
