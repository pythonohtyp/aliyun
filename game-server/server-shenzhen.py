# -*- coding:utf-8 -*-
from func_ali_sz_open_start import *
import Tkinter as tk
from ScrolledText import ScrolledText
from func_ali_sz_change_ip import *


def enter_and_print_start():
    text_output.delete(0.0,'end')
    text_output.insert(0.0,func_ali_sz_start())
    # text_output.insert(0.0,lambda i:for i in func_ali_sz_start())
def enter_and_print_stop():
    text_output.delete(0.0,'end')
    text_output.insert(0.0,func_ali_sz_stop())

def get_entry_old_ip():
    old_ip = var_old_ip.get()
    return old_ip
def get_entry_new_ip():
    new_ip = var_new_ip.get()
    return new_ip

def ok():
    old_ip = get_entry_old_ip()
    new_ip = get_entry_new_ip()
    func_ali_sz_revoke_IP(old_ip)
    func_ali_sz_add_IP(new_ip)

# print func_ali_sz_start()
# print func_ali_sz_stop()

root = tk.Tk()
root.title("飒飒动漫开停服")
root.geometry('500x500')
label = tk.Label(root, text="飒飒动漫开停服脚本",font=('Arial',15,),height=4).grid(row=0, column=1)

photo = tk.PhotoImage(file="sasalogo.gif")
label = tk.Label(image=photo)
label.image = photo
label.grid(row=0,column=0,columnspan=1)

tk.Button(root,text="开服按钮",command=enter_and_print_start,bg='green',height=1).grid(row=1, column=0)
tk.Button(root,text="停服按钮",command=enter_and_print_stop,bg='red',height=1).grid(row=1, column=1)
tk.Label(root,text="-----------------------------------------------------------------------------------------------------------",height=1).grid(row=2, columnspan=3)
tk.Label(root,text="公司公网IP修改",height=1).grid(row=2, columnspan=2)
tk.Button(root,text="确认修改",command=ok,bg='white',height=1).grid(row=5, column=1,sticky=tk.E)

var_old_ip = tk.StringVar(value="0.0.0.0")
var_new_ip = tk.StringVar(value="0.0.0.0")
tk.Label(root, text='旧公网IP：', width=8).grid(row=3, sticky=tk.E)
old_ip_input = tk.Entry(root, textvariable=var_old_ip,width=20).grid(row=3, column=1)
tk.Label(root, text='新公网IP：', width=8).grid(row=4, sticky=tk.E)
new_ip_input = tk.Entry(root,textvariable=var_new_ip, width=20).grid(row=4, column=1)

text_output = ScrolledText(root,width=66)   #use ScrolledText(下拉条)
text_output.grid(row=6, columnspan=2)

# text_output = tk.Text(root,width=70)
# text_output.pack(side='left',fill='y')
# text_output.grid()

root.mainloop()
