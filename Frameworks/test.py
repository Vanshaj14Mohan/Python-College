import tkinter as tk

#root window
root = tk.Tk()

#root config
root.title("My task")
root.geometry("500x600")
root.config(bg="blue")

#Creating label
label = tk.Label(root, text="hello guys", font=("Arial", 24), fg="red")
label.pack(pady=50)

#Creating button 
def on_click():
    label.config(text="Button was clicked")

button = tk.Button(root, text="Click here", command=on_click)
button.pack(pady=50)

#Creating exit button
def on_exit():
    root.quit()

exit_button = tk.Button(root,text="Exit Now", command=on_exit)
exit_button.pack(pady=50)

#Creating mainloop
root.mainloop()



