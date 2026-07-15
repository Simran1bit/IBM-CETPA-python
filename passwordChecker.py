# password checker
# minimum characters, uppercase, special character, number
# not accepted- very weak:1, weak: 2, medium: 3, strong: 4

import re 
def check_password_strength(passw):
    score = 0
    suggestions = []

    # length check
    if(len(passw)>=5):
        score+=1
    else:
        suggestions.append("Password should be atleast 5 characters long.")
    
    # uppercase
    if re.search(r"[A-Z]",passw):
        score+=1
    else:
        suggestions.append("Password should contain atleast 1 upper case letter.")
    
    # lowercase
    if re.search(r"[a-z]",passw):
        score+=1
    else:
        suggestions.append("Password should contain atleast 1 lower case letter.")
    
    # special character
    if re.search(r"[~!@#$%^&*()_+-=|}{:?><;']", passw):
        score+=1
    else:
        suggestions.append("Password should contain atleast 1 special character.")

    # digit
    if re.search(r"[\d]", passw):
        score+=1
    else:
        suggestions.append("Password should contain atleast 1 digit.")

    return score, suggestions

password = input("Enter your password: ")
score, suggestions = check_password_strength(password)

if score <=2:
    print("Weak ❌")
elif score == 3 or score == 4:
    print("Medium 🟡")
else: 
    print("Strong ✅")

if suggestions:
    print("Suggestions to improve password: ")
    for i in suggestions:
        print("-", i)
    