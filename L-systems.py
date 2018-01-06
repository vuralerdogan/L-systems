from tkinter import *
import tkinter as tki
from tkinter import Tk, Button, ttk
import turtle
import sys
import os
from PIL import ImageTk
import numpy as np
import random
import itertools

#-=B AND .=A
MORSE = {'A': 'AA',  'B': 'BAAA', 'C': 'BABA',
        'D': 'BAA',  'E': 'A',    'F': 'AABA',
        'G': 'BBA',  'H': 'AAAA', 'I': 'AA',
        'J': 'ABBB', 'K': 'BAB',  'L': 'ABAA',
        'M': 'BB',   'N': 'BA',   'O': 'BBB',
        'P': 'ABBA', 'Q': 'BBAB', 'R': 'ABA',
        'S': 'AAA',  'T': 'B',    'U': 'AAB',
        'V': 'AAAB', 'W': 'ABB',  'X': 'BAAB',
        'Y': 'BABB', 'Z': 'BBAA',

        '0': 'BBBB', '1': 'ABBBB', '2': 'AABBB',
        '3': 'AAABB', '4': 'AAAAB', '5': 'AAAAA',
        '6': 'BAAAA', '7': 'BBAAA', '8': 'BBBAA',
        '9': 'BBBBA',

        }
#The above dictionary can be converted for general function.
#For example; 'A': uniquestring[0]+uniquestring[0] (in my project, it symbolises 'AA' or 'BB')
#We preferred short way to illustrate the cryption method.
#Therefore, the user can study on various strings or characters by creating own dictionary or codes
#such as 'D', 'X', 'a', '+', '-', '[', ']' etc.


# The morse alpahet translated from http://code.activestate.com/recipes/578407-simple-morse-code-translator-in-python/
InvMorse = {v: k for k, v in MORSE.items()}
MyGUI = Tk()
MyGUI.title("L-System")
MyGUI.geometry("1350x800+0+0")

MyGUI.configure(background='black')

#frame
frame = tki.Frame(MyGUI, bg='black')
frame.pack(fill='both', expand='yes')

#background panel
image1 = ImageTk.PhotoImage(file="matrix.jpg")
w = image1.width()
h = image1.height()
bgpanel = tki.Label(frame, image=image1)
bgpanel.pack(side='top', fill='both', expand='yes')
bgpanel.image = image1

#Text Area
T = Text(frame, bg="white" , height=15, width=116,undo=True)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=T.yview)
T.config(yscrollcommand=scrollbar.set)
T['font'] = ('consolas', '12')
T.place(x=500,y=550)
T.config(background='black', fg='#67F383')
hcanvsize=510
wcanvsize=810
frame2 = tki.Frame(frame, bg='black', width=810, height=510)
frame2.place(x=500,y=5)
cv = turtle.ScrolledCanvas(frame2,  canvwidth=wcanvsize, canvheight=hcanvsize)
cv.config(background="black")
cv.place(x=0, y=0)
screen = turtle.TurtleScreen(cv)
screen.bgcolor('black')
screen.delay(0)
t = turtle.RawTurtle(screen)
cv.config(width=800,height=500)
cv.pack(side=LEFT,expand=True,fill=BOTH)


#ENTRIES

#axiom settings
axiom=Label(frame, text="Axiom:")
axiom.place(x=22, y=20)
axe = Entry(frame, bd=2)
axe.place(x=82, y=15)
axe.config(bg="black", fg="#00ff00")
axiom.config(bg="black",fg="#00ff00")
axiom.config(font=('Comic Sans MS',13,"bold"))

#rule1 settings
label1=Label(frame, text="Rule1:")
label1.place(x=22 ,y=50)
label1.config(bg="black",fg="#00ff00")
label1.config(font=('Comic Sans MS',13,"bold"))
rle1 = Entry(frame, bd=2, width=10)
rle1.place(x=82, y=45)
rle1.config(bg="black", fg="#00ff00")

label1To=Label(frame, text="to:")
label1To.place(x=189, y=50)
label1To.config(bg="black",fg="#00ff00")
label1To.config(font=('Comic Sans MS',13,"bold"))
rlecon1 = Entry(frame, bd=2)
rlecon1.place(x=220, y=45)
rlecon1.config(bg="black", fg="#00ff00")



