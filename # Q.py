# Q1
def remove-char(word,D)
a=[]
for char in word :
    if char !=D.lower()and char!=D.Upper():
        a.append(char)
        return join (a)

#Q2
A1=int(input("enter the lower number"))
A2=int(input("enter the upper number"))
for num in range (A1,A2+1)
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
            else print (num)


#Q3
string = input("enter any string")
f= input("enter character")            
c=0
for int i in string:
    if i==f:
        c+=1
        print(c)S