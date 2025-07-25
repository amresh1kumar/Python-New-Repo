#Type Check

# class sample(): 
#    pass 
# n=sample() 
# print(n) 
# print(type(sample))


#class variable example

#Access variable of class by class name and through object

# class student():
#    s_name='Amresh'
#    s_lname='Kumar'
#    s_roll_no='07'
# obj1=student()
# obj2=student()
# #accessing class variable by using object name
# print(obj1.s_name,obj1.s_lname,obj1.s_roll_no)   
# print(obj2.s_name,obj2.s_lname,obj2.s_roll_no)   

# #accessing class variable by using class name
# print(student().s_name,student().s_lname,student().s_roll_no)





#new
#we modify class variables by using class name it affect all the objects that belongs to a class

# class student():
#    s_name='Amresh'
#    s_lname='Kumar'
#    s_roll_no='07'

# obj1=student()
# obj2=student()
# #modify the class variable by using clasname
# # student().s_name='sachin'
# # student().s_lname='kumar'
# # student().s_roll_no='08'
# student.s_name='sachin'
# student.s_lname='kumar'
# student.s_roll_no='08'

# print(obj1.s_name,obj1.s_lname,obj1.s_roll_no)  
# print(obj2.s_name,obj2.s_lname,obj2.s_roll_no)  



#new
#we modify class variables by using class name it affect all the objects that belongs to a class
# class student():
#    s_name='Amresh'
#    s_lname='Kumar'
#    s_roll_no='07'

# obj1=student()
# obj2=student()
# #modify the class variable by using object name
# obj1.s_name='sachin'
# obj1.s_lname='kumar'
# obj1.s_roll_no='08'

# print(obj1.s_name,obj1.s_lname,obj1.s_roll_no)  
# print(obj2.s_name,obj2.s_lname,obj2.s_roll_no)




#new 

# class Student:
#    pass  # koi constructor nahi, khali class hai

# # ab object banaya aur variables baad me assign kiye
# s1 = Student()
# s1.name = "Amresh"
# s1.roll = 101

# s2 = Student()
# s2.name = "Sachin"
# s2.roll = 102

# print("\nWithout Constructor:")
# print("Student 1:", s1.name, s1.roll)
# print("Student 2:", s2.name, s2.roll)


#new 

#object variable example



#Object variables are declared inside the constructor or inside the function

#example of inside the function
# class fruit():
#    def Apple(self,fruit_name,color,quantity,cost):
#       self.fruit_name=fruit_name  #here self.fruit is object variable fruit_name is not a object variable 
#       self.color=color            # here self.color object variable
#       self.quantity=quantity      # here self.quantity object variable
#       self.cost=cost              # here self.cost object variable
#    def Display(self):
#       print('Fruit Name  :',self.fruit_name)
#       print('Fruit Color :',self.color)
#       print('Fruit quantity :',self.quantity)
#       print('Fruit Cost  :',self.cost)

# obj1=fruit()
# obj1.Apple('Apple','red','1kg','100rs')
# obj1.Display()


#example of inside the constructor

# class fruit():
#    def __init__(self,fruitName,color,quantity,cost):
#       self.fruitName=fruitName
#       self.color=color
#       self.quantity=quantity
#       self.cost=cost

# obj1= fruit('Mango','Yellow & Green','1kg','80rs')
# print(obj1.fruitName,obj1.color,obj1.quantity,obj1.cost)

