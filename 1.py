import time as time
import tkinter as tk
from tkinter import ttk
from datetime import datetime

root=tk.Tk()
root.title("Stop Watch")
root.geometry("400x600+100+100")

start_time = None
end_time=None
#readable_time1=None
#readable_time2=None
actual_time=None
#actual_time2=None
vari = tk.StringVar()

def start_fun():
    global start_time
    start_time=time.time()
    start_button.configure(state='disable')
    end_button.configure(state='normal')
    reset_button.configure(state='normal')
    #global readable_time1
    #readable_time1=datetime.fromtimestamp(start_time).strftime('%H:%M:%S')
    #print (readable_time1)

def end_fun():
    global readable_time1
    global start_time
    global vari
    end_time=time.time()
    #readable_time2=datetime.fromtimestamp(end_time).strftime('%H:%M:%S')
    actual_time=end_time-start_time
    #actual_time=datetime.fromtimestamp(actual_time).strftime('%H:%M:%S')
    #print(readable_time2)
    end_button.configure(state='disable')
    label.configure(state='anable')
    reset_button.configure(state='normal')


    hours = int(actual_time // 3600)
    minutes = int((actual_time % 3600) // 60)
    seconds = int(actual_time % 60)
    
    vari.set(f"Elapsed time: {hours:02}:{minutes:02}:{seconds:02}")

def reset():
    start_button.configure(state='anaable')
    end_button.configure(state='disable')
    label.configure(state='disable')
    reset_button.configure(state='disable')

    hours = 0
    minutes = 0
    seconds = 0
    
    vari.set(f"Elapsed time: {hours:02}:{minutes:02}:{seconds:02}")


start_button= ttk.Button(root, text= 'start', command=start_fun)
start_button.pack(padx=20,pady=20)

end_button=ttk.Button(root, text='stop',command=end_fun)
end_button.pack()

label=ttk.Label(root, textvariable=vari, font=("Arial", 16))
label.pack(padx=20,pady=20)

reset_button=ttk.Button(root, text='Reset', command=reset)
reset_button.pack()

root.mainloop()




