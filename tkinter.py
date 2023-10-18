import tkinter as tk

def button_click():
    print("Button Clicked!")

window = tk.Tk()
window.title("Tkinter")

button = tk.Button(window, text="Click Me!", command=button_click)

button.pack()

window.mainloop()
