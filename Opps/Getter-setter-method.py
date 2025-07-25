class a():
      def __init__(self):
         self. __x = 20

      def getter(self):
         return self. __x
      def setter(self, n):
         self. __x = n

obj=a() 
print(obj.getter()) 
obj.setter(50) 
print(obj.getter())
