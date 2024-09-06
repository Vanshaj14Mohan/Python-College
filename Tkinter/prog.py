import tkinter as tk

#root window
root= tk.Tk()
#configure root window
root.title("My test case")
root.geometry("400x500") #width & height
root.config(bg="Purple") #change background color

#Adding label to root window
label = tk.Label(root, text="Hello Case", font=("Arial", 24))
label.pack(pady=20)

#Creating button 
def on_button_click():
    label.config(text="Button was Clicked")

button = tk.Button(root, text="Click Here", command=on_button_click)
button.pack(pady=50)

#an exit button
def close_app():
    root.quit()

exit_button = tk.Button(root, text="Exit", command=close_app)
exit_button.pack(pady=10)

root.mainloop()
