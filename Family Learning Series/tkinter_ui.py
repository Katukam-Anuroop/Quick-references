import tkinter as tk
from tkinter import scrolledtext
from gemi_api import send_prompt

root = tk.Tk()
root.geometry("1000x1000")
root.configure(bg="#000000")
root.title("Chat GPT REPLICA")
def send_message():
    prompt = user_input.get()
    print(prompt)
    response = send_prompt(prompt)
    print(response)
    chat_response.insert(tk.END, f"User: {response}\n")
def clear_box():
    chat_response.delete(1.0, tk.END)
    user_input.delete(0, tk.END)

user_input_label = tk.Label(root, text="User Input BOX")
user_input_label.place(x=5, y=5)

user_input = tk.Entry(root,width=100, bg= "#34dbeb")
user_input.place(x=20, y=20)

chat_response = scrolledtext.ScrolledText(root, wrap = tk.WORD, height=20)
chat_response.place(x=10, y=50)

send_button = tk.Button(root, text="Send", width=10,command=send_message)
send_button.place(x=10, y=600)

send_button = tk.Button(root, text="Clear text", width=10,command=clear_box)
send_button.place(x=100, y=600)
root.mainloop()