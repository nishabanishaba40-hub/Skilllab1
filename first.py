'''a=True
print(a)
a=[10,2,3,True,'Hello']
a.append(10)
print(a)
a=(10,)
print(a,type(a))
a={10,2,3,5j,False,'hi',(1,2)}
print(a)  
a={'a':[10,20,30],'b':40}
print(a['a'][1])
a=[10,2,3,4,False,5j,'hi',[1,2],(1,2),{1,2}]
print(a)
a.pop()
print(a)
a='Hello'
print(a[2:3+1:1])
a='Hello
print(a[2:4])
print(a[-3:-2+1:1])
a='Hello'
print(a[2:3+1:1])
a="Good Morning"
print(a[7:10+1:1])
a="Good Morning"
print(a[-5:-2+1:1])
a='hello'
print(a[3:0:-1])
print(a[-2:-5:-1])
print(a[::-1])
a='Good Morning'

'odM'

print(a[1:5+1:2])
a='Good Morning'

'Mng'

print(a[5:11+1:3])
a='Good Morning'

'Mng'

print(a[-7::3])
a='Good Morning'
'nr '
print(a[-2:-8-1:-3])

print(a[10:4-1:-3])
a=eval(input("enter:"))
print(a,type(a))
a=eval(input("enter:"))
print(a,type(a))'''
'''a=int(input("enter:"))
if a%2==0:
print("even")
else:
    print("odd")'''
'''ch=input("enter:")
if "A"<=ch<="Z":
    print('upper')
elif "a"<=ch<='z':
  print('lower')
else:
print("not an alphabet")'''

username='hero:'
password='hi@123'

'''if un==username:
    print("correct username")
    pw=input("enter password:")
    if pw==password:
        print("succesful login")
  else:
        print("incorrect pw")
else:
        print("incorrect username")'''
'''i=1
while i<=100:
    print(i)
    i+=1'''
'''i=1
while i<=50:
    if i%2==0:
        print(i,'even')
    i+=1'''
'''i=2
while i<=50:
    print(i)
    i+=2'''
'''n=1234
rev=0
while n>0:
      ld=n%10
      n=n//10
      rev=rev*10+ld
print(rev)'''
'''n=100
rev=0
while n>0:
      ld=n%10
      n=n//10
      rev=rev*10+ld
print(rev)'''
''''for i in range(1,101):
     print(i)
l=[10,20,30]
for i in l:
    print(i)'''
'''s=input('enter:')
out=''
for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        out+=chr(ord(i)-32)
    else:
        out+=1
print(out)
s=input("enter:")
rev=''
for i in s:
    rev=i+rev
print(rev)'''
'''for i in range(1,6):
    for j in range(1,6):
        print('*',end='')
    print()'''
'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('*',end='')
        else:
            print('@',end='')
    print()'''
'''a='Happy Birthday' 
'htr'
print(a[-4:-7:-1])'''
'''#with arg with return
 def convert(s,out):
 out=''
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert(input('enter a string:'),''))'''
'''#with arg without return
def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
print(convert(input('enter a string:'),''))'''
'''#without arg without return
def convert():
    s=input('enter:')
    out=''
    for i in s:
        if 'a'<=i<='z':
             out+=chr(ord(i)-32)
        else:
             out+=i
    print(out)        
convert()'''
'''#without arg with return
def convert():
    s=input('enter:')
    out=''
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return(out)        
print(convert())'''
'''class college:
    cname="GPLN"
    cloc='Hoodi'
s1=college()
print(s1.cname,s1.cloc)'''
'''class college:
    cname="GPLN"
    cloc='Hoodi'
s1=college()
print(s1.cname,s1.cloc)
college.cloc='KR PURAM' 
print(college.cloc)'''
'''class college:
    cname="GPLN"
    cloc='Hoodi'
s1=college()
s1.sname='Nisha'
s1.phno='9743458528'

s2=college()
s2.sname='Nalini'
s2.phno='9108656624'

print(s1.cloc)
s1.cloc='kr puram'
print('After changing')
print(s1.cloc)
print(s2.cloc)
print(college.cloc)'''
'''class college:
    def __init__(self,name,phno,usn):
        self.name=name
        self.phno=phno
        self.usn=usn
    def display(self):
        print(self.name,self.phno,self.usn)
s1=college('Nisha',7019524685,'1gd25cd029')
s2=college('Nalini',9108256645,'1gd25cd026')
s1.display()
s2.display()'''
'''class college:
    def __init__(self,name,phno,usn):
        self.name=name
        self.phno=phno
        self.usn=usn
    def display(self):
        print(self.name,self.phno,self.usn)
    def change_name (self,new): 
         self.name=new
s1=college('Nisha',7019524685,'1gd25cd029')
s2=college('Nalini',9108256645,'1gd25cd026')
s1.display()
s2.display()
s1.change_name('hareesh')
s1.display()
s2.change_name('gireesh')
s2.display()'''










