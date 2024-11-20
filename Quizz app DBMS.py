"""
Name:- Prerak Gupta
Enrollment number:-0103CS221289
"""
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="user_management"
    )

def register_user():
    conn = connect_db()
    cursor = conn.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")
    full_name = input("Enter full name: ")
    email = input("Enter email: ")
    age = int(input("Enter age: "))
    cursor.execute("INSERT INTO users (username, password, full_name, email, age) VALUES (%s, %s, %s, %s, %s)", 
                   (username, password, full_name, email, age))
    conn.commit()
    conn.close()
    print("Registration successful.")

def login_user():
    conn = connect_db()
    cursor = conn.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        return username
    else:
        print("User not found. Please register.")
        register_user()
        return login_user()

def fetch_questions(topic):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT question FROM {topic}_questions")
    questions = cursor.fetchall()
    conn.close()
    return questions

def store_score(username, score):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (username, score) VALUES (%s, %s)", (username, score))
    conn.commit()
    conn.close()

def main():
    username = login_user()
    print("Pick a topic: 1. Python 2. DBMS 3. DSA")
    choice = int(input("Enter choice: "))
    topic = {1: "python", 2: "dbms", 3: "dsa"}.get(choice)
    if topic:
        questions = fetch_questions(topic)
        score = 0
        for q in questions:
            print(q[0])
            answer = input("Enter answer: ")
            if answer.lower() == "correct":
                score += 1
        store_score(username, score)
        print(f"Your score: {score}")
    else:
        print("Invalid choice")

main()
