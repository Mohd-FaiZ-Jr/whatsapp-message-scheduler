#modules

import pywhatkit
import pyautogui as pg
from tkinter import *
import threading
from PIL import ImageTk,Image
from tkinter import messagebox
import time

#creating loading screen

new = Tk()
new.overrideredirect(True)

new.eval('tk::PlaceWindow . center')

w = 500
h = 300

screen_width = new.winfo_screenwidth()  # Width of the screen
screen_height = new.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (w/ 2)
y = (screen_height / 2) - (h/ 2)

new.geometry('%dx%d+%d+%d' % (w, h, x, y))

#inserting image in background

pic0 = Image.open("images/splash-img.png")
resized0 = pic0.resize((500, 450))
mod_pic0 = ImageTk.PhotoImage(resized0)
Label(new, image=mod_pic0).pack()

image1 = PhotoImage(file='images/loader2.png')
image2 = PhotoImage(file='images/loader1.png')

for i in range(6):

    Label(new,image=image1,border=0,relief=SUNKEN).place(x=210,y=270)
    Label(new, image=image2, border=0, relief=SUNKEN).place(x=230, y=270)
    Label(new, image=image2, border=0, relief=SUNKEN).place(x=250, y=270)
    Label(new, image=image2, border=0, relief=SUNKEN).place(x=270, y=270)
    new.update_idletasks()
    time.sleep(0.5)

    Label(new, image=image2, border=0, relief=SUNKEN).place(x=210, y=270)
    Label(new, image=image1, border=0, relief=SUNKEN).place(x=230, y=270)
    Label(new, image=image2, border=0, relief=SUNKEN).place(x=250, y=270)
    Label(new, image=image2, border=0, relief=SUNKEN).place(x=270, y=270)
    new.update_idletasks()
    time.sleep(0.5)

    Label(new, image=image2, border=0, relief=SUNKEN).place(x=210, y=270)
    Label(new, image=image2, border=0, relief=SUNKEN).place(x=230, y=270)
    Label(new, image=image1, border=0, relief=SUNKEN).place(x=250, y=270)
    Label(new, image=image2, border=0, relief=SUNKEN).place(x=270, y=270)
    new.update_idletasks()
    time.sleep(0.5)

    Label(new, image=image2, border=0, relief=SUNKEN).place(x=210, y=270)
    Label(new, image=image2, border=0, relief=SUNKEN).place(x=230, y=270)
    Label(new, image=image2, border=0, relief=SUNKEN).place(x=250, y=270)
    Label(new, image=image1, border=0, relief=SUNKEN).place(x=270, y=270)
    new.update_idletasks()
    time.sleep(0.5)


