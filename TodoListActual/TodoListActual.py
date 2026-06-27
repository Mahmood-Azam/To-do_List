import tkinter as tk
from turtle import save
Tasks=[]



def add_task():
    task=entry.get()
    Tasks.append(task)
    listbox.insert(tk.END,task)
    entry.delete(0,tk.END)


def delete_task():
    selected =listbox.curselection()
    if selected:
        index=selected[0]
        listbox.delete(index)
        Tasks.pop(index)

def Mark_as_done():
    selected= listbox.curselection()
    if selected:
       index= selected[0]
       Tasks[index]= Tasks[index] +" [Done]"
       listbox.delete(index)
       listbox.insert(index , Tasks[index])

def SaveTasks():
    with open("Todo.txt", "w") as f:
        for task in Tasks:
            f.write(task + "\n")

def editTasks():
    selected= listbox.curselection()
    if selected:
        index=selected[0]
        new_Text=entry.get()
        if new_Text:
            Tasks[index]=new_Text 
            listbox.delete(index)
            listbox.insert(index, new_Text)
            entry.delete(0,tk.END)

window = tk.Tk()
window.title("My To-Do List")
window.geometry("400x400")

window.configure(bg="#2b2b2b")
entry=tk.Entry(window, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(window, text= "Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 10))
button.pack(pady=5)

delete_button=tk.Button(window, text="Delete task", command=delete_task,  bg="#4CAF50", fg="white", font=("Arial", 10))
delete_button.pack(pady=5)

Mark_button= tk.Button(window,text="Mark as done", command=Mark_as_done, bg="#4CAF50", fg="white", font=("Arial", 10))
Mark_button.pack(pady=5)

listbox= tk.Listbox(window)
listbox.pack()

edit_button = tk.Button(window, text="Edit Task", command=editTasks, bg="#FF9800", fg="white", font=("Arial", 10))
edit_button.pack(pady=5)

try:
    with open("Todo.txt", "r") as f:
        for line in f:
            task=line.strip()
            Tasks.append(task)
            listbox.insert(tk.END,task)
except FileNotFoundError:
    pass

window.protocol("WM_DELETE_WINDOW", lambda: (SaveTasks(), window.destroy()))
window.mainloop()

