# 1st
class Parent1():
   def Student1(self):
      Name='Amresh'
      LastName='Kumar'
      Course='MCA'
      Fees='40K'
      print(Name,LastName,Course,Fees)
      print("Parent 1")
      pass
class Parent2():
   def Student2(self):
      Name='Sachin'
      LastName='Kumar'
      Course='BCA'
      Fees='35K'
      print(Name,LastName,Course,Fees)
      print("Parent 2")

class Parent3():
   def Student3(self):
      Name='Aadity'
      LastName='Kumar'
      Course='B-Tech'
      Fees='40K'
      print(Name,LastName,Course,Fees)
      print("Parent 3")

class Child(Parent1,Parent2,Parent3):
      print("Child Class")
      pass
obj1 = Child()  
obj1.Student1()    
obj1.Student2()    
obj1.Student3()    