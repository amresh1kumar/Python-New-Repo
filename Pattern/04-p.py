rows =7
star =1 
space=3

for i in range(rows):
   if i==0 or i==rows-1:
      for l in range(space):
         print(' ',end=' ')
      for l in range(star):
         print('*',end='')
      print()     
   if(i== 1 or i== 2):
      for j in range(space-1):
         print(' ',end=' ')
      for k in range(star+1):
         print('*',end=' ')
      print()

   if(i==5 or i==3 ):
      for k in range(space-2):
         print(' ',end=' ')
      for m in range(star+2):
         print('*',end=' ')
      print()

   if(i==4):
      for m in range(star+3):
         print('*',end=' ')
      print()                    