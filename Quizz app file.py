"""
Name:- Prerak Gupta
Enrollment number:-0103CS221289
"""
#The main concept is to fetch data and put them in these dictionaries
users = {}
quiz_questions = {}

def load_questions():
    with open("questions.txt", "r") as file:
        for line in file:
            # Strip whitespace and check if line is empty
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            # Split line and check if we have enough values
            parts = line.split(',')
            if len(parts) < 7:
                print(f"Skipping malformed line: {line}")
                continue

            # Unpack parts into question fields
            subject, question, *options, answer = parts
            if subject not in quiz_questions:
                quiz_questions[subject] = []
            quiz_questions[subject].append({
                "question": question,
                "options": options[:4],  # First 4 items as options
                "answer": answer
            })

    print("Questions loaded successfully.")


def load_users():
    with open("users.txt", "r") as file:
        for line in file:
            username, password, full_name, email, age = line.strip().split(',')
            users[username] = {
                "password": password,
                "full_name": full_name,
                "email": email,
                "age": age
            }

def register():
    print("----- Register -----")
    username = input("Enter username: ")
    if username in users:
        print("Username already exists! Try logging in.\n")
        return

    password = input("Enter password: ")
    full_name = input("Enter full name: ")
    email = input("Enter email: ")
    age = input("Enter age: ")
    users[username] = {
        "password": password,
        "full_name": full_name,
        "email": email,
        "age": age
    }
    with open("users.txt", "a") as file:
        file.write(f"{username},{password},{full_name},{email},{age}\n")
    print(f"Registration successful! Welcome, {full_name}.\n")

def login():
    print("----- Login -----")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password:
        print(f"Login successful! Welcome back, {users[username]['full_name']}.\n")
        return username
    else:
        print("Invalid login credentials or user not registered.\n")
        return None

def attempt_quiz(subject, username):
    score = 0
    print(f"\nStarting the {subject.upper()} quiz...\n")

    for i, question in enumerate(quiz_questions[subject]):
        print(f"Q{i + 1}: {question['question']}")
        for idx, option in enumerate(question["options"]):
            print(f"{idx + 1}. {option}")       
        answer = input("Your answer (1/2/3/4): ")
        if question["options"][int(answer) - 1] == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")

    print(f"Your final score: {score}/5\n")
    with open("score.txt", "a") as file:
        file.write(f"{username},{subject},{score}\n")


def quiz_menu(username):
    print("----- Quiz Menu -----")
    print("1. Python")
    print("2. DBMS")
    print("3. DSA")
    choice = input("Select a subject to attempt (1/2/3): ")

    subject_mapping = {'1': "python", '2': "dbms", '3': "dsa"}
    if choice in subject_mapping:
        attempt_quiz(subject_mapping[choice], username)
    else:
        print("Invalid choice! Returning to main menu.\n")

def main_menu():
    load_users()
    load_questions()
    
    while True:
        print("----- Main Menu -----")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                quiz_menu(username)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option! Please choose again.\n")

if __name__ == "__main__":
    main_menu()
