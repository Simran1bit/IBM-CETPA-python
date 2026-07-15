# Driving License
def driving_license_eligibility(age):
    if age >= 18:
        print("You are eligible for a driving license.")
    else:
        print("You are not eligible for a driving license.")
    
def learner_permit_eligibility(age):
    if age >= 16:
        print("You are eligible for a learner's permit.")
    else:
        print("You are not eligible for a learner's permit.")

while True:
    print("\nWelcome to the Driving Eligibility Checker!")
    choice = int(input("1. Check eligibility for Driver's License\n2. Check eligibility for Learner's Permit\n3. Exit\nEnter your choice (1-3): "))
    if choice == 3:
        print("Exiting the program. Goodbye!")
        break

    age = int(input("Enter your age: "))
    if choice == 1:
        driving_license_eligibility(age)
    elif choice == 2:
        learner_permit_eligibility(age)
    else:
        print("Invalid input. Please enter a number between 1 and 3.")