star =5
rows=5
space=1

for i in range(rows):
   if(i==0 or i==4):
      for j in range(star):
         print('*',end=' ') 
      print()     
   else:
      print(end='')   
      for k in range(1):
            print('*',end=' ')
      for l in range(space):
            print(' ',end=' ')
      for m in range(1):
            print('*',end=' ')
      for o in range(space):
            print(' ',end=' ')
      for m in range(1):
            print('*',end=' ')
      for o in range(space):
            print(' ',end=' ')       
      print()            