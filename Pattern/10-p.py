rows =1
num=1

mainrow = int(input('Enter a number : '))

space = mainrow
for i in range(mainrow):
   for j in range(space):
      print(' ',end=' ')

   for k in range(rows):
      print(num, end=' ')
      num=num-1

   num = rows 
   for l in range(1,num):
      print(l+1,end=' ')
      l=l+1  
      
   print()
   rows= rows+1
   num=rows
   space=space-1

