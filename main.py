import tkinter as tk

root = tk.Tk()
root.title("My Tkinter App")
root.geometry("400x300") 


label = tk.Label(root, text="Welcome to My App!")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

def on_button_click():
    user_text = entry.get()
    label.config(text=f"Hello, {user_text}!")

button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)


# Run the application
root.mainloop()
