import tkinter as tk
print("Tkinter is available")

#Step 1:create root window
root = tk.Tk()

#Step 2configure the root window
root.title("My first GUI App")

root.geometry("400x300") #width x height in pixels

#Step 3: Create a label widget
label = tk.Label(root, text="Hello, world", font=("Arial", 24))
label.pack(pady=20) #Padding around the label

#Step 4: create button widget
def on_button_click():
    label.config(text="Button Clicked")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

#Step 5: Start the main event loop
root.mainloop()