#public

# class Student:
#    def __init__(self):
#       self.name = "Amresh"   # Public variable

#    def show(self):
#       print(self.name)

# obj = Student()
# print(obj.name)   # Accessible
# print(obj.show())   # Accessible



#protected

# class Student:
#    def __init__(self):
#       self._roll = 101    # Protected variable

# class Derived(Student):
#    def display(self):
#       print(self._roll)

# d = Derived()
# d.display()        # Accessible in subclass
# print(d._roll)     # Accessible but not recommended


#private


class Student:
   def __init__(self):
      self.__marks = 95   # Private variable

   def show(self):
      print(self.__marks)

obj = Student()
obj.show()           # Accessible via method
# print(obj.__marks)   # Error: can't access directly


