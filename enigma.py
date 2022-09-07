import os

from random import randrange, uniform

from tkinter import *


#

#

#This program is codenamed "Enigma" in reference to the German enigma machine

#which is a ww2 encryption machine that produce different codes

#for the same text

#

#This program is a hash function program that encrypts a text

#it can also decrypt the text also

#

#The

#digit() is used to count the digits in a number

def digit(num):

    i=int(len(str(num)))

    return i


#Python does not allow division by large numbers

#and if done so, will produce it in hex

#converting it from hex and into will produce a different result

#since the number is too large

#

#divison() function is a self made program to divide by large numbers

#it uses a basic division technique by splitting the number

#and dividing it seperately

def division(num,den):

    if(den==0):

        raise Exception('Cannot divide by zero')

    numstr=str(num)

    num=int(num)

    den=int(den)

    a=int(numstr[0])

    i=0

    q=0

    c=-1

    rem=0

    numdig=digit(num)

    res=''

    while(numdig!=0):

        while(a>=den):

            numdig-=1

            c+=1

        while((a<den)&(numdig!=0)):

            q+=1

            a=int(numstr[i:i+q])

            numdig-=1

            if((a<den)&(numdig!=0)):

                res+='0'

            c+=1

        q=1

        i=c

        res+=str(int(a/den))

        rem=a%den

        a=rem

        alist=list(numstr)

        alist[c]=str(rem)

        numstr="".join(alist)

        z=digit(rem)

        while(z>1):

            q+=1

            z=z-1

            c+=1

    return(int(res))


#putzero() function is used to put a set number of zeroes in front of a number

#to a certain digit

#

#e.g. (if set to 4 digits)

#"10" will be "0010"

#"3" will be "0003"

def putzero(num,m):

    res=''

    while(num<10**(m-1)):

        res=res+'0'

        num=num*10

    return(res)


#chiper() is the encryption function, the result will be stored in "morse.txt"

#

#this program will produce different codes yet if decrypted will always

#be the same amount

#

#The amount of the maximum text lenght are abritrary but I set it

#as 10^10 max possible characters

#

#the amount of possible variations of the produced code is arbritrary but I

#set it as the amount of every odd number between 15 until 15555

def chiper(inp):

    sec=randrange(15,15555,2)

    m=10

    dignum=0

    aspace=' '.join(format(ord(x), 'b') for x in inp)

    morse=''.join(format(ord(x), 'b') for x in inp)

    alist=aspace.split()

    for x in alist:

        if (len(x)==7):

           

            dignum=dignum+1

            morse=morse+'1'

        elif (len(x)==6):

            dignum=dignum+1

            morse=morse+'0'

        else:

            print("ERROR")

    dignum=putzero(dignum,m)+str(dignum)

    morse=morse+dignum

    morse=int(morse)*sec

    morse=str(morse)+putzero(sec,m)+str(sec)

    f=open("morse.txt","w+")

    f.write(morse)

    f.close()

    return morse


#dechiper() is the decryption function that will store the result in

#"translated.txt"

def dechiper():

    m=10

    i=0

    final=[]

    f=open("morse.txt")

    morse=f.read()

    sec=int(morse[-m:])

    morse=str(division(morse[0:-m],sec))

    lastdigits=int(morse[-m:])

    seq=morse[len(morse)-(m+lastdigits):len(morse)-m]

    actmorse=morse[:len(morse)-(m+lastdigits)]

    for x in seq:

        if(x=='1'):

            final.append(actmorse[i:i+7])

            i+=7

        elif(x=='0'):

            final.append(actmorse[i:i+6])

            i+=6

    i=0

    for x in final:

        final[i]=chr(int(final[i],2))

        i+=1

    f=open("translated.txt","w+")

    f.write(''.join(final))

    f.close()


#Main program#

   

root=Tk()

root.title("Enigman")

root.geometry("200x100")

text=Label(root,text="Please use this program discretly\nDo not change the output file name\nClose this notice to continue\n\n            -Anonymous")

text.pack(fill=X)

root.mainloop()


print("Do you want to Encrypt or Decrypt a text file?\nType 1 to encrypt\nType 2 to decrypt\nType anything else to terminate the program")

inp=input()

if((inp!='1')&(inp!='2')):

    raise Exception("You have terminated the program")

if(inp=='1'):

    print("Please type the message to be encrypted\nThe encrypted message will be named \"morse.txt\"")

    chiper(inp=input())

    print("Done!")

if(inp=='2'):

    print("The decrypted version will be stored in \"translated.txt\"")

    dechiper()


#

#

#Unused codes, may be used in future updates

#

#

#


#def guichiper():

#    gchip=Tk()

#    gchip.title("Chiper")

#    textchip=Label(gchip,text="Type code to be encrypted")

#    entchip=Entry(gchip, width=100)

#    entchip.grid(row=1,column=0,columnspan=30)

#    textchip.grid(row=0,column=1)

#    butchip=Button(gchip,text="Submit",fg="black",command=entchip.get())

#    butchip.grid(row=2,column=0)

#    gchip.mainloop

   

#root=Tk()

#root.title("Enigma")

#root.geometry("100x50")

#text=Label(root,text="Enigma")

#tfram=Frame(root)

#bfram=Frame(root)

#but1=Button(tfram,text="chiper",fg="black",command=chiper)

#but2=Button(tfram,text="dechiper",fg="black",command=dechiper)

#text.pack(fill=X)

#tfram.pack()

#bfram.pack(side=BOTTOM)

#but1.pack(side=LEFT)

#but2.pack(side=RIGHT)

#root.mainloop()