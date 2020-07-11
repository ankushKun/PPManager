import tkinter as tk
from tkinter import *
import os
import os.path
import random
import ast

## using these characters to generate password ##
letters=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numbers=('1','2','3','4','5','6','7','8','9','0')
chars = ('@','*','_','$')
all_chars=letters+numbers+chars

root = Tk()
root.geometry('600x400')
root.configure(background='gray5')
root.title('Password Manager')
root.resizable(False,False)


stuff={} ## dictionary to store {website:[username,password]} ##

def readfromfile(): ## reads the dictonary from the file ##
    global stuff
    if os.path.exists("./uselessfile.bin"):
        with open('./uselessfile.bin','br') as f:
            s=str(f.read().decode('ascii'))
            if len(s)>0: stuff=ast.literal_eval(s)
    else: writetofile()
    print('READ > '+str(stuff))
        
def writetofile(): ## saves the dictionary to the file ##
    with open('./uselessfile.bin','bw') as f:
        f.write(str(stuff).encode('utf-8'))
        print('WRITE > ',end=' ')
    readfromfile()
    

def create_new(): ## called when user wants to save a new password ##
    def generate(): ## GENERATES A PASSWORD ##
        rnd_letter_lower=random.choice(letters)
        rnd_letter_upper=random.choice(letters).upper()
        rnd_number=random.choice(numbers)
        rnd_char=random.choice(chars)
        t_pass=''
        for x in range(8): t_pass+=random.choice(all_chars)
        f_pass_list = list(t_pass + rnd_letter_lower+rnd_letter_upper+rnd_number+rnd_char)
        random.shuffle(f_pass_list)
        f_pass=''
        for c in f_pass_list: f_pass+=c
        password.set(f_pass)
        
    readfromfile()
            
    def savedata(): ## called when saved button is clicked ##
        if len(website.get())>0 and len(username.get())>0 and len(password.get())>0 :
            if not (website.get().endswith('.com')): website.set(website.get()+'.com')
            stuff[website.get()]=[username.get(),password.get()]
            writetofile()
            done=Toplevel()
            done.title('Done!')
            done.configure(background='gray11')
            done.resizable(False,False)
            Label(done,text='Details Saved',bg="gray11",fg='white',font=('roboto',30)).pack()
            Button(done,text='Ok',font=('roboto',20),command=done.destroy,bg='gray14',fg='white').pack()
            done.mainloop() 
        else :
            err=Toplevel()
            err.title('BAKA!')
            err.configure(background='gray11')
            err.resizable(False,False)
            Label(err,text='Enter all the details first',bg="gray11",fg='white',font=('roboto',30)).pack()
            Button(err,text='Ok',font=('roboto',20),command=err.destroy,bg='gray14',fg='white').pack()
            err.mainloop()
        
    cn=Toplevel()
    cn.title('New Password')
    cn.configure(background='gray8')
    cn.resizable(False,False)
    
    website=StringVar()
    web_label=Label(cn,text='website\n(e.g. youtube.com)',bg='gray8',fg='white',anchor=CENTER,pady=5,padx=10)
    web_label.grid(row=0,column=0)
    web_entry=Entry(cn,textvariable=website,width=45)
    web_entry.grid(row=0,column=1)
    
    username=StringVar()
    username_label=Label(cn,text='username\n(e.g. NoobDeveloper@gmail.com)',bg='gray8',fg='white',anchor=CENTER,pady=5,padx=10)
    username_label.grid(row=1,column=0)
    username_entry=Entry(cn,textvariable=username,width=45)
    username_entry.grid(row=1,column=1)
    
    password=StringVar()
    pass_label=Label(cn,text='password\n(e.g. NoobMaster69)',bg='gray8',fg='white',anchor=CENTER,pady=5,padx=10)
    pass_label.grid(row=2,column=0)
    pass_entry=Entry(cn,textvariable=password,width=45)
    pass_entry.grid(row=2,column=1)
    
    gen=Button(cn,text='Generate',anchor=CENTER,command=generate,bg='gray14',fg='white')
    gen.grid(row=2,column=2,padx=10)
    
    save=Button(cn,text='SAVE',anchor=CENTER,command=savedata,bg='gray14',fg='white')
    save.grid(row=3,column=1,pady=6)
    
    Button(cn,text='Ok',command=cn.destroy,bg='gray14',fg='white').grid(row=4,column=1,pady=6)
    
    
    cn.mainloop()
    
def get_old(): ## called when user wants to retrieve a stored password ##
    def getsaveddata():## called when user clicks the go button ##
        if not (website.get().endswith('.com')): website.set(website.get()+'.com')
        readfromfile()
        if website.get() in stuff :
            data=stuff[website.get()]
            found=Toplevel()
            found.title(website.get())
            found.configure(background='gray11')
            found.resizable(False,False)
            Label(found,text='Username : ',bg="gray11",fg='white',font=('roboto',20)).grid(row=0,column=0,padx=15,pady=15)
            Label(found,text=data[0],bg="gray11",fg='white',font=('roboto',20)).grid(row=0,column=1,padx=15,pady=15)
            Label(found,text='Password : ',bg="gray11",fg='white',font=('roboto',20)).grid(row=1,column=0,padx=15,pady=15)
            Label(found,text=data[1],bg="gray11",fg='white',font=('roboto',20)).grid(row=1,column=1,padx=15,pady=15)
            Button(found,text='Ok',font=('roboto',20),command=found.destroy,bg='gray14',fg='white').grid(row=2,column=2)
            found.mainloop()
        else:
            err=Toplevel()
            err.title('Error 404')
            err.configure(background='gray11')
            err.resizable(False,False)
            Label(err,text='can\'t find that website',bg="gray11",fg='white',font=('roboto',30)).pack()
            Button(err,text='Ok',font=('roboto',20),command=err.destroy,bg='gray14',fg='white').pack()
            err.mainloop()
                
        
    old=Toplevel()
    old.title('Get Saved Passwords')
    old.configure(background='gray8')
    old.resizable(False,False)
    
    website=StringVar()
    web_entry=Entry(old,textvariable=website,width=45)
    web_entry.grid(row=0,column=1)
    web_label=Label(old,text='website\n(e.g. youtube.com)',bg='gray8',fg='white',anchor=CENTER,pady=5,padx=10)
    web_label.grid(row=0,column=0)
    search=Button(old,text='GO',anchor=CENTER,command=getsaveddata,bg='gray14',fg='white')
    search.grid(row=0,column=2,padx=6)
    

logo=Label(text='PASSWORD\nMANAGER',bg='gray5',fg='white',anchor=CENTER,font=('Roboto',40))
logo.place(x=300,y=100,anchor=CENTER)

logo=Label(text='dev : Ankush Tech Creator',bg='gray5',fg='white',anchor=CENTER,font=('Roboto',10))
logo.place(x=50,y=390,anchor=CENTER)

new_pass=Button(text='Store New Password',command=create_new,anchor=CENTER,bg='gray14',fg='white')
new_pass.place(x=300,y=200,anchor=CENTER)

get_pass=Button(text='Retrieve Password',command=get_old,anchor=CENTER,bg='gray14',fg='white')
get_pass.place(x=300,y=250,anchor=CENTER)


root.mainloop()



