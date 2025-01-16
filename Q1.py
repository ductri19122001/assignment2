
n = int(input("Enter value for n: "))
m = int(input("Enter value for m: "))
f= open('raw_text.txt', 'r') 
b=f.read()
c1=[]

def encrypr(f,n,m):
 x=""
 for char in f:
    value = ord(char)
    if char.isalpha():
        if char.islower():
         if value >= 97 and value <= 109:
            p=((value - 97 + (n*m))%26)        
            x += chr(p + 97)
            c1.append(1)
         else:
            p= ((value- 97 - (n+m))%26)           
            x += chr(p + 97)     
            c1.append(2)       
        else:
          if value >= 65 and value <= 77:
            p=(((value - 65 - n))%26)
            x += chr(p + 65)
            c1.append(3)
          else:
           p=((value - 65 + (m**2))%26)
           x += chr(p +65)  
           c1.append(4)
    else:
     x+=char
     c1.append(0)

 return x
   
   
def deencrypr(enrypt,n,m,c1):
 y=""
 
 for ind, char in enumerate(enrypt):
    value = ord(char)
    if char.isalpha():
        if char.islower():
            if c1[ind]==1:   
                      p=(value - 97 - (n*m) %26)             
                      y += chr(p+ 97)
            if c1[ind]==2:
                      p= ((value- 97 + (n+m)) %26)              
                      y += chr(p + 97)
        else:
                    if c1[ind]==3:
                     p=(((value - 65 + n)) %26)
                     y += chr(p +65)
                    if c1[ind]==4:
                      p=((value - 65 - (m**2)) %26)
                      y += chr(p + 65)          
    else:
     y+=char   
 return y
   

enrypt= encrypr(b,n,m)
i= open("encrypted.txt", "w") 
i.write(enrypt) 
i.close()
dec=deencrypr(enrypt,n,m,c1)
i= open("dec.txt", "w") 
i.write(dec) 
i.close()

print(f"the correctness is {b==dec}")