#rule2 settings
label2=Label(frame, text="Rule2:")
label2.place(x=22 ,y=80)
label2.config(bg="black",fg="#00ff00")
label2.config(font=('Comic Sans MS',13,"bold"))
rle2 = Entry(frame, bd=2, width=10)
rle2.place(x=82, y=75)
rle2.config(bg="black", fg="#00ff00")
label2To=Label(frame, text="to:")
label2To.place(x=189, y=80)
label2To.config(bg="black",fg="#00ff00")
label2To.config(font=('Comic Sans MS',13,"bold"))
rlecon2 = Entry(frame, bd=2)
rlecon2.place(x=220, y=75)
rlecon2.config(bg="black", fg="#00ff00")

#rule 3 settings
label3=Label(frame, text="Rule3:")
label3.place(x=22 ,y=110)
label3.config(bg="black",fg="#00ff00")
label3.config(font=('Comic Sans MS',13,"bold"))
rle3 = Entry(frame, bd=2, width=10)
rle3.place(x=82, y=105)
rle3.config(bg="black", fg="#00ff00")
label3To=Label(frame, text="to:")
label3To.place(x=189, y=110)
label3To.config(bg="black",fg="#00ff00")
label3To.config(font=('Comic Sans MS',13,"bold"))
rlecon3 = Entry(frame, bd=2)
rlecon3.place(x=220, y=105)
rlecon3.config(bg="black", fg="#00ff00")


#Generation settings
gen3=Label(frame, text="Level:")
gen3.place(x=22, y=140)
gen3.config(bg="black",fg="#00ff00")
gen3.config(font=('Comic Sans MS',13,"bold"))
gen = Entry(frame, bd=2, width=5)
gen.config(bg="black", fg="#00ff00")
gen.place(x=82, y=135)

#segment settings
segmentLabel=Label(frame, text="Segment:")
segmentLabel.place(x=10, y=170)
segmentLabel.config(bg="black",fg="#00ff00")
segmentLabel.config(font=('Comic Sans MS',13,"bold"))
segment = Entry(frame, bd=2, width=8)
segment.place(x=82, y=165)
segment.config(bg="black", fg="#00ff00")

#Angle settings
angleLabel=Label(frame, text="Angle:")
angleLabel.place(x=22, y=200)
angleLabel.config(bg="black",fg="#00ff00")
angleLabel.config(font=('Comic Sans MS',13,"bold"))
angle = Entry(frame, bd=2, width=8)
angle.place(x=82, y=195)
angle.config(bg="black", fg="#00ff00")

#name
Vural=Label(frame, text="Vural Erdogan")
Vural.place(x=50 ,y=750)
Vural.config(bg="black",fg="cyan")
Vural.config(font=('Comic Sans MS',20))

#Functions

#compare function helps to generate previous L system.
def compare():
    # clearing boxes

    text=combo.get()
    axe.delete(0, END)
    rle1.delete(0, END)
    rlecon1.delete(0, END)
    rle2.delete(0, END)
    rlecon2.delete(0, END)
    rle3.delete(0, END)
    rlecon3.delete(0, END)
    gen.delete(0, END)
    segment.delete(0, END)
    angle.delete(0, END)

    #calling ready methods

    if (text== 'Sierpinsky'):
        axe.insert(0, 'F')
        rle1.insert(0, 'F')
        rlecon1.insert(0,'Y-F-Y')
        rle2.insert(0, 'Y')
        rlecon2.insert(0, 'F+Y+F')
        segment.insert(0, '5')
        angle.insert(0, '60')
        gen.insert(0, '5')
    if (text=='Koch'):
        axe.insert(0, 'F')
        rle1.insert(0, 'F')
        rlecon1.insert(0, 'F-F++F-F')
        gen.insert(0, '5')
        segment.insert(0, '5')
        angle.insert(0, '60')
    if (text=='Square'):
        axe.insert(0, 'F')
        rle1.insert(0, 'F')
        rlecon1.insert(0, 'F-F+F+F-F')
        gen.insert(0, '5')
        segment.insert(0, '5')
        angle.insert(0, '90')
    if (text=='Plant'):
        axe.insert(0, 'Y')
        rle1.insert(0, 'Y')
        rlecon1.insert(0, 'F-[[Y]+Y]+F[+FY]-Y')
        rle2.insert(0, 'F')
        rlecon2.insert(0, 'FF')
        gen.insert(0, '5')
        segment.insert(0, '5')
        angle.insert(0, '25')
    if (text=='Fibonacci'):
        axe.insert(0, 'Y')
        rle1.insert(0, 'F')
        rlecon1.insert(0, 'FF')
        rle2.insert(0, 'Y')
        rlecon2.insert(0, 'F[-Y]+Y')
        gen.insert(0, '5')
        segment.insert(0, '5')
        angle.insert(0, '30')
    if (text=='Dcurve'):
        axe.insert(0, 'FV')
        rle1.insert(0, 'V')
        rlecon1.insert(0, 'V+YF')
        rle2.insert(0, 'Y')
        rlecon2.insert(0, 'FV-Y')
        gen.insert(0, '5')
        segment.insert(0, '5')
        angle.insert(0, '90')
    if (text=='ArrowPlant'):
        axe.insert(0, 'X')
        rle1.insert(0, 'X')
        rlecon1.insert(0, 'F[+X][-X]FX')
        rle2.insert(0, 'F')
        rlecon2.insert(0, 'FF')
        gen.insert(0, '7')
        segment.insert(0, '3')
        angle.insert(0, '25.7')
    if (text=='Plant2'):
        axe.insert(0, 'X')
        rle1.insert(0, 'X')
        rlecon1.insert(0, 'F[+X]F[-X]+X')
        rle2.insert(0, 'F')
        rlecon2.insert(0, 'FF')
        gen.insert(0, '7')
        segment.insert(0, '4')
        angle.insert(0, '20')
    if (text=='CoolPlant'):
        axe.insert(0, 'F')
        rle1.insert(0, 'F')
        rlecon1.insert(0, 'FF-[-F+F+F]+[+F-F-F]')
        gen.insert(0, '4')
        segment.insert(0, '4')
        angle.insert(0, '22.5')
    if (text=='CurlyPlant'):
        axe.insert(0, 'F')
        rle1.insert(0, 'F')
        rlecon1.insert(0, 'F[+F]F[-F][F]')
        gen.insert(0, '4')
        segment.insert(0, '5')
        angle.insert(0, '20')

