str1 = input('Enter a string : ')
str2 =''


for i in str1:
   if(not str2 == str1):
      str2= i + str2 

if(str2== str1):
 print('palindrome')
else:
    print('not palindrome')     

