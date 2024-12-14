from tkinter import *
import random

host_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
ip_address = '127.0.0.1'

def block():
    website_list = enter_Website.get(1.0, END).strip()
    Website = list(website_list.split(','))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for web in Website:
            if web in file_content:
                print(f"{web} is already blocked.")
            else:
                host_file.write(ip_address + ' ' + web + '\n')
                print(f"{web} has been added to the block list.")

    if Website:
        random_website = random.choice(Website).strip()
        output_label.config(text=f"Website is blocked", fg='red', font=('arial', 20))
        
        print(f"Website {random_website} has been successfully blocked.\n"
              "This is a sample HOSTS file used by Microsoft TCP/IP for Windows.\n"
              "#\n"
              "# This file contains the mappings of IP addresses to host names.\n"
              "# Each entry should be kept on an individual line.\n"
              "# The IP address should be placed in the first column followed by the corresponding host name.\n"
              "#\n"
              "# Example:\n"
              f"127.0.0.1 {random_website}\n"
              "#source server")
        print(f"Website {random_website} has been blocked.\n")

def unblock():
    website_list = enter_Website.get(1.0, END).strip()
    Website = list(website_list.split(','))
    temp_f = ''
    with open(host_path, 'r+') as host_file:
        file_content = host_file.readlines()
        for web in Website:
            if any(web in line for line in file_content):
                print(f"Unblocking {web}...")
                for line in file_content:
                    if web not in line:
                        temp_f += line
                with open(host_path, 'w') as new_file:
                    new_file.write(temp_f)
                print(f"{web} has been removed from the block list.")
            else:
                print(f"{web} is not blocked.")

    if Website:
        random_website = random.choice(Website).strip()
        output_label.config(text=f"Website is unblocked", fg='red', font=('arial', 20))

        print(f"Website {random_website} has been successfully unblocked.\n"
              "This is a sample HOSTS file used by Microsoft TCP/IP for Windows.\n"
              "#\n"
              "# This file contains the mappings of IP addresses to host names.\n"
              "# Each entry should be kept on an individual line.\n"
              "# The IP address should be placed in the first column followed by the corresponding host name.\n"
              "#\n"
              "# Example:\n"
              f"127.0.0.1 {random_website}\n"
              "#source server")
        print(f"Website {random_website} has been unblocked.\n")

def close():
    output_label.config(text="You have Exited the website", fg='red', font=('arial', 20))
    window.after(2000, window.destroy)

window = Tk()
window.geometry('650x400')
window.maxsize(750, 600)
window.minsize(550, 300)
window.title('WEBSITE BLOCKER')

Label(window, text='WEBSITE BLOCKER', font=('bold', 15), fg='black').pack()
Label(window, text='Developed By @B.S.Pandi', font=('bold', 12), fg='black').pack(side=BOTTOM)

Label(window, text='Enter website:').place(x=100, y=50)
enter_Website = Text(window, font=(10), width=30, height=1)
enter_Website.place(x=200, y=48)

Button(window, text='Block', font=('bold', 10), bg='red', fg='white', command=block).place(x=150, y=100)
Button(window, text='Un Block', font=('bold', 10), bg='green', fg='white', command=unblock).place(x=270, y=100)
Button(window, text='Exit', font=('bold', 10), bg='pink', fg='white', command=close).place(x=400, y=100)

output_label = Label(window, text='', font=('arial', 20), fg='red', justify=LEFT)
output_label.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()
