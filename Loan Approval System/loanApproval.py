# Loan Approval System
import pandas as pd
import os

def basic_eligibility(age, salary, credit_score, emis, loan_purpose):
    if age < 21 or age > 60:
        return False, "Applicant age must be between 21 and 60 years."
    elif salary < 60000:
        return False, "Monthly salary must be at least ₹60,000."
    elif credit_score < 650:
        return False, "Credit score below 650."
    elif emis > (0.5 * salary):
        return False, "Existing EMIs exceed 50% of monthly salary."
    elif loan_purpose not in ["home", "car", "education", "personal", "business"]:
        return False, "Invalid loan purpose entered."
    else:
        return True, ""

def new_record(name, age, gender, monthly_salary, credit_score, emis, loan_purpose, loan_amt, loan_tenure, rating, interest_rate, loan_status, reason):
    record = {
        "Applicant Name": name,
        "Age": age,
        "Gender": gender,
        "Loan Type": loan_purpose.title(),
        "Loan Amount": loan_amt,
        "Loan Tenure": loan_tenure,
        "Monthly Salary": monthly_salary,
        "Credit Score": credit_score,
        "Credit Rating": rating,
        "Monthly EMIs": emis,
        "Loan Category": loan_category(monthly_salary),
        "Interest Rate": interest_rate,
        "Loan Status": loan_status,
        "Rejection Reason": reason
    }
    return record

def applicant_details():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    while True:
        gender = input("Enter your gender (M/F): ").capitalize()
        if gender in ['M', 'F']:
            break
        print("Invalid input. Please enter 'M' for Male or 'F' for Female.")
    monthly_salary = float(input("Enter your monthly salary (in ₹): "))
    credit_score = int(input("Enter your credit score: "))
    emis = float(input("Enter your existing EMIs (in ₹): "))
    loan_purpose = input("Enter loan purpose (home, car, education, personal, business): ").lower()
    
    return name, age, gender, monthly_salary, credit_score, emis, loan_purpose

def credit_rating_interest(score):
    if score >= 750:
        rating = "Excellent"
        interest_rate = 8
        return rating, interest_rate
    elif score >= 700:
        rating = "Good"
        interest_rate = 9
        return rating, interest_rate
    elif score >= 650:
        rating = "Average"
        interest_rate = 10.5
        return rating, interest_rate
    else:
        return "Rejected", None

def loan_category(salary):
    if salary >= 200000:
        return "Platinum"
    elif salary >= 100000:
        return "Gold"
    elif salary >= 80000:
        return "Silver"
    else:
        return "Bronze"

def save_to_csv(record):

    if os.path.exists("Python_prg\\Loan Approval System\\loan_applications.csv"):
        df = pd.read_csv("Python_prg\\Loan Approval System\\loan_applications.csv")
    else:
        df = pd.DataFrame(columns=[
            "Applicant Name", "Age",
            "Gender", "Loan Type",
            "Loan Amount", "Loan Tenure",
            "Monthly Salary", "Credit Score",
            "Credit Rating", "Monthly EMIs",
            "Loan Category", "Interest Rate",
            "Loan Status", "Rejection Reason"
        ])
    df.loc[len(df)] = record
    df.to_csv("Python_prg\\Loan Approval System\\loan_applications.csv", index=False)
    print("\nApplication saved successfully.")

def view_records():
    if os.path.exists("Python_prg\\Loan Approval System\\loan_applications.csv"):
        df = pd.read_csv("Python_prg\\Loan Approval System\\loan_applications.csv")
        print("\n--- Loan Applications ---")
        print(df)
    else:
        print("\nNo loan applications found.")

def search_applicant():
    if not os.path.exists("Python_prg\\Loan Approval System\\loan_applications.csv"):
        print("\nNo loan applications found.")
        return
    df = pd.read_csv("Python_prg\\Loan Approval System\\loan_applications.csv")
    name = input("Enter the applicant's name to search: ")
    result = df[df["Applicant Name"].str.lower() == name.lower()]
    if result.empty:
        print("\nApplicant not found.")
    else:
        print("\n--- Search Results ---")
        print(result)

def bank_manager():
    while True:
        print("1. View all loan applications\n2. Search Applicant\n3. Exit")
        ch = int(input("Enter your choice (1-3): "))
        if ch == 1:
            view_records()
        elif ch == 2:
            search_applicant()
        elif ch == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

def applicant():
    details = applicant_details()
    name, age, gender, monthly_salary, credit_score, emis, loan_purpose = details
    loan_amt = float(input("Enter loan amount (₹): "))
    loan_tenure = int(input("Enter loan tenure (Years): "))

    loan_status = "Loan Rejected"
    rejection_reason = ""
    eligible, reason = basic_eligibility(age, monthly_salary, credit_score, emis, loan_purpose)
    if not eligible:
        rejection_reason = reason
    
   #loan amount criteria on the basis of loan purpose
    elif loan_purpose == "home" and not (500000 <= loan_amt <= 5000000):
        rejection_reason = "Home loan amount must be between ₹5,00,000 and ₹50,00,000."

    elif loan_purpose == "car" and not (300000 <= loan_amt <= 2000000):
        rejection_reason = "Car loan amount must be between ₹3,00,000 and ₹20,00,000."

    elif loan_purpose == "education" and not (100000 <= loan_amt <= 1000000):
        rejection_reason = "Education loan amount must be between ₹1,00,000 and ₹10,00,000."

    elif loan_purpose == "personal" and not (100000 <= loan_amt <= 1500000):
        rejection_reason = "Personal loan amount must be between ₹1,00,000 and ₹15,00,000."

    elif loan_purpose == "business" and not (500000 <= loan_amt <= 10000000):
        rejection_reason = "Business loan amount must be between ₹5,00,000 and ₹1,00,00,000."
        
    elif loan_tenure < 1 or loan_tenure > 30:
        rejection_reason = "Loan tenure must be between 1 and 30 years."
        
    else:
        loan_status = "Loan Approved"
    
    rating, interest = credit_rating_interest(credit_score)
    record = new_record(name, age, gender, monthly_salary, credit_score, emis, loan_purpose, loan_amt, loan_tenure, rating, interest, loan_status, rejection_reason)
    save_to_csv(record)
    print("\n========== Loan Result ==========")
    print("Loan Status:", loan_status)

    if rejection_reason:
        print("Reason:", rejection_reason)
    else:
        print("Credit Rating:", rating)
        print(f"Interest Rate: {interest}%")
        print("Loan Category:", loan_category(monthly_salary))

while True:
    print("\n========== Loan Approval System ==========")
    print("1. Bank Manager")
    print("2. Applicant")
    print("3. Exit")
    role = int(input("Enter your choice: "))

    if role == 1:
        bank_manager()
    elif role == 2:
        applicant()
    elif role == 3:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid Choice. Please try again.")