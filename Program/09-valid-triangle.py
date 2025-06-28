angle1=int(input('Enter the 1st angle: '))
angle2=int(input('Enter the 2nd angle: '))
angle3=int(input('Enter the 3rd angle: '))

if(angle1 > 0 and angle2 > 0 and angle3>0 and (angle1+angle2+angle3 == 180)):
   print('Valid triangle.')
else:
   print('Not a valid triangle')   