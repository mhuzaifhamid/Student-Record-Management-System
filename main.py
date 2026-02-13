import json
import os


# ------------------ File Names ------------------
STUDENT_FILE = "students.json"
USER_FILE = "users.json"


# ------------------ Student Class ------------------
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 85:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 55:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "marks": self.marks,
            "grade": self.grade
        }


# ------------------ File Handling ------------------
def load_students():
    if not os.path.exists(STUDENT_FILE):
        return []

    with open(STUDENT_FILE, "r") as file:
        return json.load(file)


def save_students(students):
    with open(STUDENT_FILE, "w") as file:
        json.dump(students, file, indent=4)


def load_users():
    if not os.path.exists(USER_FILE):
        default_user = {"admin": "1234"}

        with open(USER_FILE, "w") as file:
            json.dump(default_user, file, indent=4)

        return default_user

    with open(USER_FILE, "r") as file:
        return json.load(file)


# ------------------ Login System ------------------
def login(users):
    print("\n===== Login =====")

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Login successful!\n")
        return True

    print("Invalid username or password.")
    return False


# ------------------ Validation ------------------
def get_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Please enter a valid number.")


def get_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Please enter a valid number.")


# ------------------ Core Functions ------------------
def add_student(students):
    roll_no = get_int("Enter Roll No: ")

    for s in students:
        if s["roll_no"] == roll_no:
            print("Roll number already exists!")
            return

    name = input("Enter Name: ")
    marks = get_float("Enter Marks: ")

    student = Student(roll_no, name, marks)
    students.append(student.to_dict())

    print("Student added successfully.")


def display_all(students):
    if not students:
        print("No records found.")
        return

    print("\nRoll No   Name                 Marks   Grade")
    print("-" * 50)

    for s in students:
        print(f"{s['roll_no']:<9} {s['name']:<20} {s['marks']:<7} {s['grade']}")


def search_student(students):
    roll_no = get_int("Enter Roll No: ")

    for s in students:
        if s["roll_no"] == roll_no:
            print("\nRoll No   Name                 Marks   Grade")
            print("-" * 50)
            print(f"{s['roll_no']:<9} {s['name']:<20} {s['marks']:<7} {s['grade']}")
            return

    print("Student not found.")


def update_student(students):
    roll_no = get_int("Enter Roll No: ")

    for s in students:
        if s["roll_no"] == roll_no:
            s["name"] = input("New Name: ")
            s["marks"] = get_float("New Marks: ")

            temp = Student(s["roll_no"], s["name"], s["marks"])
            s["grade"] = temp.grade

            print("Record updated.")
            return

    print("Student not found.")


def delete_student(students):
    roll_no = get_int("Enter Roll No: ")

    for i, s in enumerate(students):
        if s["roll_no"] == roll_no:
            del students[i]
            print("Record deleted.")
            return

    print("Student not found.")


def sort_by_marks(students):
    students.sort(key=lambda x: x["marks"], reverse=True)
    print("Sorted by marks (high to low).")


def show_top_3(students):
    if not students:
        print("No records found.")
        return

    sorted_list = sorted(students, key=lambda x: x["marks"], reverse=True)

    print("\nTop 3 Students")
    print("-" * 40)

    for s in sorted_list[:3]:
        print(f"{s['roll_no']}  {s['name']}  {s['marks']}  {s['grade']}")


# ------------------ Menu ------------------
def menu(students):
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display All")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort by Marks")
        print("7. Show Top 3")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_all(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            sort_by_marks(students)

        elif choice == "7":
            show_top_3(students)

        elif choice == "0":
            save_students(students)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice!")


# ------------------ Main ------------------
def main():
    users = load_users()
    students = load_students()

    if login(users):
        menu(students)
    else:
        print("Access denied.")


if __name__ == "__main__":
    main()