#change background of Turtle screen
def changecolour():
    screen.bgcolor(str(combo2.get()))

#restart the GUI
def restart():

    gui = sys.executable
    os.execl(gui, gui, * sys.argv)


#rulefinder finds the rule by obtaining from last generations : Glast and Glast-1
def rulefinder():
    global externalrul1
    global externalrul2

    # The size of your "expanding permutations"
    if len(rlecon1.get())>=len(rlecon2.get()):
        n = len(rlecon1.get())+1
    elif len(rlecon2.get()) > len(rlecon1.get()):
        n = len(rlecon2.get())+1

    res = []
    for i in range(1, n):
        res.extend(map(''.join, list(itertools.product(uniquestring1, repeat=i))))
    print(res)

    for y in range(0,len(res)):
        rul2 = res[y]
        for x in  range(0,len(res)):
                    rul1 = res[x]
                    code = ""
                    for cha in Genx1:

                        if cha==uniquestring1[0]:
                            code +=codereplacer(rul1)
                        elif cha==uniquestring1[1]:
                            code +=codereplacer(rul2)
                    print(code)
                    print(uniquestring1[0],rul1)
                    print(uniquestring1[1],rul2)
                    print(LastString)
                    if code == LastString:
                        axiom1=uniquestring1[0]
                        axiom2=uniquestring1[1]
                        externalrul1=rul1
                        externalrul2=rul2
                        print('rules are found')
                        print("First RULE:", uniquestring1[0], rul1)
                        print("Second RULE:", uniquestring1[1], rul2)
                        findsubgeneration(code, axiom1, externalrul1, axiom2, externalrul2)
                        return

#findsubgeneration finds previous generations untill finds the axiom of rule.
def findsubgeneration(generation, ax1, rul1, ax2, rul2):
    nextgeneration = ''
    i = 0
    state1 = 0

    while (i < (len(generation))):

        if generation[i:i + len(rul1)] == rul1:
            nextgeneration = nextgeneration + ax1
            i = i + len(rul1)
            state1=1
        elif generation[i:i + len(rul2)] == rul2:
            nextgeneration = nextgeneration + ax2
            i = i + len(rul2)
            state1=2
        else:
            if  state1==1  :
                nextgeneration = nextgeneration[:-len(ax1)]+''
                i = i - len(rul1)

            elif state1==2  :
                nextgeneration = nextgeneration[:-len(ax2)]+''
                i = i - len(rul2)
            swaprules = rul1
            rul1 = rul2
            rul2 = swaprules
            swapax = ax1
            ax1 = ax2
            ax2= swapax
            state1 = 0

    if (len(rul1) > len(nextgeneration)) or (len(rul2) > len(nextgeneration)):
        print ('Generation number:'+ str(z))
        print('Axoim:' + nextgeneration)
        return nextgeneration
    else:

      print('Generations:'+ nextgeneration)
      findsubgeneration(nextgeneration, ax1, rul1, ax2, rul2)

#codereplacer adds new character to old string
def codereplacer(rules):
    NewString=""
    NewString = NewString + rules
    return NewString

#cyphersolver reveals the cypher by comparing hidden message with L-system generated message.
def cyphersolver(word1,word2):

    word1 = ''.join(x for x, y in zip(word1, word2) if x != y)
    print("Message has been found:" + word1)
    return word1

#createmessage enables an user to enter a message and hide it.
def createmessage(allchas):


    global cypher
    cypher=""
    s=''
    msg = input('SECRET MESSAGE: ')
    randomarray=[]
    for char in msg:
        print(MORSE[char.upper()])
        s= s + MORSE[char.upper()]
        s= s + '.'

    print ('Translation:' + s)
    print('message is encrypting...Please wait...')
    codelist = list(allchas)
    x=0
    randomarray = random.sample(range(1, len(codelist) - len(Genx1) - len(Genx2)), len(s))


    while (x < len(s)):
        randomarray.sort()

        if (s[x]=='A' ) :
            if (codelist[randomarray[x]]=='B'):

                codelist[randomarray[x]] = s[x]
                x = x + 1
            else:
                randomarray[x] = randomarray[x] + 1
        elif (s[x]=='B' ) :
            if (codelist[randomarray[x]]=='A'):
                codelist[randomarray[x]] = s[x]
                x = x + 1
            else:
                randomarray[x] = randomarray[x] + 1
        elif (s[x]=='.'):
            codelist[randomarray[x]]=' '
            x= x + 1



    allchas = "".join(codelist)
    cypher=allchas
    T.insert(END,'Message is uploaded:'+ cypher)
    T.yview_pickplace("end")


#finds message in the encrypted code.
def findmessage():
    x=''
    thesecretcode =""
    secretarray=[]
    thesecretcode = cyphersolver(cypher, Message)
    secretarray = thesecretcode.split()
    for char in secretarray:
        print(InvMorse[char.upper()])
        x = x + InvMorse[char.upper()]

    print (x)

# a simple word adder
def sum(Wordsum,Generation):

    return Wordsum + Generation

#decypher reveals the details of generations.
def decypher():
    global uniquecount2, uniquecount1
    #1
    uniquecount1 = len(uniquestring1)
    print('Gen1:')
    print(*Genx1)
    n=""
    n +='Unique cha counts:' + str(uniquecount1)+ "\n"
    n += str(uniquestring1) +"\n"
    for cha in uniquestring1:
        n += cha + ':' + str(Genx1.count(cha)) + "\n"
    T.insert(END, n)
    #2
    uniquecount2 = len(uniquestring2)
    print('Gen2:')
    print(*Genx2)
    m=""
    m +='Unique cha counts:' + str(uniquecount2) + "\n"
    m += str(uniquestring2) + "\n"
    for cha2 in uniquestring2:
        m += cha2 + ':' + str(Genx2.count(cha2)) + "\n"
    T.insert(END, m)
    T.yview_pickplace("end")


#convert function changes the characters to the rules. E.g. A ---> AB
def Convert(String):
    convertedString = ""
    if String == rle1.get() :
        rule1 = rlecon1.get()
        convertedString = rule1
    elif String == rle2.get():
        rule2 = rlecon2.get()
        convertedString = rule2
    elif String == rle3.get():
        rule3 = rlecon3.get()
        convertedString = rule3
    else: convertedString=String
    return convertedString

#string adder
def AddingToNewString(changingString):
    NewString = ""

    for character in changingString:
        NewString = NewString + Convert(character)
    return NewString

#creator function creates L-system strings.
def CreatorFunction(Generation, axiom):

    global LastString
    global Message
    global Genx1, StringCount1, uniquestring1
    global Genx2, StringCount2, uniquestring2
    Message = ""
    LastString = ""

    for x in range(1, Generation+1):

        LastString = AddingToNewString(axiom)
        axiom = LastString
        Message=sum(Message,LastString)
        s ="G" + str(x) + ":" + LastString + "\n" + 'Character Count:' + str(len(LastString)) + "\n"

        if x==Generation-1:
            Genx1=list(LastString)
            uniquestring1 = list(set(LastString))

        if x==Generation:
            Genx2=list(LastString)
            uniquestring2 = list(set(LastString))

        T.insert(END, s)
    return LastString


