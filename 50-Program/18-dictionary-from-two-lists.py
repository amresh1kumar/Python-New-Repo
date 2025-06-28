l1=['name','age','rollno']
l2=['Amresh','21','07','BCA']

d= {}
# print(dict(zip(l1,l2)))


for i in range(len(l1)):
   
   if(len(l1) != len(l2)):
      print('Index out of bound')
      break
   else:   
      d[l1[i]] = l2[i]
      print(d) 





