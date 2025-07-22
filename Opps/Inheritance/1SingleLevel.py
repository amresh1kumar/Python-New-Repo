# 1st
class Parent():
   def Student1(self):
      Name='Amresh'
      LastName='Kumar'
      Course='MCA'
      Fees='40K'
      print(Name,LastName,Course,Fees)
      pass
class Child(Parent):
   def Student2(self):
      Name='Sachin'
      LastName='Kumar'
      Course='BCA'
      Fees='35K'
      print(Name,LastName,Course,Fees)
obj1 = Child()
obj1.Student1()    
obj1.Student2()    




