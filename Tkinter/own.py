import tkinter as tk 

# Create root window
root = tk.Tk()

#Creating titile
root.title("MY test case")
#Creating geometry
root.geometry("500x600")

#creating label widget
label = tk.Label(root, text="Hello Guys", font=("Times New Roman", 24), fg="yellow", bg="Green")
label.pack(pady=20)

#Create button widget
def on_click_button():
    label.config(text="Button was clicked")
button = tk.Button(root, text="Click here", command=on_click_button)
button.pack(pady=20)

#Creating main event loop
root.mainloop()
