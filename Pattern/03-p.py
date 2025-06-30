
#task 3

rows =5
space= 3
star= 5

for i in range(rows):
   if(i == 0 or i == rows-1):
      for i in range(star):
         print('*',end=' ')
   else:
      for j in range(star-4):
         print('*',end=" ")
      for k in range(space):
         print(' ',end=' ')
      for l in range(star-4):
         print('*',end=" ")
   print()                  