#implement a function called sort_students that takes a list of students object as input and sorts the list based on their cgpa(cumulative grade point average)in descending order. each student object has the following attributes: name (string),roll_number(string ), and cgpa(float).test the function with different input list of students
class students:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
def sort_students(student_list):
  sorted_students=sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  return sorted_students
student=[students ("thirru ","a123",4.6),students ("dhanush ","a234",5.8),students ("Vishal ","a133",5.6)]
sorted_students=sort_students(student)
for student in sorted_students:
  print("name:{},roll number:{},cgpa:{}". format (student.name, student.roll_number,
                                                  student.cgpa))
  
