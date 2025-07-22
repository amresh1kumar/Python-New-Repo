class Animal:
   def speak(self):
      print('Animal make a sound.')
class Dog(Animal):
   def speak(self):
      print('Dog Barks')
class Cat(Animal):
   def speak(self):
         print('Cat Meows')


#function that accepts any animal
def make_Sound(animal):
   animal.speak()


#Run-time decision which speak() to call
make_Sound(Animal())
make_Sound(Dog())
make_Sound(Cat())






