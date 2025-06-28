char = input("Enter a character: ")
# char = ord(input("Enter a character: "))   # for finding ASCII value

if char=='a' or char =='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char == 'I' or char =='O' or char == 'U':
   print(f'{char} Is Vowel')
else:
   print(f'{char} Is Consonents')    