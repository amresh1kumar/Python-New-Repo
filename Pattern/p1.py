# rows =5
# star =5

# for i in range(rows):
#    for j in range(star):
#       print('*',end='')
#    print()  
#    star= star-1 

#task start
# 1st
#       * 
#     * * *
#   * * * * *
# * * * * * * *

# rows = 4
# stars = 1
# sp =3

# for i in range(rows):
#    for j in range(sp):
#       print(' ' ,end=' ')
#    for k in range(stars):
#       print('*',end=' ') 
#    print()
#    stars+=2
#    sp-=1



#task 2

# * * * * * 
#   * * *
#     *

# rows= 3
# sp=0
# star= 5

# for i in range(rows):
#    for j in range(sp):
#       print(' ',end=' ')
#    for k in range(star):
#       print('*',end=' ')
#    print()
#    sp +=1
#    star-=2


#task 3

rows =5
space= 3
star= 5

for i in range(rows):
   if(i == 0 or i == rows-1):
      for i in range(star):
         print('*',end=' ')
   else:
      for j in range(1):
         print('*',end=" ")
      for k in range(space):
         print(' ',end=' ')
      for l in range(1):
         print('*',end=" ")
   print()                  

#task 4











