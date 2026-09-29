def check_password(pas):
    score = 0
    if len(pas) >= 8:
        score=score + 1
        print("Password has at least 8 characters")
    else:
        print("Password should have at least 8 characters")
    
    uppercase=False
    for character in pas:
        if character.isupper():
            uppercase = True
            break
    if uppercase:
        score=score + 1
        print("Password contains uppercase letter")
    else:
        print("Password should contain uppercase letter")

    lowercase=False
    for character in pas:
        if character.islower():
            lowercase = True
            break       
    if lowercase:
        score=score + 1
        print("Password contains a lowercase letter")
    else:
        print("Password should contain a lowercase letter")

    number=False

    for character in pas:
        if character.isdigit():
            number = True
            break
    if number:
        score=score + 1
        print("Password contains a number")
    else:
        print("Password should contain a number")

    special=False
    special_characters = "!@#$%^&*()-_=+[];:',.<>?/"
    for character in pas:
        if character in special_characters:
            special = True
            break
    if special:
        score=score + 1
        print("Pass contains a special character")
    else:
        print("Pass should contain a special character")


    print("\nPass Score:",score, "/ 5")

    if score<= 2:
        print("Pass Strength: WEAK")
    elif score<= 4:
        print("Pass Strength: MEDIUM")
    else:
        print("Pass Strength: STRONG")


def main():

    print("\nThis program checks your password using")
    print("five basic security requirements.")

    while True:
        print("a. Check Password")
        print("b. Exit")

        choice=input("Enter your choice: ")

        if choice=="a":
            password=input("\nEnter your pass: ")

            if password=="":
                print("Password cannot be empty.")
            else:
                print("\nPassword Analysis")
                check_password(password)

        elif choice=="b":
            print("\nThank you for using Password Strength Checker!")
            break

        else:
            print("\nInvalid choice.enter a or b.")



if __name__=="__main__":
    main()