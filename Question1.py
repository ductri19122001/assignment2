
n = int(input("Enter value for n: ")) #get user input
m = int(input("Enter value for m: "))
f= open('raw_text.txt', 'r') #open file
b=f.read() #read file
c1=[]

def encrypr(f,n,m):
 x=""
 for char in f:
    value = ord(char) #take ACSII value for each character
    if char.isalpha(): #check is alpha
        if char.islower(): #lower case
         if value >= 97 and value <= 109: #ACSII value range from a to m
            p=((value - 97 + (n*m))%26)   #take the value and move forward by n*m and circullar character in 26 alphabet characters     
            x += chr(p + 97) #get the character based on ACSII value
            c1.append(1) #validation the character in which case of 1,2,3,4
         else:
            p= ((value- 97 - (n+m))%26)  #take the value and move backward by n+m and circullar character in 26 alphabet characters              
            x += chr(p + 97)     
            c1.append(2)    #validation the character in which case of 1,2,3,4   
        else: #Upper case
          if value >= 65 and value <= 77:
            p=(((value - 65 - n))%26)#take the value and move backward by n and circullar character in 26 alphabet characters              
            x += chr(p + 65)
            c1.append(3) #validation the character in which case of 1,2,3,4   
          else:
           p=((value - 65 + (m**2))%26) #take the value and move forward by m^2 and circullar character in 26 alphabet characters  
           x += chr(p +65)  
           c1.append(4) #validation the character in which case of 1,2,3,4   
    else: # not character
     x+=char #write down the stuff
     c1.append(0) #classified as 0

 return x
   
   
def deencrypr(enrypt,n,m,c1):
 y=""
 
 for ind, char in enumerate(enrypt): #get index and character in encrypt file
    value = ord(char) #take ACSII value for each character
    if char.isalpha():#check is alpha
        if char.islower():#lower case
            if c1[ind]==1:   #specified the case from 1 to 4 to decrypt and is lower case
                      p=(value - 97 - (n*m) %26)      #move backward if case 1 by n*m       
                      y += chr(p+ 97)
            if c1[ind]==2: #specified the case from 1 to 4 to decrypt and is lower case
                      p= ((value- 97 + (n+m)) %26)     #move forward if case 2 by n+m                
                      y += chr(p + 97)
        else: #upper case
                    if c1[ind]==3: #specified the case from 1 to 4 to decrypt
                     p=(((value - 65 + n)) %26)  #move forward if case 3 by n     
                     y += chr(p +65)
                    if c1[ind]==4:#specified the case from 1 to 4 to decrypt
                      p=((value - 65 - (m**2)) %26) #move backward if case 4 by m^2
                      y += chr(p + 65)          
    else:
     y+=char   
 return y
   

enrypt= encrypr(b,n,m) #call the encryption function
i= open("encrypted.txt", "w") #write encrypted text to new file
i.write(enrypt) 
i.close()
dec=deencrypr(enrypt,n,m,c1) #call the dencryption function


print(f"the correctness is {b==dec}") #check correctness
