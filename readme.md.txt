# Password Strength Checker

## 1. Project Overview

Password Strength Checker is a simple Python command-line program that checks how strong a password is.

The program checks different properties of the password, such as:
- Password length
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of numbers
- Presence of special characters

Based on these conditions, the program gives a score and classifies the password as Weak, Medium, or Strong.

---

## 2. Objective

The main objective of this project is to create a simple program that can help users understand whether their password contains the basic elements of a strong password.

This project also helps in understanding basic Python concepts such as:
- Variables
- Functions
- If-else statements
- For loops
- Strings
- User input
- Boolean conditions

---

## 3. Technologies Used

- **Programming Language:** Python
- **Interface:** Command Line / Terminal
- **Editor:** VS Code
- **Version Control:** Git and GitHub

No external Python libraries are required for this project.

---

## 4. How the Program Works

The program first asks the user to enter a password.

It then checks the password one condition at a time:

1. It checks whether the password has at least 8 characters.
2. It checks for an uppercase letter.
3. It checks for a lowercase letter.
4. It checks for a number.
5. It checks for a special character.

For every condition that is satisfied, the score is increased.

Finally, the program displays the total score and gives the password a strength level.

### Strength Levels

- **0–2:** Weak
- **3–4:** Medium
- **5:** Strong

---

## 5. Algorithm

1. Start the program.
2. Display the menu.
3. Ask the user to choose an option.
4. If the user chooses to check a password, take the password as input.
5. Check the length of the password.
6. Check for uppercase letters.
7. Check for lowercase letters.
8. Check for numbers.
9. Check for special characters.
10. Increase the score whenever a condition is satisfied.
11. Display the score.
12. Display the password strength.
13. Ask the user whether they want to check another password or exit.
14. End the program.

---

## 6. How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

You can check it by opening the terminal and typing:
