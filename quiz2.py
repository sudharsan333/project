



#-----some imports------
import random,sys
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Separator,Progressbar
from PIL import ImageTk
from tkinter.messagebox import showinfo
from time import time,strftime
import pymysql as sql

#---starting making new window--------
root=Tk()
root.geometry("1350x700+0+0")
root.resizable(0,0)
root.title("QUIZ")

#set an img as icon
img=('wm','iconphoto',root._w,PhotoImage(file="C:\\Users\\Aarthi\\Downloads\\quiz.png"))
root.tk.call(img)
root.config(bg="black")
i=0
timeLeft={'min':5,'sec':10}# 3 total time +30 waiting time for intro
intro='''\t\t :: INSTRUCTIONS ::
1. Total Quiz Time is : 15:00 mins
2.Total Questions : 9
3.Total score : 9
4. Please select appropriate option at once as you have only one chance to select.
   \t\t Good Luck!'''
print(intro)

def timeShow():

  global i,timeLeft
  if timeLeft['min']==5 and timeLeft['sec']>0:
     note.config (text='You can Start Quiz after U Seconds.'.format(timeLeft['sec']))
     timeLeft['sec']-=1
  elif timeLeft['sec']>0:
     submit.config(state=NORMAL)
     instruction.config(text="")
     timeLeft['sec']-=1
     note.config(text='Time Left: ()min:sec()'.format(timeLeft['min'],timeLeft['sec']))
  elif timeLeft['min']!=0 and timeLeft['sec']==0:
      timeLeft['min']-=1
      timeLeft['sec']=59
      note.config(text='Time Left: ()min:sec()'.format(timeLeft['min'],timeLeft['sec']))
  elif timeLeft['min']==0 and timeLeft['sec']==0:
      print('time up! your test is over.')
      result()
  showtime.config(text=strftime('%H:%M:%S'))
  showtime.after(1000,timeShow)
#student details
def getdetails():
    global mainwindow,Name,Roll
    Name=name.get()
    Roll=roll.get()
    root.deiconify()
    timeShow()
    mainwindow.destroy()
def attendance():
    global mainwindow,name,roll,Name,Rollno
    mainwindow=Toplevel(root)
    mainwindow.geometry("1350x700+0+0")
    mainwindow.resizable(0,0)
    mainwindow.title("QUIZ PAGE")
    mainwindow.tk.call(img)
    mainwindow.config(bg='black')
    #appname same as root
    appName=Label(mainwindow,text=title,font=('impact',20,'italic'),
                  justify=CENTER,bg='goldenrod2',fg='white')
   
    appName.pack(side=TOP,fill=BOTH)
    #show current time
    showtime=Label(mainwindow,text='',font=14,fg='red',bg='goldenrod2')
    showtime.place(x=600,y=50)
    #lable to show info of attendence
    info=Label(mainwindow,text='enter your name and roll number',bg='black',fg='goldenrod1',font=('arial',15))
    info.place(x=210,y=200)
    name=Entry(mainwindow,width=30)
    name.place(x=250,y=235)
    roll=Entry(mainwindow,width=30)
    roll.place(x=250,y=260)
 
    submit=Button(mainwindow,text='START',width=15,bg='goldenrod2',fg='green',command=getdetails)
    submit.place(x=265,y=300)
    mainwindow.mainloop()
    #quit game        
def quit_function():                                                            
    answer=showinfo(title="GOOD LUCK",message="Hope you were able to score good mark\n There's always time to take up the course again for better understanding")
    print(answer)
    if answer=='ok':
        sys.exit(root.destroy())
def scorecard():
    global score,top1
    root.withdraw()
    top1=Toplevel(root)
    img=('wm','iconphoto',top1._w,PhotoImage(file="C:\\Users\\Aarthi\\Downloads\\quiz.png"))
    top1.tk.call(img)
    top1.geometry("1350x700+0+0")
    top1.resizable(0,0)
    top1.title("SCORE CARD")
    top1.config(bg='blue')
    top1.protocol('WM_DELETE_WINDOW',quit_function)
    con=sql.connect(host ='localhost',user = 'root',database ='arthi')
    cursor = con.cursor()
    query='SELECT * FROM scores'
    cursor.execute(query)
    rows=cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    frm =Frame(top1)
    frm.pack(side=LEFT, padx=20)
    tv =ttk.Treeview(frm,columns=(1,2,3), show="headings")
    tv.pack()
    tv.heading(1, text="Name")
    tv.heading(2, text="Roll No")
    tv.heading(3, text="Score")
   
    for i in rows:
        tv.insert('', 'end', values=i)
    exitbtn1=Button(top1,text='exit',width=15,bg='black',fg='red',command=quit_function).place(x=350,y=570)

    top1.mainloop()
def disable():
    option1.config(state=DISABLED)
    option2.config(state=DISABLED)
    option3.config(state=DISABLED)
    option4.config(state=DISABLED)
   
def enable():
    option1.config(state=NORMAL)
    option2.config(state=NORMAL)
    option3.config(state=NORMAL)
    option4.config(state=NORMAL)
def result():
    global score
    root.withdraw()
    top=Toplevel(root)
    img=('wm','iconphoto',top._w,PhotoImage(file="C:\\Users\\Aarthi\\Downloads\\quiz.png"))
    top.tk.call(img)
    top.geometry("1350x700+0+0")
    top.resizable(0,0)
    top.title("Result")
    top.config(bg='blue')
    top.protocol('WM_DELETE_WINDOW',quit_function)
    con=sql.connect(host ='localhost',user = 'root',database ='arthi')
    cursor = con.cursor()
    query="INSERT INTO scores (name,roll,score) VALUES (%s,%s,%s)"
    val=(Name,Roll,score)
    cursor.execute(query,val)
    con.commit()
   
    cursor.close()
    con.close()
    label=Label(top,text='quiz over...\nScore:'+str(score),font=15,fg='white',bg='blue').place(x=50,y=25)            
    exitbtn=Button(top,text='exit',width=15,bg='black',fg='red',command=quit_function).place(x=50,y=70)
    viewscore=Button(top,text='view score card',width=15,bg='black',fg='red',command=scorecard).place(x=50,y=120)
    top.mainloop()
                #questions and corresponding answers
questions={'''find the output
               def myfunc(a):
         a = a + 2
 a = a * 2
         return a
      print myfunc(2)''':'8',
             'what will be the output produced by 17%5.0':'2.0',
             'which statement skips the rest of the code and causes the next iteration to take place':'continue',
             'Which of the following is a keyword in Python?':'return',
             'Which of the following is a valid variable name in Python?':'none of the above',
             '''What does the following print?
                x = 10/4
                y = 5/2.0
                print x + y      ''':'5.0',
             '''Write the OUTPUT of the following code segment
                for i in range(1,12):
                   if i%2==0:
                     continue
                print(i)''':'11',
             "Suppose a tuple T is declared as T = (10, 12, 43, 39), which of the following is incorrect?":'T[2]=-29',
             '''What is the output print(type(1/2)''':'<class float>',    

             "what is the output of following code p='welcome to python'\t print(p[::-1])":"nohtyp ot emoclew"}

que=[]
ans=[]
for key,value in questions.items():
        que.append(key)
        ans.append(value)
#corrgsponding answers with answers including at random
options=[
        ['16',ans[0],'6','error'],
        [ans[1],'2','2.5','error'],
        ['break',ans[2],'pass','none of these'],
        ['int', 'float',ans[3],'void'],
        ['do it','doit+2','2do',ans[4]],
        ['4','4.5','7',ans[5]],
        ['12','10','12.5',ans[6]],
        ['print(T[1])','print(max(T))','print(len(T))',ans[7]],
        ['<class int>','0.5','namerror:1/2 not defined',ans[8]],
        ['welcome to python','python to welcome',ans[9],'emoclew ot nohtyp']
        ]

#  

currentQ=''
queNo=None
currentA=""
score=0
qn=1 #for printing no of question finished
var=StringVar ()
def _next ():
  global currentQ,currentA,queNo,score,i,qn,bar
  i=0 # till last question is Left
  if len(que)>0:
    currentQ=random.choice(que)
    print(currentQ)
    q=Label(root,text='Que. '+str(qn),font=('arial',10)).place(x=20,y=80)
    qn+=1
    #que
    queNo=que.index(currentQ) #total questions=5 so queNos =5,queNo 0 means first que
    print(options[queNo])
    currentA=questions[currentQ]
    #firstly change caption of button
    submit.config(text='Next')
    #print current question on quelabel.
    queLabel.config(text=currentQ,fg='green',height=6)
    #print options for question on labels--option 1 option2,.....
    enable()
    option1.config(text=options[queNo][0],bg='sky blue',value=options[queNo][0],bd=1,command=answer)
    option2.config(text=options[queNo][1],bg='sky blue',value=options[queNo][1],bd=1,command=answer)
    option3.config(text=options[queNo][2],bg='sky blue',value=options[queNo][2],bd=1,command=answer)
    option4.config(text=options[queNo][3],bg='sky blue',value=options[queNo][3],bd=1,command=answer)
   
    #remove question from list which are asked
    que.remove(currentQ)
    ans.remove(currentA)
    options.remove(options[queNo])
    if len(que)==0:
      result()
def answer():
  global currentQ,currentA,score
  #essseessss====print selected radiobutton
  a=var.get()
  if currentA==str(a):
    score+=1
    disable()
  else:
    disable()#--------disable all button
   
title='''PYTHON QUIZ FOR BEGINNERS'''
appName=Label(root,text=title,font=('impact',15,'italic'),
              justify=CENTER,bg='goldenrod2',fg='white')
appName.pack(side=TOP,fill=BOTH)

#==== label to show current question

queLabel=Label(root,text='',justify=LEFT,font=20)
queLabel.pack(side=TOP,fill=BOTH)
S=Separator(root).place(x=0,y=195,relwidth=1)

#gwaEocossessessSsssSsssses====options labels
option1=Radiobutton(root,text='',fg='white',bg='black',font=15,width=15,relief=FLAT,indicator=0,value=1,variable=var,bd=0)
option1.place(x=150,y=250)
option2=Radiobutton(root,text='',fg='white',bg='black',font=15,width=15,relief=FLAT,indicator=0,value=2,variable=var,bd=0)
option2.place(x=150,y=300)
option3=Radiobutton(root,text='',fg='white',bg='black',font=15,width=15,relief=FLAT,indicator=0,value=3,variable=var,bd=0)
option3.place(x=150,y=350)
option4=Radiobutton(root,text='',fg='white',bg='black',font=15,width=15,relief=FLAT,indicator=0,value=4,variable=var,bd=0)
option4.place(x=150,y=400)


#instruction of quiz
instruction=Label(root,text=intro,bg='black',fg='white',font=('calibri',15),justify=LEFT)
instruction.place(x=150,y=150)

#note to quiz
note=Label(root,text="",font=('impact',10),bg="black",fg="red")
note.pack(side=BOTTOM)
#---------submit button-----------
submit=Button(root,text="START QUIZ",bg="blue",fg="white",width=15,font=('impact',15),state=DISABLED,command=_next)
submit.pack(side=BOTTOM)
#---------show current time
showtime=Label(root,text="",font=20,fg="black",bg="goldenrod2")
showtime.place(x=620,y=50)

#--------progress bar for time Left question
if __name__=="__main__":
  attendance()
  root.mainloop()

