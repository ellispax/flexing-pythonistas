#i want to use this to enter names for students and their test scores.
#we should be able to get the score of a student.
#have a menu to control 
#all in terminal

import random

students = {}

def add_student():
  name = input("Enter student's name: ").lower()
  score = int(input("Enter student's score: "))
  status = "Pass" if score >= 50 else "Fail"
  students[name] = {"score": score, "status": status}

def view_student_score():
  name = input("Enter student's name: ").lower()
  if name in students:
    print(f"Student {name}'s score is {students[name]['score']}.")
    print(f"Student {name}'s status is {students[name]['status']}.")
  else:
    print(f"Student {name} is not in the system.")

def view_all_students():
  for name, student in students.items():
    print(f"Student {name}'s score is {student['score']}.")
    print(f"Student {name}'s status is {student['status']}.")

def display_class_average():
  total_score = 0
  number_of_students = len(students)
  for score in students.values():
    total_score += score["score"]
  average_score = total_score / number_of_students
  print(f"The class average is {average_score}.")

def edit_student_score():
  name = input("Enter student's name to edit: ").lower()
  if name in students:
    score = int(input("Enter new score: "))
    status = "Pass" if score >= 50 else "Fail"
    students[name] = {"score": score, "status": status}
    print(f"Student {name}'s score has been updated to {score}.")
    print(f"Student {name}'s status is now {status}.")
  else:
    print(f"Student {name} is not in the system.")

def main():
  while True:
    print("Select an option:")
    print("1. Add student")
    print("2. View student's score")
    print("3. View all students")
    print("4. Display class average")
    print("5. Edit student's score")
    print("6. Quit")
    option = int(input())

    if option == 1:
      add_student()
    elif option == 2:
      view_student_score()
    elif option == 3:
      view_all_students()
    elif option == 4:
      display_class_average()
    elif option == 5:
      edit_student_score()
    elif option == 6:
      break

if __name__ == "__main__":
  main()
