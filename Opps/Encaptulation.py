class Student:
   def __init__(self, name, marks):
      self.__name = name        # private variable
      self.__marks = marks      # private variable

   def show(self):
      print("Name:", self.__name)
      print("Marks:", self.__marks)

   def set_marks(self, new_marks): # public method to modify private variable
      if 0 <= new_marks <= 100:
            self.__marks = new_marks
      else:
            print("Invalid Marks")

# Object banate hain
s1 = Student("Amresh", 90)
s1.show()

# Direct access - ye galti karega:
# print(s1.__marks)  

# Proper way to update:
s1.set_marks(95)     # Using method
s1.show()