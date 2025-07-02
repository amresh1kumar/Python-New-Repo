str1 = 'my name ()# !@#$$%^&*() is python'
str2= list(str1)

# print(type(str2))

for i in str2:
      if i.isalpha() or i.isspace():
         print(i, end='')
      else:
         continue
        