def drawFunction(rules, angle, segment, Turt, canvsizew, canvsizeh):

        location=[]
        Turt.hideturtle()
        Turt.setheading(90)
        Turt.back(1)
        Turt.speed(0)

        #turtle colours arrays
        colours=["#BFFF00", "#00CC00", "white", "#FFFF00"]
        set2=['green3','green2', '#4CC417']
        set1=['#4CC417','yellow2']
        green=['yellow2']

        y=0
        x=0
        for cha in rules:
            if  abs(2*Turt.ycor())> canvsizeh:
                canvsizeh +=300
                cv.reset(canvheight=canvsizeh)
                cv.yview_moveto(-(Turt.ycor()))


            if abs(2 * Turt.xcor())>canvsizew:
                canvsizew += 300
                cv.reset(canvwidth=canvsizew)
                cv.xview_moveto((Turt.xcor()))

            if cha == 'F':
                Turt.forward(segment)
                x = x + 1
                x = x % 3
                Turt.forward(segment)
                Turt.color(set2[x])
            elif cha=='Y':
                y = y + 1
                y = y % 2
                Turt.forward(segment)
                Turt.color(set1[y])
            elif cha == 'X':
                Turt.backward(segment)
            elif cha == '[':
                location.append((Turt.heading(), Turt.pos()))
            elif cha == ']':
                heading, position = location.pop()
                Turt.penup()
                Turt.goto(position)
                Turt.setheading(heading)
                Turt.pendown()
            elif cha == '+':
                Turt.right(angle)
            elif cha == '-':
                Turt.left(angle)

# 'AddingtoNewString', 'CreatorFunction', 'DrawFunction' and 'Convert' inpired by below website.
# http://interactivepython.org/courselib/static/thinkcspy/Strings/TurtlesandStringsandLSystems.html

#Buttons
print1 = Button(frame, text="Print",borderwidth=5, command=lambda: CreatorFunction(int(gen.get()), str(axe.get())))
print1.place(x=35, y=250)
print1.config(highlightbackground='black')

quit1 = Button(frame, text="Exit", command=lambda:quit())
quit1.place(x=220, y=250)
quit1.config(highlightbackground='black')

clear2 = Button(frame, text="Clear Text", command=lambda: T.delete('1.0', END))
clear2.place(x=390, y=750)
clear2.config(highlightbackground='black')

clear1 = Button(frame, text="Clear Screen", command=lambda: screen.resetscreen())
clear1.place(x=380, y=490)
clear1.config(highlightbackground='black')

Draw1 = Button(frame, text="Draw!", command=lambda:drawFunction(CreatorFunction(int(gen.get()), str(axe.get())), float(angle.get()), float(segment.get()),t, wcanvsize, hcanvsize))
Draw1.place(x=35, y=285)
Draw1.config(highlightbackground='black')

Restart=Button(frame, text="Restart", command=restart)
Restart.place(x=140,y=250)
Restart.config(highlightbackground='black')

combo=ttk.Combobox(MyGUI)
combo.place(x=35, y= 330)
combo['values']=('Koch','Plant','Square','Sierpinsky','Fibonacci','Dcurve', 'ArrowPlant', 'Plant2', 'CoolPlant','CurlyPlant')
combo.current(1)

combo2=ttk.Combobox(MyGUI)
combo2.place(x=35, y= 360)
combo2['values']=('black','white','gray16','gray71','MediumOrchid3','light cyan','wheat1','azure2')
combo2.current(0)


Generate=Button(frame, text="Generate!", command=lambda: compare())
Generate.place(x=280,y=250)
Generate.config(highlightbackground='black')

changebg=Button(frame, text="Change Colour", command=lambda: changecolour())
changebg.place(x=280,y=280)
changebg.config(highlightbackground='black')

Detail=Button(frame, text="Detail", command=lambda: decypher())
Detail.place(x=280,y=310)
Detail.config(highlightbackground='black')

Solve=Button(frame, text="Solve!", command=lambda: rulefinder())
Solve.place(x=280,y=340)
Solve.config(highlightbackground='black')

Upload=Button(frame, text="Encrypt a Message", command=lambda: createmessage(Message))
Upload.place(x=280,y=370)
Upload.config(highlightbackground='black')

FindMessage=Button(frame, text="Decrypt!", command=lambda: findmessage())
FindMessage.place(x=280,y=400)
FindMessage.config(highlightbackground='black')


MyGUI.mainloop()













