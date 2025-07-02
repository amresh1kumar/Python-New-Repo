#           *  
#         *   *  
#       *       *  
#     *           *  
#   *               *  
# *                   *  
#   *               *  
#     *           *  
#       *       *  
#         *   *  
#           *

# rows=11
# star=1
# space=5

# for i in range(rows):
#    if(i==0 or i== 10):
#       for j in range(space):
#          print(' ',end=' ')
#       for k in range(star):
#          print('*',end=' ') 
#    elif(i== 10):
#       for j in range(space):
#          print(' ',end=' ')
#       for k in range(star):
#          print('*',end=' ')        
#    elif(i==1):
#       print()
#       for l in range(space-1):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       for n in range(space-4):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#    elif(i==9):
#       print()
#       for l in range(space-1):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       for n in range(space-4):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       print()         
#    elif(i==2):
#       print()
#       for l in range(space-2):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       for n in range(space-2):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       print()
#    elif(i==8):
#       print()
#       for l in range(space-2):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       for n in range(space-2):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       # print()   
#    elif(i==3):
#       # print()
#       for l in range(space-3):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       for n in range(space-0):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       print()
#    elif(i==7):
#       # print()
#       for l in range(space-3):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       for n in range(space-0):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       # print()   
#    elif(i==4 or i==6):
#       # print()
#       for l in range(space-4):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       for n in range(space+2):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       print()
#    elif(i==5):
#       for l in range(space-5):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       for n in range(space+4):
#          print(' ',end=' ')
#       for m in range(star):
#          print('*',end=' ')
#       print()


#           *  
#         *   *  
#       *       *  
#     *           *  
#   *               *  
# *                   *  
#   *               *  
#     *           *  
#       *       *  
#         *   *  
#           *

rows=5
space =4
star= 1


for i in range(rows):
   for j in range(space):
      print(' ',end=' ')
   for k in range(star):
      print('*',end=' ')   
   print()   
   space-=1






