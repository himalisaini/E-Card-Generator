from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
from PIL import ImageGrab

#background gif
class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = Canvas(parent, width=1400, height=1400)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open('images/bggif.gif'))]
        self.image = self.canvas.create_image(700,500, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(100, lambda: self.animate((counter+1) % len(self.sequence)))


    
root = Tk()
root.title('E-Card Generator')
app = App(root)

#Saving Image
def getter(fname,widget,popup,window1):
    popup.destroy()
    time.sleep(5)
    x=window1.winfo_rootx()+widget.winfo_x()
    y=window1.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()
    img=ImageGrab.grab().crop((x,y,x1,y1))
    rgb_im = img.convert('RGB')
    rgb_im.save(fname+'.png')
    label = Label(widget, text="Your Card has been saved successfully please check the current directory !",font=("Comic Sans MS",20))
    label.place(relx=0.25,rely=0.92)
    
 #Pop up box
def popupmsg(canv,l1,popupMenu,popupMenu2,sv,window):
    popup = Tk()
    popup.wm_title("Save Ecard !")
    popup.geometry("300x200")
    l1.place_forget()
    popupMenu2.destroy()
    popupMenu.destroy()
    sv.place_forget()
    label = Label(popup, text="Enter the file name :",font=("Comic Sans MS",20))
    label.pack(side="top", fill="x", pady=10)
    txt = Entry(popup)
    txt.insert(0,"*File Name*")
    txt.place(relx=0.3,rely=0.3)
    B1 = Button(popup, text="Okay", command = lambda: getter(txt.get(),canv,popup,window))
    B1.place(relx=0.4,rely=0.6)
    B1 = Button(popup, text="Cancel", command = popup.destroy)
    B1.place(relx=0.6,rely=0.6)
    popup.mainloop()


#Birthday cards
def birthday_def(name,txt,stat,imagename,title_name):
    window1 = Toplevel(root)
    window1.geometry("1400x1400")
    window1.title(title_name)
    img1 = Image.open('images/'+imagename)
    im1 = ImageTk.PhotoImage(img1)
    c = Canvas(window1,width=1400, height=1400,bg='pink')
    c.pack()
    c.create_image(1200, 10, image=im1,anchor=NE)
    tkvar = StringVar(window1)
    tkvar2 = StringVar(window1)
    
    # Dictionary with options
    choices = { 'Red','Blue','Green','Orange'}
    tkvar.set('Red')
    tkvar2.set('Blue') # set the default option

    popupMenu = OptionMenu(window1, tkvar, *choices)
    popupMenu2 = OptionMenu(window1, tkvar2, *choices)
    l1 = Label(window1, text="Choose a color",font=("Comic Sans MS",15))
    l1.place(relx=0.6,rely=0.375)
    popupMenu.place(relx=0.669,rely=0.375)
    popupMenu2.place(relx=0.669,rely=0.425)

    def change_dropdown(*args):
        x = tkvar.get()
        canvas_text = c.create_text(635, 290, text='', anchor=NW,fill=x,font=("Comic Sans MS",50))

        test_string = name
        #Time delay between chars, in milliseconds
        delta = 700
        delay = 0
        for i in range(len(test_string) + 1):
            s = test_string[:i]
            update_text = lambda s=s: c.itemconfigure(canvas_text, text=s)
            c.after(delay, update_text)
            delay += delta
            
    def change_dropdown2(*args):
        x = tkvar2.get()
        j=0
        if (stat == True):
            canvas_text = c.create_text(580, 380, text=txt, anchor=NW,fill=x,font=("Comic Sans MS",30))
        
        else:
            while(j<=(len(txt)-1)):
                if j==0:
                    canvas_text = c.create_text(480, 380, text=txt[0], anchor=NW,fill=x,font=("Comic Sans MS",30))
                    j = j + 1
                    if(j==len(txt)):
                        break
                if j==1:
                    canvas_text = c.create_text(480, 425, text=txt[1], anchor=NW,fill=x,font=("Comic Sans MS",30))
                    j = j + 1
                    if(j==len(txt)):
                        break
                if j==2:
                    canvas_text = c.create_text(480, 470, text=txt[2], anchor=NW,fill=x,font=("Comic Sans MS",30))
                    j = j + 1
                    if(j==len(txt)):
                        break
                if j==3:
                    canvas_text = c.create_text(480, 505, text=txt[3], anchor=NW,fill=x,font=("Comic Sans MS",30))
                    j = j + 1
                    if(j==len(txt)):
                        break
                if j==4:
                    canvas_text = c.create_text(480, 540, text=txt[4], anchor=NW,fill=x,font=("Comic Sans MS",30))
                    j = j + 1
                    if(j==len(txt)):
                        break
        

    tkvar.trace('w', change_dropdown)
    tkvar2.trace('w', change_dropdown2)
    
    j=0
    if (stat == True):
        canvas_text = c.create_text(580, 380, text=txt, anchor=NW,fill='Blue',font=("Comic Sans MS",30))
    else:
        while(j<=(len(txt)-1)):
            if j==0:
                canvas_text = c.create_text(480, 380, text=txt[0], anchor=NW,fill='Blue',font=("Comic Sans MS",30))
                j = j + 1
                if(j==len(txt)):
                    break
            if j==1:
                canvas_text = c.create_text(480, 425, text=txt[1], anchor=NW,fill='Blue',font=("Comic Sans MS",30))
                j = j + 1
                if(j==len(txt)):
                    break
            if j==2:
                canvas_text = c.create_text(480, 470, text=txt[2], anchor=NW,fill='Blue',font=("Comic Sans MS",30))
                j = j + 1
                if(j==len(txt)):
                    break
            if j==3:
                canvas_text = c.create_text(480, 505, text=txt[3], anchor=NW,fill='Blue',font=("Comic Sans MS",30))
                j = j + 1
                if(j==len(txt)):
                    break
            if j==4:
                canvas_text = c.create_text(480, 540, text=txt[4], anchor=NW,fill='Blue',font=("Comic Sans MS",30))
                j = j + 1
                if(j==len(txt)):
                    break
    
    canvas_text = c.create_text(635, 290, text='', anchor=NW,fill='Red',font=("Comic Sans MS",50))

    test_string = name
        #Time delay between chars, in milliseconds
    delta = 300
    delay = 0
    for i in range(len(test_string) + 1):
        s = test_string[:i]
        update_text = lambda s=s: c.itemconfigure(canvas_text, text=s)
        c.after(delay, update_text)
        delay += delta
        
    sv = Button(window1,text="SAVE",font=("Comic Sans MS",30),command=lambda :popupmsg(c,l1,popupMenu,popupMenu2,sv,window1))
    sv.place(relx=0.5,rely=0.9)
    window1.mainloop()

#Anniversary cards
def anniversary_def(name,txt,stat,imagename,title_name):
    window1 = Toplevel(root)
    window1.geometry("1400x1400")
    window1.title(title_name)
    img1 = Image.open('images/'+imagename)
    im1 = ImageTk.PhotoImage(img1)
    c = Canvas(window1,width=1400, height=1400,bg='pink')
    c.pack()
    c.create_image(1200, 10, image=im1,anchor=NE)
    tkvar = StringVar(window1)
    tkvar2 = StringVar(window1)
    
    # Dictionary with options
    choices = { 'Red','Blue','Green','Orange'}
    tkvar.set('Red')
    tkvar2.set('Blue') # set the default option

    popupMenu = OptionMenu(window1, tkvar, *choices)
    popupMenu2 = OptionMenu(window1, tkvar2, *choices)
    l1 = Label(window1, text="Choose a color",font=("Comic Sans MS",15))
    l1.place(relx=0.75,rely=0.31)
    popupMenu.place(relx=0.75,rely=0.42)
    popupMenu2.place(relx=0.75,rely=0.53)

    def change_dropdown(*args):
        x = tkvar.get()
        canvas_text = c.create_text(875, 290, text='', anchor=NW,fill=x,font=("Comic Sans MS",50))

        test_string = name
        #Time delay between chars, in milliseconds
        delta = 700
        delay = 0
        for i in range(len(test_string) + 1):
            s = test_string[:i]
            update_text = lambda s=s: c.itemconfigure(canvas_text, text=s)
            c.after(delay, update_text)
            delay += delta
            
    def change_dropdown2(*args):
        x = tkvar2.get()
        j=0
        if (stat == True):
            canvas_text = c.create_text(860, 380, text=txt, anchor=NW,fill=x,font=("Comic Sans MS",30))
        
        else:
            while(j<=(len(txt)-1)):
                if j==0:
                    canvas_text = c.create_text(480, 380, text=txt[0], anchor=NW,fill=x,font=("Comic Sans MS",30))
                    j = j + 1
                    if(j==len(txt)):
                        break
                if j==1:
                    canvas_text = c.create_text(480, 425, text=txt[1], anchor=NW,fill=x,font=("Comic Sans MS",30))
                    j = j + 1
                    if(j==len(txt)):
                        break
                if j==2:
                    canvas_text = c.create_text(480, 470, text=txt[2], anchor=NW,fill=x,font=("Comic Sans MS",30))
                    j = j + 1
                    if(j==len(txt)):
                        break
                if j==3:
                    canvas_text = c.create_text(480, 505, text=txt[3], anchor=NW,fill=x,font=("Comic Sans MS",30))
                    j = j + 1
                    if(j==len(txt)):
                        break
                if j==4:
                    canvas_text = c.create_text(480, 540, text=txt[4], anchor=NW,fill=x,font=("Comic Sans MS",30))
                    j = j + 1
                    if(j==len(txt)):
                        break
        

    tkvar.trace('w', change_dropdown)
    tkvar2.trace('w', change_dropdown2)
    
    j=0
    if (stat == True):
        canvas_text = c.create_text(860, 380, text=txt, anchor=NW,fill='Blue',font=("Comic Sans MS",30))
    else:
        while(j<=(len(txt)-1)):
            if j==0:
                canvas_text = c.create_text(480, 380, text=txt[0], anchor=NW,fill='Blue',font=("Comic Sans MS",30))
                j = j + 1
                if(j==len(txt)):
                    break
            if j==1:
                canvas_text = c.create_text(480, 425, text=txt[1], anchor=NW,fill='Blue',font=("Comic Sans MS",30))
                j = j + 1
                if(j==len(txt)):
                    break
            if j==2:
                canvas_text = c.create_text(480, 470, text=txt[2], anchor=NW,fill='Blue',font=("Comic Sans MS",30))
                j = j + 1
                if(j==len(txt)):
                    break
            if j==3:
                canvas_text = c.create_text(480, 505, text=txt[3], anchor=NW,fill='Blue',font=("Comic Sans MS",30))
                j = j + 1
                if(j==len(txt)):
                    break
            if j==4:
                canvas_text = c.create_text(480, 540, text=txt[4], anchor=NW,fill='Blue',font=("Comic Sans MS",30))
                j = j + 1
                if(j==len(txt)):
                    break
    
    canvas_text = c.create_text(875,290, text='', anchor=NW,fill='Red',font=("Comic Sans MS",50))

    test_string = name
        #Time delay between chars, in milliseconds
    delta = 300
    delay = 0
    for i in range(len(test_string) + 1):
        s = test_string[:i]
        update_text = lambda s=s: c.itemconfigure(canvas_text, text=s)
        c.after(delay, update_text)
        delay += delta
        
    sv = Button(window1,text="SAVE",font=("Comic Sans MS",30),command=lambda :popupmsg(c,l1,popupMenu,popupMenu2,sv,window1))
    sv.place(relx=0.5,rely=0.9)
    window1.mainloop()

#Anniversary Main Menu
def anniversary(subim1,subim2,subim3,imgname1,imgname2,imgname3,title_name):
    window = Toplevel(root)
    window.geometry("1400x1400")
    window.title(title_name)
    lab = Label(window,bg="#ff6666")
    lab.place(relwidth=1,relheight=1)
    heading = Label(window,text="Choose a template :",fg="white",bg="#ff6666",font=("Comic Sans MS", 30))
    heading.place(relx = 0.45,rely =0.05)

    img1 = Image.open('images/'+subim1)
    im1 = ImageTk.PhotoImage(img1)
    img2 = Image.open('images/'+subim2)
    im2 = ImageTk.PhotoImage(img2)
    img3 = Image.open('images/'+subim3)
    im3 = ImageTk.PhotoImage(img3)
    
    def details(x):
        t1.place_forget()
        t2.place_forget()
        t3.place_forget()
        heading.place_forget()
        
        
        h1 = Label(window,text="Step 1 : Enter the name ",fg="white",bg="#ff6666",font=("Comic Sans MS", 30))
        h1.place(relx = 0.4,rely =0.4)
        display = Entry(window)
        display.insert(0,"*Name*")
        display.place(relx=0.47,rely=0.5)
        
        
        
        h1 = Label(window,text="Step 2 : Enter the message ",fg="white",bg="#ff6666",font=("Comic Sans MS", 30))
        h1.place(relx = 0.4,rely =0.65)
        display2 = Entry(window)
        display2.insert(0,"*Sample Text Message*")
        display2.place(relx=0.47,rely=0.75)
        
        if x==1:
            pic1 = Button(window,image=im1)
            pic1.place(relx=0.4,rely=0.05,relheight=0.25,relwidth=0.25)
            
        elif x==2:
            pic2 = Button(window,image=im2)
            pic2.place(relx=0.4,rely=0.05,relheight=0.25,relwidth=0.25)
            
        else:
            pic3 = Button(window,image=im3)
            pic3.place(relx=0.4,rely=0.05,relheight=0.25,relwidth=0.25)
            
        
        def name_func(x):
            name = display.get()
            
            txt = display2.get()
            res = txt.split()
            

            c = 1
            set = []
            word =''
            
            if len(res)<9:
                set = txt
                stat = True
            else:
                stat = False
                for i in res:
                    if(c%9 !=0):
                        word = word +" "+ i
                        c = c + 1

                    if(c%9 == 0):
                        set.append(word)
                        word = ''
                        c = c + 1
            
           
            if x==1:
                save = Button(window,text="Generate Ecard",font=("Comic Sans MS",20),command=lambda : anniversary_def(name,set,stat,imgname1,title_name))
                save.place(relx=0.47,rely=0.9)
            elif x==2:
                
                save = Button(window,text="Generate Ecard",font=("Comic Sans MS",20),command=lambda : anniversary_def(name,set,stat,imgname2,title_name))
                save.place(relx=0.47,rely=0.9)
                
            else:
                
                save = Button(window,text="Generate Ecard",font=("Comic Sans MS",20),command=lambda : anniversary_def(name,set,stat,imgname3,title_name))
                save.place(relx=0.47,rely=0.9)
            
        
            
        
        but1 = Button(window,text="Done",font=("Comic Sans MS",15),command=lambda : name_func(x))
        but1.place(relx=0.51,rely=0.84)
        
        
        
        
        
        

        
    t1 = Button(window,image=im1,command=lambda : details(1))
    t1.place(relx=0.1,rely=0.2,relheight=0.25,relwidth=0.25)
    t2 = Button(window,image=im2,command=lambda : details(2))
    t2.place(relx=0.4,rely=0.4,relheight=0.25,relwidth=0.25)
    t3 = Button(window,image=im3,command=lambda : details(3))
    t3.place(relx=0.7,rely=0.6,relheight=0.25,relwidth=0.25)

    
        
    window.mainloop()

#End of Anniversary



#Birthday Main Menu
def birthday(subim1,subim2,subim3,imgname1,imgname2,imgname3,title_name):
    window = Toplevel(root)
    window.geometry("1400x1400")
    window.title(title_name)
    lab = Label(window,bg="#ff6666")
    lab.place(relwidth=1,relheight=1)
    heading = Label(window,text="Choose a template :",fg="white",bg="#ff6666",font=("Comic Sans MS", 30))
    heading.place(relx = 0.45,rely =0.05)

    img1 = Image.open('images/'+subim1)
    im1 = ImageTk.PhotoImage(img1)
    img2 = Image.open('images/'+subim2)
    im2 = ImageTk.PhotoImage(img2)
    img3 = Image.open('images/'+subim3)
    im3 = ImageTk.PhotoImage(img3)
    
    def details(x):
        t1.place_forget()
        t2.place_forget()
        t3.place_forget()
        heading.place_forget()
        
        
        h1 = Label(window,text="Step 1 : Enter the name ",fg="white",bg="#ff6666",font=("Comic Sans MS", 30))
        h1.place(relx = 0.4,rely =0.4)
        display = Entry(window)
        display.insert(0,"*Name*")
        display.place(relx=0.47,rely=0.5)
        
        
        
        h1 = Label(window,text="Step 2 : Enter the message ",fg="white",bg="#ff6666",font=("Comic Sans MS", 30))
        h1.place(relx = 0.4,rely =0.65)
        display2 = Entry(window)
        display2.insert(0,"*Sample Text Message*")
        display2.place(relx=0.47,rely=0.75)
        
        if x==1:
            pic1 = Button(window,image=im1)
            pic1.place(relx=0.4,rely=0.05,relheight=0.25,relwidth=0.25)
            
        elif x==2:
            pic2 = Button(window,image=im2)
            pic2.place(relx=0.4,rely=0.05,relheight=0.25,relwidth=0.25)
            
        else:
            pic3 = Button(window,image=im3)
            pic3.place(relx=0.4,rely=0.05,relheight=0.25,relwidth=0.25)
            
        
        def name_func(x):
            name = display.get()
            
            txt = display2.get()
            res = txt.split()
            

            c = 1
            set = []
            word =''
            
            if len(res)<9:
                set = txt
                stat = True
            else:
                stat = False
                for i in res:
                    if(c%9 !=0):
                        word = word +" "+ i
                        c = c + 1

                    if(c%9 == 0):
                        set.append(word)
                        word = ''
                        c = c + 1
            
           
            if x==1:
                save = Button(window,text="Generate Ecard",font=("Comic Sans MS",20),command=lambda : birthday_def(name,set,stat,imgname1,title_name))
                save.place(relx=0.47,rely=0.9)
            elif x==2:
                
                save = Button(window,text="Generate Ecard",font=("Comic Sans MS",20),command=lambda : birthday_def(name,set,stat,imgname2,title_name))
                save.place(relx=0.47,rely=0.9)
                
            else:
                
                save = Button(window,text="Generate Ecard",font=("Comic Sans MS",20),command=lambda : birthday_def(name,set,stat,imgname3,title_name))
                save.place(relx=0.47,rely=0.9)
            
        
            
        
        but1 = Button(window,text="Done",font=("Comic Sans MS",15),command=lambda : name_func(x))
        but1.place(relx=0.51,rely=0.84)
        
        
        
        
        
        

        
    t1 = Button(window,image=im1,command=lambda : details(1))
    t1.place(relx=0.1,rely=0.2,relheight=0.25,relwidth=0.25)
    t2 = Button(window,image=im2,command=lambda : details(2))
    t2.place(relx=0.4,rely=0.4,relheight=0.25,relwidth=0.25)
    t3 = Button(window,image=im3,command=lambda : details(3))
    t3.place(relx=0.7,rely=0.6,relheight=0.25,relwidth=0.25)

    
        
    window.mainloop()

#End of Birthday




#Home Window
def start():

    heading1 = Label(frame2,text="Select a category :",fg="#ff6666",font=("Comic Sans MS", 30),bg="#F3D8F5")
    heading1.place(relx=0.5,rely=0.5,relwidth=0.6,relheight=0.2,anchor='n')

#buttons for selecting category

    Button(frame2,text="Birthday",fg="pink",bg="blue",font=("Comic Sans MS",20), command=lambda : birthday('birth1.jpg','birth2.jpg','birth3.jpg','birthday1.jpg','birthday2.jpg','birthday3.jpg','Birthday')).place(relx=0.3,rely=0.75)
    Button(frame2,text="Anniversary",fg="pink",bg="blue",font=("Comic Sans MS",20), command=lambda : anniversary('ann1.jpg','ann2.jpg','ann3.jpg','anniversary1.jpg','anniversary2.jpg','anniversary3.jpg','Anniversary')).place(relx=0.65,rely=0.75)
    Button(frame2,text="Diwali",fg="pink",bg="blue",font=("Comic Sans MS",20), command=lambda : birthday('di1.jpg','di2.jpg','di3.jpg','diwali1.jpg','diwali2.jpg','diwali3.jpg','Diwali')).place(relx=0.3,rely=0.9)
    Button(frame2,text="New Year",fg="pink",bg="blue",font=("Comic Sans MS",20), command=lambda : birthday('hny1.jpg','hny2.jpg','hny3.jpg','newyear1.jpg','newyear2.jpg','newyear3.jpg','New Year')).place(relx=0.65,rely=0.9)
    
    
    
#heading frame
frame1 = Frame(root,bg="#F3D8F5")
frame1.place(relx = 0.25 , rely = 0.05 , relwidth = 0.48 , relheight = 0.15)


heading1 = Label(frame1,text="E-Card Generator",fg="#ff6666",font=("Comic Sans MS", 50),bg="#F3D8F5")
heading1.place(relx=0.5,rely=0.1,relwidth=0.6,relheight=0.4,anchor='n')


heading2 = Label(frame1,text="Craft Heartfelt Cards for your loved ones",fg="#ff9999",font=("Comic Sans MS", 30),bg="#F3D8F5")
heading2.place(relx=0.5,rely=0.5,relwidth = 0.9 , relheight = 0.5,anchor='n')

#Lower frame
frame2 = Frame(root,bg="#F3D8F5")
frame2.place(relx = 0.05, rely = 0.4 , relwidth = 0.9 , relheight = 0.55)


heading2 = Label(frame2,text="It is moms birthday again and it came up fast.So fast, in fact, that theres no way a greeting card will reach her through the mail in time.\n Thankfully, you dont have to settle for the inevitable belated greeting. \nInstead, you can just make your own eCard for free",fg="purple",font=("Comic Sans MS", 18),bg="#F3D8F5")
heading2.place(relx=0.5,rely=0.05,anchor='n')

Button(frame2,text="Click here to start!",fg="pink",bg="blue",font=("Comic Sans MS",30), command=lambda : start()).place(relx=0.4,rely=0.4)

#End of Home Window



root.mainloop()

