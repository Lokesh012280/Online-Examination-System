class Student:
    def __init__(self, student_id, name, course, email, phone):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.email = email
        self.phone = phone
        self.marks = 0
        self.result = "Not Attempted"

    def display(self):
        print("==============================")
        print("Student Details")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Course     :", self.course)
        print("Email      :", self.email)
        print("Phone      :", self.phone)
        print("Marks      :", self.marks)
        print("Result     :", self.result)

    def take_exam(self):
        score = 0

        print("\nONLINE EXAM STARTED")
        print("--------------------------")

        q1 = input("1. Python is a? \nA) Programming Language\nB) Database\nC) Browser\nEnter Answer: ")
        if q1.upper() == "A":
            score += 1

        q2 = input("2. Which keyword is used to define a function?\nA) function\nB) def\nC) define\nEnter Answer: ")
        if q2.upper() == "B":
            score += 1

        q3 = input("3. Which data type stores True/False?\nA) int\nB) string\nC) bool\nEnter Answer: ")
        if q3.upper() == "C":
            score += 1

        q4 = input("4. Which loop executes until condition becomes False?\nA) while\nB) switch\nC) case\nEnter Answer: ")
        if q4.upper() == "A":
            score += 1

        q5 = input("5. Which symbol is used for comments in Python?\nA) //\nB) #\nC) /*\nEnter Answer: ")
        if q5.upper() == "B":
            score += 1

        self.marks = score * 20

        if self.marks >= 60:
            self.result = "PASS"
        else:
            self.result = "FAIL"

        print("Exam Completed Successfully.")

    def show_result(self):
        print("\n========== RESULT ==========")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Marks      :", self.marks)
        print("Result     :", self.result)
        print("============================")

    def get_marks(self):
        return self.marks


students = []


def add_student():
    print("\nADD STUDENT")
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    stu = Student(student_id, name, course, email, phone)
    students.append(stu)

    print("Student Added Successfully.")


def view_students():
    if len(students) == 0:
        print("No Students Found.")
        return

    for stu in students:
        stu.display()


def search_student():
    student_id = int(input("Enter Student ID: "))

    for stu in students:
        if stu.student_id == student_id:
            stu.display()
            return stu

    print("Student Not Found.")
    return None


def remove_student():
    student_id = int(input("Enter Student ID: "))

    for stu in students:
        if stu.student_id == student_id:
            students.remove(stu)
            print("Student Removed Successfully.")
            return

    print("Student Not Found.")


def start_exam():
    stu = search_student()

    if stu:
        stu.take_exam()


def view_result():
    stu = search_student()

    if stu:
        stu.show_result()


def get_marks():
    stu = search_student()

    if stu:
        print("Marks :", stu.get_marks())


while True:

    print("\n===================================")
    print(" ONLINE EXAMINATION SYSTEM ")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Start Exam")
    print("6. View Result")
    print("7. Get Marks")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        remove_student()

    elif choice == 5:
        start_exam()

    elif choice == 6:
        view_result()

    elif choice == 7:
        get_marks()

    elif choice == 8:
        print("Thank You")
        break
    
    else:
        print("Invalid Choice")
