#add key value pair into the dictionary: 
# d={}
# d['a']=10
# d['a']=20
# d['b']=20 
# d[1]=20 
# d[(22,33)]=30 
# d[2.0]=40 
# print(d)

#this method is used to add multiple key value pair to the dictionary
# x={'a':10,'b':20} 
# y={'c':30,'d':40} 
# x.update(y) 
# print(x) 
# print(y)

#pop()
n={'a':10,'b':20,'c':30} 
# m=n.pop('a') 
# print(m) 
# print(n) 
# x=n.pop('d') 
x=n.popitem()  # it return or delete the  last key and values value pair from the dic and return in tuple form 
print(x)
print(n)

#get
# g={'a':10,'b':20,'c':30,'d':40} 
# print(g.get('a')) 
# print(g.get('f',100)) 
# print(g.get('g'))

#setdefault
# s={'a':10,'b':20,'c':30,'d':40} 
# print(s.setdefault('d'))  
# print(s.setdefault('f',100)) 
# print(s.setdefault('g')) 
# print(s)

#fromkeys
# d={} 
# x=d.fromkeys('abc',[1,2,3]) 
# print(x)

# l=3
# j=1
# print(l is j)

# a=11
# print("yes") if a>10 else print("no")
# # print(vote)

# if a>10:
#    print("yes")
# else:
#    print("no")