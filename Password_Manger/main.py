from tkinter import *
from tkinter import  messagebox
import random
import  pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    # for char in password_list:
    #   password += char
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    pasword=password_entry.get()
    email=email_entry.get()
    website= website_entry.get()

    if len(pasword)==0 or len(email)==0 or len(website)==0:
        messagebox.showinfo(title='OOPs',message='Please dnt leave filed empty ')
    else:

        is_ok= messagebox.askokcancel(title=website,message=f'Details \n email:{email} \n'
                                                     f'Password:{pasword}\n is it okay')

        if is_ok:
            with open(file='data.txt',mode='a') as data:
                data.write(f'{website} | {email} | {pasword} \n')
                password_entry.delete(0,'end')
                email_entry.delete(0,'end')
                website_entry.delete(0,'end')
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Password Manger')

window.config(padx=20,pady=20,bg='White')

canvas= Canvas(width=200,height=200,highlightthickness=0,bg='White')
logo_img= PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label(text='Website:',bg='White')
website_label.grid(row=1,column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_label = Label(text='Email/Username:',bg='White')
email_label.grid(row=2,column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'tanu@gmail.com')

password_label = Label(text='Password:',bg='White',width=21)
password_label.grid(row=3,column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)


generate_password_button = Button(text='Generate Password',command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button= Button(text='Add',width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()