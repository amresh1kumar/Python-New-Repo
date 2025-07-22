class myclass():
   def function1(self):
      self.Name='Amresh'
      self.LastName='Kumar'
      self.Course='MCA'
      self.Fees='40K'
      print(self.Name,self.LastName,self.Course,self.Fees)
      print("Parent 1")
class myclass2(myclass):
   pass
class myclass3(myclass2):
   pass
class myclass4(myclass):
   pass

obj1= myclass4()
obj1.function1()