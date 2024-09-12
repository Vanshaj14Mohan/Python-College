#Wap to print a message in a window highlight the message in yellow color
import tkinter as tk 
root = tk.Tk()

root.title("Test 3")
root.geometry("500x700")
root.config(bg="green")

label = tk.Label(root, text="Test 3", font=("Arial", 24), fg="yellow",bg="green") #fg -> font color
label.pack(pady=20)

root.mainloop()