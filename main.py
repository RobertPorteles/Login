import pickle
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.geometry("300x500")
root.config(bg="Black")
def add_taks():
    task = info.get()
    if task != "":
        lb.insert(tkinter.END,task)
        info.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning", message="You most Enter a task!")
def remove_taks():
    try:
        taks_index =  lb.curselection()[0]
        lb.delete(taks_index)
    except:
        tkinter.messagebox.showwarning(title="warning", message="You most Select a task!")
def load_taks():
    taks = pickle.load(open("taks.dat","rb"))
    lb.delete(0,tkinter.END)
    for taks in taks:
        lb.insert(tkinter.END,taks)

def save_taks():
    taks = lb.get(0, lb.size())
    pickle.dump(taks, open("taks.dat","wb"))
    print(taks)

#GUI:
frame_tks = tkinter.Frame(root)
frame_tks.pack()

lbl_title = tkinter.Label(root, text="To-Do-List:", bg="White",width=30,font = "Time 15")
lbl_title.pack()

#list-Box:

lb = tkinter.Listbox(frame_tks, height =15,width=47)
lb.pack(side =tkinter.LEFT)

#Scrollbar:

scrollbar = tkinter.Scrollbar(frame_tks)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command =lb.yview)

#Entry:

info = tkinter.Entry()
info.pack()

#Buttons:

# ADD:
btn_add_taks = tkinter.Button(root, height =2,width=48,bg="White", text ="Add",font = "Time 9",command=add_taks)
btn_add_taks.pack()

# REMOVE:
btn_remove_taks = tkinter.Button(root, height =2,width=48,bg="White", text ="Remove",font = "Time 9",command=remove_taks)
btn_remove_taks.pack()

# LOAD:
btn_load_taks = tkinter.Button(root, height =2,width=48,bg="White", text ="Load",font = "Time 9",command=load_taks)
btn_load_taks.pack()

# SAVE:
btn_save_taks = tkinter.Button(root, height =2,width=48,bg="White", text ="Save",font = "Time 9",command=save_taks)
btn_save_taks.pack()

root.mainloop()

