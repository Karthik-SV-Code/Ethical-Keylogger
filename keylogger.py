import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import json
from datetime import datetime

keys_used = []
logging_active = False

# ---------- FUNCTIONS ----------

def generate_json_file():
    with open('key_log.json', 'w') as file:
        json.dump(keys_used, file, indent=4)

def log_key(event):
    global logging_active

    if not logging_active:
        return

    key = event.keysym
    time = datetime.now().strftime("%H:%M:%S")

    log_entry = f"[{time}] Key Pressed: {key}\n"

    # Append to UI
    log_box.insert(END, log_entry)
    log_box.see(END)

    # Store in list
    keys_used.append({"time": time, "key": key})

    generate_json_file()

def start_logging():
    global logging_active
    logging_active = True
    root.bind("<Key>", log_key)
    status_label.config(text="Status: Running", fg="green")

def stop_logging():
    global logging_active
    logging_active = False
    root.unbind("<Key>")
    status_label.config(text="Status: Stopped", fg="red")

def clear_log():
    log_box.delete('1.0', END)

# ---------- UI DESIGN ----------

root = Tk()
root.title("Ethical Keylogger ")
root.geometry("600x450")
root.configure(bg="#1e1e2f")

# Header
header = Label(root, text="Keyboard Activity Monitor",
               font=("Arial", 18, "bold"),
               bg="#1e1e2f", fg="white")
header.pack(pady=10)

# Status
status_label = Label(root, text="Status: Stopped",
                     font=("Arial", 12),
                     bg="#1e1e2f", fg="red")
status_label.pack()

# Frame for log box
frame = Frame(root)
frame.pack(pady=10)

# Scrollable log box
log_box = scrolledtext.ScrolledText(frame,
                                    width=70,
                                    height=15,
                                    font=("Consolas", 10))
log_box.pack()

# Buttons Frame
btn_frame = Frame(root, bg="#53536a")
btn_frame.pack(pady=15)

start_btn = Button(btn_frame, text="Start",
                   command=start_logging,
                   bg="green", fg="white",
                   width=10)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = Button(btn_frame, text="Stop",
                  command=stop_logging,
                  bg="red", fg="white",
                  width=10)
stop_btn.grid(row=0, column=1, padx=10)

clear_btn = Button(btn_frame, text="Clear Log",
                   command=clear_log,
                   bg="orange", fg="black",
                   width=12)
clear_btn.grid(row=0, column=2, padx=10)

# Footer
footer = Label(root,
               text="Type inside this window to log keys",
               bg="#1e1e2f", fg="lightgray")
footer.pack(pady=5)

root.mainloop()