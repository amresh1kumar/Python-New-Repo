# 1. Instance Method

# class Student:
#    def __init__(self, name):
#       self.name = name

#    def show(self):  # Instance method
#       self.name='Amresh'
#       print("Name:", self.name)

# s1 = Student("Vinay")
# s1.show()


#  2. Class Method
class Student:
   school = "DAV"

   @classmethod
   def change_school(cls, new_school):  # Class method
      cls.school = new_school

Student.change_school("DPS")
print(Student.school)