def main_window():

    new.destroy()

    win = Tk()
    win.configure(bg="#fff")
    win.geometry("1200x700+380+150")
    win.resizable(False,False)

    win.overrideredirect(True)

    #left side gui

    writeup = Frame(win,width=600,height=700,bg='black',border=0)
    writeup.grid(row=0,column=0)
    head = Label(writeup,text='Welcome',bg='black',fg='white',border=0,font=('Georgia',20,'bold'))
    head.place(x=30,y=40)
    head1 = Label(writeup,text='to Message Scheduler',fg='white',bg='black',border=0,font=('Georgia',20))
    head1.place(x=200,y=40)
    Frame(writeup,width=240,height=6,bg='white').place(x=40,y=80)

    Label(writeup,text="Hello User!!",bg='black',fg='white',border=0,font=('arial',11,'bold')).place(x=20,y=150)
    Label(writeup,text="You might be wandering that what is the use of this GUI?",bg='black',fg='white',border=0,font=('Century',11)).place(x=20,y=210)
    Label(writeup,text="This GUI is build for the people who are hell busy",bg='black',fg='white',border=0,font=('Century',11)).place(x=20,y=250)
    Label(writeup,text="in their work and even forgets to wish their loved one's.",bg='black',fg='white',border=0,font=('Century',11)).place(x=20,y=280)
    Label(writeup,text="This is where my GUI makes your work more easy",bg='black',fg='white',border=0,font=('Century',11)).place(x=20,y=340)
    Label(writeup,text="Just schedule your message and your text ",bg='black',fg='white',border=0,font=('Century',11)).place(x=20,y=370)
    Label(writeup,text="will be sent without any delay!!",bg='black',fg='white',border=0,font=('Century',11)).place(x=20,y=400)
    Label(writeup,text="Here you get a SPAM feature.",bg='black',fg='white',border=0,font=('Century',11)).place(x=20,y=470)
    Label(writeup,text="An additional feature enhancing your experience!!",bg='black',fg='white',border=0,font=('Century',11)).place(x=20,y=500)
    Label(writeup,text="It's better to build yourself rather than copying it from others.",bg='black',fg='white',border=0,font=('Century',11)).place(x=20,y=630)
    Label(writeup,text="Md. Faiz.",bg='black',fg='white',border=0,font=('Century',11)).place(x=20,y=660)

    #right side gui

    Label(win,text='Enter Details.',border=0,fg='dark green',bg='#fff',font=('Agency FB',30)).place(x=620,y=30)

    frame = LabelFrame(win,text='Enter Name',padx=60,pady=5,bg='#fff')
    frame.place(x=670,y=140)
    user = Entry(frame,width=10,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.grid(row=0,column=0)
    user.insert(0,'Name')
    Frame(frame,width=250,height=2,bg='black').place(x=-60,y=30)

    frame2 = LabelFrame(win,text='Enter Number',padx=60,pady=5,bg='#fff')
    frame2.place(x=670,y=230)
    num = Entry(frame2,width=10,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    num.grid(row=0,column=0)
    num.insert(0,'Ph. Number')
    Frame(frame2,width=250,height=2,bg='black').place(x=-60,y=30)

    frame3 = LabelFrame(win,text='Enter Hour',padx=60,pady=5,bg='#fff')
    frame3.place(x=670,y=320)
    hour = Entry(frame3,width=10,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    hour.grid(row=0,column=0)
    hour.insert(0,'Format: hh')
    Frame(frame3,width=250,height=2,bg='black').place(x=-60,y=30)

    frame3 = LabelFrame(win,text='Enter Min',padx=60,pady=5,bg='#fff')
    frame3.place(x=670,y=410)
    min = Entry(frame3,width=10,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    min.grid(row=0,column=0)
    min.insert(0,'Format: mm')
    Frame(frame3,width=250,height=2,bg='black').place(x=-60,y=30)

    frame4 = LabelFrame(win,text='Enter Message',padx=60,pady=5,bg='#fff')
    frame4.place(x=670,y=500)
    msg = Entry(frame4,width=10,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    msg.grid(row=0,column=0)
    msg.insert(0,'Message')
    Frame(frame4,width=250,height=2,bg='black').place(x=-60,y=30)

    #adding images

    im1 = LabelFrame(win,border=0,relief='groove')
    im1.place(x=960,y=-10)
    pic = Image.open("images/img-1.png")
    resized1 = pic.resize((160, 160))
    mod_pic = ImageTk.PhotoImage(resized1)
    fin = Label(im1, image=mod_pic)
    fin.pack()

    im2 = LabelFrame(win,border=0,relief='groove')
    im2.place(x=960,y=190)
    pic2 = Image.open("images/img-2.png")
    resized2 = pic2.resize((160, 160))
    mod_pic2 = ImageTk.PhotoImage(resized2)
    fin2 = Label(im2, image=mod_pic2)
    fin2.pack()

    im3 = LabelFrame(win,border=0,relief='groove')
    im3.place(x=960,y=390)
    pic3 = Image.open("images/img-4.png")
    resized3 = pic3.resize((160, 160))
    mod_pic3 = ImageTk.PhotoImage(resized3)
    fin3 = Label(im3, image=mod_pic3)
    fin3.pack()

    im4 = LabelFrame(win,border=0,relief='groove')
    im4.place(x=960,y=590)
    pic4 = Image.open("images/img-5.jpg")
    resized4 = pic4.resize((160, 160))
    mod_pic4 = ImageTk.PhotoImage(resized4)
    fin4 = Label(im4, image=mod_pic4)
    fin4.pack()

    im5 = LabelFrame(win,border=0,relief='groove')
    im5.place(x=1160,y=150)
    pic5 = Image.open("images/side-dynamic.jpg")
    resized5 = pic5.resize((40, 400))
    mod_pic5 = ImageTk.PhotoImage(resized5)
    fin5 = Label(im5, image=mod_pic5)
    fin5.pack()

    def exitloop():
        win.destroy()

    ig = PhotoImage(file='images/remove.png')
    btn = Button(win,image=ig,width=25,height=25,border=0,command=exitloop)
    btn.place(x=1172,y=0)

    my_string_number = ''

    def main():

        import phonenumbers

        global my_string_number

        # getting input from user

        name = user.get()
        number = num.get()
        time_hour = hour.get()
        time_min = min.get()
        message = msg.get()
        time = time_hour + ":" + time_min

        #errors & messagebox

        h = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
             '21', '22', '23', '24']
        m = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
             '21', '22', '23', '24', '25'
            , '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
             '44', '45', '46', '47', '48', '49',
             '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']

        if (name == '' or number == '' or time_hour == '' or time_min == '' or message == ''):
            messagebox.showerror('Error','Please Enter All Details!!')

        elif (number == 'Ph. Number' or time_hour == "Format: hh" or time_min == 'Format: mm'):
            messagebox.showinfo("Info","First Clear All Data")

        # adding country code to number

        elif len(number) <10:
            messagebox.showerror('Error', 'Enter a Valid Number!!')

        elif len(number) >10:
            messagebox.showerror('Error', 'Enter a Valid Number!!')

        elif len(number) == 10:

            my_string_number = '+91' + ' ' + number
            my_number = phonenumbers.parse(my_string_number)
            st = phonenumbers.is_possible_number(my_number)

            if (st == False):
                messagebox.showerror('Error', 'Enter a Valid Number!!')


            elif (time_hour in h and time_min in m and st == True):

                messagebox.showinfo('Info', "Your message has been scheduled successfully.")

                time_hour = int(hour.get())
                time_min = int(min.get())
                pywhatkit.sendwhatmsg(str(my_string_number), str(message), time_hour=time_hour, time_min=time_min)
                pg.press("Send")

            else:
                messagebox.showerror("Error", "Enter Time In Correct Format")

    def clear():
        user.delete(0,END)
        num.delete(0,END)
        hour.delete(0,END)
        min.delete(0,END)
        msg.delete(0,END)

    def spambtn():

        win.destroy()

        import pyautogui as spam
        import time
        import threading

        global lb

        root = Tk()
        root.title("SPAM")

        root.iconbitmap('images/spam.ico')
        root.geometry("364x990+1540+30")
        root.maxsize(width=364, height=990)
        root.minsize(width=364, height=990)
        root.configure(bg='black')

        im6 = LabelFrame(root, border=0, relief='groove')
        im6.place(x=0, y=0)
        pic6 = Image.open("images/hacker-img.png")
        resized6 = pic6.resize((364, 480))
        mod_pic6 = ImageTk.PhotoImage(resized6)
        fin6 = Label(im6, image=mod_pic6)
        fin6.pack()

        Frame(root, width=8, height=490, bg='black').place(x=0, y=2)
        Frame(root, width=364, height=8, bg='black').place(x=0, y=480)

        Label(root, text="NUMBER OF MESSAGES", fg="white", bg='black', font=('NSimSun', 20)).place(x=30, y=520)
        num = Entry(root, width=35, fg='red', bg='white')
        num.place(x=40, y=580)

        Label(root, text="ENTER YOUR MESSAGE", bg="black", fg="white", font=('NSimSun', 20)).place(x=30, y=640)
        msg = Entry(root, width=35, fg="red", bg='white')
        msg.place(x=40, y=700)

        def spammsg():

            flag = True
            number = num.get()
            message = msg.get()

            if number != '':

                flag = True
                # Applying error - handling method
                try:
                    # try converting to integer
                    int(number)
                except ValueError:
                    flag = False
                    # flag check
                if flag:
                    pass
                else:
                    messagebox.showerror("error", 'Put An Integer In First Field')

            if (number == '' and message != ''):
                messagebox.showerror("Error","Please Fill In Number Of Messages Field")

            elif (number != '' and message == ''):
                messagebox.showerror("Error","Please Fill Message Field!!")

            elif (number == '' or message == ''):
                messagebox.showerror("Error","Please Fill Both The Fields!! ")

            elif (flag == True and message !=''):
                messagebox.showinfo("info","You have 15 to go to your messenger and click.")
                i = 0
                print("You have 15 seconds to go to your messenger and click !")
                time.sleep(15)
                while i < int(number):
                    spam.typewrite(message)
                    spam.press('Enter')
                    i += 1

        Button(root, text="S P A M", padx=50, pady=3, relief='raised', borderwidth=4, bg='red', fg='white', command=lambda: threading.Thread(target=spammsg).start()).place(x=100, y=930)
        Label(root, text="--- SPAM ALERT ---", bg='black', fg='orange', font=('Gabriola', 18, 'bold')).place(x=80,y=760)
        Label(root,text="THIS IS JUST FOR EDUCATIONAL PURPOSE AND FUN\nTHIS IS NOT TO USE FOR HAZARDOUS THINGS\nOR TO HARRASS PEOPLE BY SPAMMING.",bg='black', fg='orange').place(x=5, y=830)
        root.mainloop()

    Button(writeup,width=20,pady=1,text=" S  P  A  M ",font=("Khmer UI",11,'bold'),bg="orange red",fg="white",border=0,relief='flat',borderwidth=2,command=spambtn).place(x=30,y=550)
    Button(win,width=27,pady=7,text="S C H E D U L E",font=("MS Micho",10,'bold'),bg="#57a1f8",fg="white",border=0, relief='groove',borderwidth=2,command=lambda:threading.Thread(target=main).start()).place(x=650,y=645)
    Button(win, width=20, padx=2, pady=2, text="Clear All",bg='#ffdd0b',fg="black", border=0, relief='ridge',borderwidth=1,command=clear).place(x=700, y=590)
    win.mainloop()

new.after(5000, main_window)
mainloop()