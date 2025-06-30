#task 2

# * * * * * 
#   * * *
#     *

rows= 3
sp=0
star= 5

for i in range(rows):
   for j in range(sp):
      print(' ',end=' ')
   for k in range(star):
      print('*',end=' ')
   print()
   sp +=1
   star-=2