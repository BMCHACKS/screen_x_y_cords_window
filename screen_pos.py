import pyautogui
import tkinter as tk

def pos(label):
    def update_position():
        x, y = pyautogui.position()
        label.config(text=f"X : {x} | Y : {y}")
        label.after(100, update_position) 

    update_position()


root = tk.Tk()
root.title("Mouse Coords")
root.attributes('-topmost', True)
label = tk.Label(root, text="", font=("Consolas", 16))
label.pack(pady=20, padx=20)

pos(label)
root.mainloop()
