import tkinter as tk

def submit_form():
    name = entry_name.get()
    roll = entry_roll.get()

    if name and roll:
        result_label.config(text="Registration successful!")
        print(name)
        print(roll)
    else:
        result_label.config(text="Please fill in all fields.")

window = tk.Tk()
window.title("Student Registration")

label_name = tk.Label(window, text="Name:")
label_name.pack()

entry_name = tk.Entry(window)
entry_name.pack()

label_roll = tk.Label(window, text="Roll No:")
label_roll.pack()

entry_roll = tk.Entry(window)
entry_roll.pack()

submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.pack()

result_label = tk.Label(window, text="", fg="green")
result_label.pack()

window.mainloop()
