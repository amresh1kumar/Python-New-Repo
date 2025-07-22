# 1st
class Parent():
   def Student1(self):
      Name='Amresh'
      LastName='Kumar'
      Course='MCA'
      Fees='40K'
      print(Name,LastName,Course,Fees)
      print("Parent Class called")
      print('')
class Child1(Parent):
   print("Child1 Class called")
class Child2(Parent):
   print("Child2 Class called")
class Child3(Parent):
   print("Child3 Class called")

obj1 = Child1()  
obj1.Student1() 
obj2 = Child2()  
obj2.Student1() 
obj3 = Child3()  
obj3.Student1()    


# class Animal():
#    a=10
#    print(a)
#    print('Hello')
   # def myclass(self):
   #    print('hello my class')
# Animal().myclass()    