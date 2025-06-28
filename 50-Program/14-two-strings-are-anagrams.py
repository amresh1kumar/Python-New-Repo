str1 = 'ABC'
str2 = 'AAA'
c=''


if(len(str1) != len(str2)):
   print('not anagrams ')
else:
   for i in range(len(str1)):
      for j in range(len(str2)):
         if( str1[i] ==  str2[j]):
            c = c + str1[i]

   if(c == str1):
      print('anagrams')
   else:
      print('not anagrams ')
      
