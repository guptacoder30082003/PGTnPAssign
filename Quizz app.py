"""
Name:- Prerak Gupta
Enrollment number:-0103CS221289
"""
users = {}
quiz_questions = {
    "python": [
        {"question": "What is the output of print(2 ** 3)?", "options": ["6", "9", "8", "7"], "answer": "8"},
        {"question": "Which one is immutable?", "options": ["List", "Set", "Dictionary", "Tuple"], "answer": "Tuple"},
        {"question": "What keyword is used to define a function?", "options": ["fun", "def", "function", "define"], "answer": "def"},
        {"question": "Which method is used to add an element to a set?", "options": ["append()", "add()", "insert()", "extend()"], "answer": "add()"},
        {"question": "What is the output of len([1, 2, 3, 4])?", "options": ["3", "4", "5", "2"], "answer": "4"}
    ],
    "dbms": [
        {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Simple Query Language", "Strong Question List", "Sequential Query Language"], "answer": "Structured Query Language"},
        {"question": "Which of the following is a NoSQL database?", "options": ["MySQL", "MongoDB", "PostgreSQL", "SQLite"], "answer": "MongoDB"},
        {"question": "What is a primary key?", "options": ["A unique identifier", "A foreign key", "An index", "A type of constraint"], "answer": "A unique identifier"},
        {"question": "Which command is used to remove a table?", "options": ["DELETE", "REMOVE", "DROP", "CLEAR"], "answer": "DROP"},
        {"question": "What is a foreign key?", "options": ["A primary key in another table", "A unique key", "A composite key", "None of these"], "answer": "A primary key in another table"}
    ],
    "dsa": [
        {"question": "Which data structure follows LIFO?", "options": ["Queue", "Tree", "Stack", "Graph"], "answer": "Stack"},
        {"question": "Which sorting algorithm has the worst case O(n^2)?", "options": ["Quick Sort", "Merge Sort", "Heap Sort", "Bubble Sort"], "answer": "Bubble Sort"},
        {"question": "Which of these is not a linear data structure?", "options": ["Array", "Stack", "Queue", "Tree"], "answer": "Tree"},
        {"question": "What is the time complexity of binary search?", "options": ["O(log n)", "O(n)", "O(n^2)", "O(1)"], "answer": "O(log n)"},
        {"question": "What is the worst case time complexity of merge sort?", "options": ["O(n log n)", "O(n)", "O(log n)", "O(n^2)"], "answer": "O(n log n)"}
    ]
}
def register():
    print("----- Register -----")
    username = input("Enter username: ")
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
    print(f"Registration successful! Welcome, {full_name}.\n")

def login():
    print("----- Login -----")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password:
        print(f"Login successful! Welcome back, {users[username]['full_name']}.\n")
        return True
    else:
        print("Invalid login credentials or user not registered.\n")
        return False

def attempt_quiz(subject):
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
    return score

def quiz_menu():
    print("----- Quiz Menu -----")
    print("1. Python")
    print("2. DBMS")
    print("3. DSA")
    choice = input("Select a subject to attempt (1/2/3): ")

    if choice == '1':
        attempt_quiz("python")
    elif choice == '2':
        attempt_quiz("dbms")
    elif choice == '3':
        attempt_quiz("dsa")
    else:
        print("Invalid choice! Returning to main menu.\n")

def main_menu():
    while True:
        print("----- Main Menu -----")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                quiz_menu()
            else:
                print("Please try logging in again or register if you haven't done so.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option! Please choose again.\n")

if __name__ == "__main__":
    main_menu()
