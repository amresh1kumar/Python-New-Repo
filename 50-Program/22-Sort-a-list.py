l1 = [1,5,1,2,3,4]
l2=[]

for i in l1:
   for j in l1:
      if(i<j):
         i=j
         l2.append(i)
print(l2)
