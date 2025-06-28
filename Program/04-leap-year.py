year = int(input("Enter an years: "))

if( year % 400 == 0 or (  year % 4 == 0 and year % 100 != 0 )):
   print(f'{year} is leap years')
else:
   print(f'{year} is not an leap years') 
