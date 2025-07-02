l=[]
l2=[]
num=int(input('Enter a number : '))
rem =0



while(num):
   rem=num % 2 
   num=num//2
   l.append(rem)
# print(l)   


count = len(l)

for i in range(0,count):
   l2.append(l[(count-1)-i])
print(l2)   


