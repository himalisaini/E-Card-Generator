from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time

#background gif
class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = Canvas(parent, width=1400, height=1400)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open('bggif.gif'))]
        self.image = self.canvas.create_image(700,500, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(100, lambda: self.animate((counter+1) % len(self.sequence)))


    
root = Tk()
app = App(root)





#Birthday Submenus
def birthday1(name,txt):
	window1 = Toplevel(root)
        window1.geometry("1400x1400")
        window1.title("Birthday")
        img1 = Image.open('birthday1.jpg')
        im1 = ImageTk.PhotoImage(img1)
        c = Canvas(window1,width=1400, height=1400,bg='pink')
        c.pack()
        c.create_image(1200, 10, image=im1,anchor=NE)
        tkvar = StringVar(root)
        c1 = 'Red'
        c2 = 'Blue'
        # Dictionary with options
        choices = { 'Red','Blue','Green','Orange'}
        tkvar.set('Red') # set the default option

        popupMenu = OptionMenu(window, tkvar, *choices)
        Label(window, text="Choose a colo").grid(row = 1, column = 1)
        popupMenu.grid(row = 2, column =1)

        # on change dropdown value
        def change_dropdown(*args):
            print( tkvar.get() )
            c1 = tkvar.get()

        # link function to change dropdown
        tkvar.trace('w', change_dropdown)
        #c.create_text(700, 300, text=name,fill=c1,font=("Comic Sans MS",50))
        canvas_text = c.create_text(700, 300, text='', anchor=NW,fill=c1,font=("Comic Sans MS",50))

        test_string = name
        #Time delay between chars, in milliseconds
        delta = 300
        delay = 0
        for i in range(len(test_string) + 1):
            s = test_string[:i]
            update_text = lambda s=s: c.itemconfigure(canvas_text, text=s)
            c.after(delay, update_text)
            delay += delta
        c.create_text(700, 350, text=txt,fill=c2,font=("Comic Sans MS",40))
        window1.mainloop()

def birthday2(name,txt):
	window1 = Toplevel(root)
    	window1.geometry("1400x1400")
    	window1.title("Birthday")
    	img1 = Image.open('birthday2.jpg')
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
            canvas_text = c.create_text(580, 370, text='', anchor=NW,fill=x,font=("Comic Sans MS",35))

            test_string = txt
            #Time delay between chars, in milliseconds
            delta = 300
            delay = 0
            for i in range(len(test_string) + 1):
                s = test_string[:i]
                update_text = lambda s=s: c.itemconfigure(canvas_text, text=s)
                c.after(delay, update_text)
                delay += delta
        

        tkvar.trace('w', change_dropdown)
        tkvar2.trace('w', change_dropdown2)
    
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
        
        canvas_text2 = c.create_text(580,370, text='', anchor=NW,fill='Blue',font=("Comic Sans MS",35))

        test_string2 = txt
        #Time delay between chars, in milliseconds
        delta2 = 300
        delay2 = 0
        for i in range(len(test_string2) + 1):
            s2 = test_string2[:i]
            update_text2 = lambda s2=s2: c.itemconfigure(canvas_text2, text=s2)
            c.after(delay2, update_text2)
            delay2 += delta2
        
        
        def save():
            l1.place_forget()
            popupMenu2.destroy()
            popupMenu.destroy()
            sv.place_forget()
        
        sv = Button(window1,text="SAVE",command=lambda :save())
        sv.place(relx=0.45,rely=0.8)
	window1.mainloop()

def birthday3(name,txt):
	window1 = Toplevel(root)
        window1.geometry("1400x1400")
        window1.title("Birthday")
        img1 = Image.open('birthday3.jpg')
        im1 = ImageTk.PhotoImage(img1)
        c = Canvas(window1,width=1400, height=1400,bg='pink')
        c.pack()
        c.create_image(1200, 10, image=im1,anchor=NE)
        c.create_text(700, 300, text=name,fill=c1,font=("Comic Sans MS",50))
        c.create_text(700, 350, text=txt,fill=c2,font=("Comic Sans MS",40))
    
 
	window1.mainloop()


    
#Birthday Main Menu
def birthday():
    window = Toplevel(root)
    window.geometry("1400x1400")
    window.title("Birthday")
    lab = Label(window,bg="#ff6666")
    lab.place(relwidth=1,relheight=1)
    heading = Label(window,text="Choose a template :",fg="white",bg="#ff6666",font=("Comic Sans MS", 30))
    heading.place(relx = 0.45,rely =0.05)

    img1 = Image.open('birth1.jpg')
    im1 = ImageTk.PhotoImage(img1)
    img2 = Image.open('birth2.jpg')
    im2 = ImageTk.PhotoImage(img2)
    img3 = Image.open('birth3.jpg')
    im3 = ImageTk.PhotoImage(img3)
    
    def details(x):
        t1.place_forget()
        t2.place_forget()
        t3.place_forget()
        heading.place_forget()
        
        
        h1 = Label(window,text="Step 1 : Enter the name ",fg="white",bg="#ff6666",font=("Comic Sans MS", 30))
        h1.place(relx = 0.4,rely =0.4)
        display = Entry(window)
        display.insert(0,"*Himali*")
        display.place(relx=0.4,rely=0.5)
        
        
        
        h1 = Label(window,text="Step 2 : Enter the message ",fg="white",bg="#ff6666",font=("Comic Sans MS", 30))
        h1.place(relx = 0.4,rely =0.65)
        display2 = Entry(window)
        display2.insert(0,"*Sample Text Message*")
        display2.place(relx=0.4,rely=0.75)
        
        name = display.get()
        txt = display2.get()
        
        
        
        if x==1:
            pic1 = Button(window,image=im1)
            pic1.place(relx=0.4,rely=0.05,relheight=0.25,relwidth=0.25)
            save = Button(window,text="Generate Ecard",fg="pink",bg="blue",font=("Comic Sans MS",20),command=lambda : birthday1(name,txt))
            save.place(relx=0.45,rely=0.9)
        elif x==2:
            pic2 = Button(window,image=im2)
            pic2.place(relx=0.4,rely=0.05,relheight=0.25,relwidth=0.25)
            save = Button(window,text="Generate Ecard",fg="pink",bg="blue",font=("Comic Sans MS",20),command=lambda : birthday2(name,txt))
            save.place(relx=0.45,rely=0.9)
            
        else:
            pic3 = Button(window,image=im3)
            pic3.place(relx=0.4,rely=0.05,relheight=0.25,relwidth=0.25)
            save = Button(window,text="Generate Ecard",fg="pink",bg="blue",font=("Comic Sans MS",20),command=lambda : birthday3(name,txt))
            save.place(relx=0.45,rely=0.9)
        

        
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

    Button(frame2,text="Birthday",fg="pink",bg="blue",font=("Comic Sans MS",20), command=lambda : birthday()).place(relx=0.2,rely=0.7)
    Button(frame2,text="Anniversary",fg="pink",bg="blue",font=("Comic Sans MS",20), command=lambda : birthday()).place(relx=0.5,rely=0.7)
    Button(frame2,text="Diwali",fg="pink",bg="blue",font=("Comic Sans MS",20), command=lambda : birthday()).place(relx=0.8,rely=0.7)
    Button(frame2,text="Christmas",fg="pink",bg="blue",font=("Comic Sans MS",20), command=lambda : birthday()).place(relx=0.2,rely=0.85)
    Button(frame2,text="New Year",fg="pink",bg="blue",font=("Comic Sans MS",20), command=lambda : birthday()).place(relx=0.5,rely=0.85)
    Button(frame2,text="Friendship Day",fg="pink",bg="blue",font=("Comic Sans MS",20), command=lambda : birthday()).place(relx=0.8,rely=0.85)
    
    
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
