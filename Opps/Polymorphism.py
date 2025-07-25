# class Calculator:
#    def add(self, a, b=0, c=0):   # Overloaded function using default args
#       return a + b + c

# obj = Calculator()
# print(obj.add(5))         # 5
# print(obj.add(5, 10))     # 15
# print(obj.add(5, 10, 20)) # 35



class sample(): 
   def sum(self,a,b): 
      return a+b 
   def sum(self,a,b,c): 
      return a+b+c 
   def sum(self,a,b,c,d): 
      return a+b+c+d 
      
obj=sample() 
print(obj.sum(2,3,4,4)) 
print(obj.sum(1,2,3))