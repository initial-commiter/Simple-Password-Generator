import random
import string
import pyperclip
import tkinter as tk

window = tk.Tk()
window.title(" Simple Password Generator")
app_name = tk.Label(text="""Enter how many characters you want your password to be.
 Longer passwords are more secure.""",
                    font=("Times New Romen", 17),
                    foreground="White",
                    background="black",
                    )
app_name.grid(row=0, column=0)
window.geometry('850x850')
window.config(bg="black")

frame = tk.Frame()
frame.grid()

letters = string.ascii_letters
char = ["!", "@", "%", "&", "+", "=", "*", "?"]


def passwords():
    gen_pass.delete('1.0', "end")
    gen_pass.config(state="normal")
    update = []
    length = int(length_entry.get())
    for x in range(int(length)):
        password = random.choice(random.choice(letters) + random.choice(char) + str(random.randint(0, 9)))
        update.append([password])
        if int(length) > 20 or int(length) <= 5:
            gen_pass.delete('1.0', "end")
            gen_pass.insert("1.0", "Password has to be between 6 and 20 characters long")
            gen_pass.config(state="disabled")
        else:
            gen_pass.delete('1.0', "end")
            gen_pass.config(state="normal")
            gen_pass.insert("1.0", password)
            gen_pass.config(state="disabled")


def copy():
    copier = gen_pass.get(1.0, "end")
    pyperclip.copy(copier)


length_entry = tk.Entry(window, bg="White", width=26, font=("Times New Romen", 20,))
length_entry.grid(row=2, column=0)

gen_btn = tk.Button(window, bg="White", text="Generate", command=passwords)
gen_btn.grid(row=2, column=1)
filler = tk.Label(window, bg="black")
filler.grid(row=3, column=1)

gen_pass = tk.Text(window, bg="white",
                   fg="black",
                   pady=10,
                   padx=10,
                   height=1,
                   width=52,
                   state="normal")
gen_pass.insert("1.0", "click 'Generate' to get password")
gen_pass.grid(row=4, column=0)

copy_password = tk.Button(window, bg="white", text="Click to copy password", padx=10, pady=10, command=copy)
copy_password.grid(row=4, column=1)

window.mainloop()
