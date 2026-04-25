students = []
def add_students(name,marks):
    student = {"name": name,"marks": marks}
    students.append(student)

def display_student():
 for student in students:
  print(student["name"],student["marks"])

def show_passed_student():
  for student in students:
    if student["marks"]>=50:
      print(student["name"] ,"pass")
    else:
      print(student["name"] ,"fail")




def count_students():
  count =0
  for student in students:
    count = count+1
  print("total number of students" , count)

def avg_marks():
  total = 0
  for student in students:
    total = total + student["marks"]
  average = total/len(students)
  print("The average is", average)
    


add_students("Saad",90)
add_students("Rida",40)
display_student()
show_passed_student()
count_students()
avg_marks()