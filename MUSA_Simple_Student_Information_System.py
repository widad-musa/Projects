# WIDAD P. MUSA #


#========== Simple Student Information System==========#

"""
Fields :- ['ID Number', 'Name of Student', 'Course', 'Year Level', 'Gender']

1. Add New Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
"""

import csv
student_fields = ['ID Number', 'Name of Student', 'Course', 'Year Level', 'Gender']
student_database = 'students.csv'


def display_menu():
    print("")
    print("====================")
    print(">> Welcome! <<")
    print("Student Information System")
    print("")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("")


#===============ADDING A STUDENT RECORD===============#


def add_student():
    print("")
    print(">>>  Add Student Information  <<<")
    print("")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("")
    print("Data Saved Successfully!")
    print("")
    input("Press ENTER to Continue")
    return


#===============VIEWING THE STUDENT LIST===============#


def view_students():
    global student_fields
    global student_database

    print("=====  STUDENT LIST OF RECORDS  =====")
    print("")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n=============================================")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press ENTER to Continue")


#===============SEARCHING A STUDENT RECORD===============#


def search_student():
    global student_fields
    global student_database

    print(">>>  Search Student  <<<")
    print("")
    roll = input("Enter ID Number to Search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print(">>>  Student Found  <<<")
                    print("")
                    print("ID Number: ", row[0])
                    print("Name: ", row[1])
                    print("Course: ", row[2])
                    print("Year Level: ", row[3])
                    print("Gender: ", row[4])
                    break
        else:
            print("Identification Number NOT FOUND!")
    input("Press ENTER to Continue")


#===============UPDATING A STUDENT RECORD===============#


def update_student():
    global student_fields
    global student_database

    print(">>>  Update Student  <<<")
    print("")
    idno = input("Enter ID Number to Update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if idno == row[0]:
                    index_student = counter
                    print("Student Found: ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


#===============CHECKING STUDENT RECORD===============#

                
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("ID Number Not Found")
        print("")

    input("Press ENTER to Continue")


#===============DELETING STUDENT RECORD===============#


def delete_student():
    global student_fields
    global student_database

    print(">>> Delete Student  Record <<<")
    print("")
    idno = input("Enter ID No. to Delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if idno != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID Number", idno, "is Deleted Successfully")
        print("")
    else:
        print("ID Number Not Found")
        print("")

    input("Press ENTER to Continue")

while True:
    display_menu()

    choice = input("Enter number of your choice: ")
    print("")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break

print("")
print("          THANK YOU !!         ")
print("")

