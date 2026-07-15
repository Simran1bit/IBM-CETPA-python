# Student Report Card Generator
import pandas as pd
import os

if os.path.exists("Python_prg\\Student Report Card\\report_card.xlsx"):
    df = pd.read_excel("Python_prg\\Student Report Card\\report_card.xlsx")
else:
    df = pd.DataFrame(columns=[
        'Student Name', 'Student ID', 'Math', 'Science',
        'English', 'Hindi', 'SST',
        'Total Marks', 'Percentage', 'Grade', 'Result'
    ])
def calculate_grade(percentage):
    if percentage >= 95:
        return 'O'
    elif percentage >= 85:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

def generate_report_card(name, student_id, marks, total_marks, percentage, grade):
    # Generate report card
    print("\n--- Report Card ---")
    print(f"Student Name: {name}")
    print(f"Student ID: {student_id}")
    print("\nMarks:")
    
    for subject, mark in marks.items():
        print(f"{subject}: {mark}")
    
    # Calculate total percentage
    print(f"\nTotal Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Final Grade: {grade}")
    print("Result: " + ("Pass" if grade != 'F' else "Fail"))

def view_individual_report(student_id):
    student_data = df[df['Student ID'] == student_id]
    if not student_data.empty:
        student_data = student_data.iloc[0]
        marks = {
            'Math': student_data['Math'],
            'Science': student_data['Science'],
            'English': student_data['English'],
            'Hindi': student_data['Hindi'],
            'SST': student_data['SST']
        }
        generate_report_card(student_data['Student Name'], student_id, marks, student_data['Total Marks'], student_data['Percentage'], student_data['Grade'])
    else:
        print("No record found for the given Student ID.")

while True:
    print("\nWelcome to the Student Report Card Generator!")
    choice = int(input("1. Add a new student\n2. View individual report\n3. View class report\n4. Exit\nEnter your choice: "))
    if choice == 4:
        print("Exiting the program. Goodbye!")
        break

    elif choice == 1:
        # Get student information
        while True:
            student_id = int(input("Enter the student's ID: "))

            if student_id in df["Student ID"].values:
                print("This Student ID already exists.")
                ans = input("Do you want to overwrite it? (yes/no): ").lower()

                if ans == "yes":
                    df = df[df["Student ID"] != student_id]
                    break
                else:
                    print("Enter another Student ID.")
            else:
                break
        student_name = input("Enter the student's name: ").lower()
        # Get marks for subjects
        subjects = ['Math', 'Science', 'English', 'Hindi', 'SST']
        marks = {}

        # marks for each subject
        for sub in subjects:
            while True:
                mark = int(input(f"Enter the mark for {sub}: "))
                if 0 <= mark <= 100:
                    marks[sub] = mark
                    break
                else:
                    print("Please enter marks between 0 and 100.")

        # Total marks and percentage calculation
        total_marks = sum(marks.values())
        percentage = total_marks / len(marks)

        new_row = pd.DataFrame([{
            'Student Name': student_name,
            'Student ID': student_id,
            'Math': marks['Math'],
            'Science': marks['Science'],
            'English': marks['English'],
            'Hindi': marks['Hindi'],
            'SST': marks['SST'],
            'Total Marks': total_marks,
            'Percentage': percentage,
            'Grade': calculate_grade(percentage),
            'Result': "Pass" if calculate_grade(percentage) != 'F' else "Fail"
        }])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel("report_card.xlsx", index=False)
        generate_report_card(student_name, student_id, marks, total_marks, percentage, calculate_grade(percentage))

    elif choice == 2:
        stu_id = int(input("Enter the Student ID to view the report: "))
        view_individual_report(stu_id)
    
    elif choice == 3:
        print("\n--- Class Report ---")
        print(df)
    
    else:
        print("Invalid Choice.")
