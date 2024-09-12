#Wap to create a window of size 80x56  with bg color green text size 56, font-> times new roman  
import tkinter as tk
root = tk.Tk()

root = tk.Tk()

#Step 2configure the root window
root.title("My first GUI App")

root.geometry("400x300") #width x height in pixels

root.title("Test")

root.geometry("800x560") #Size
root.config(bg="green")

label = tk.Label(root, text="CLick",  background="green", font=("Arial", 24))
label.pack(pady=20) #Padding around the label
root.mainloop()

#Wap to create a window with two buttons of any size any color and any style..