import tkinter as tk
from tkinter import filedialog
from GO_enrichment import *
from tkinter import messagebox


def browse():
    filename= filedialog.askopenfilename()
    entry1.delete(0,"end")
    entry1.insert(0,filename)

def get_values():
    input_file_path = entry1.get()
    #print(input_file_path)
    sheet_name = entry2.get()
    #print(type(entry3.get()))
    #print(sheet_name)
    sheet_col_name_list = entry3.get()
    sheet_col_name_list = sheet_col_name_list.split(",")
    #print(sheet_col_name_list)
    result=go_en(input_file_path, sheet_name, sheet_col_name_list)
    if result!="":
        messagebox.showinfo("Congrats!!","File successfully created")
        tk.Label(frame,text=result).grid(row=4,column=0)

window=tk.Tk()
window.title("GO Enrichment Analysis")
window.geometry("800x400")

background_image=tk.PhotoImage(file=r"C:\Users\dell\Desktop\GO_Enrichment_code\GO_image1.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

header_label=tk.Label(window,text="GO Enrichment Analysis",bg="black",fg="white")
header_label.pack(side="top",fill="x")

footer_label=tk.Label(window,text="version 1.0",bg="black",fg="white")
footer_label.pack(side="bottom",fill="x")


frame=tk.Frame(window,relief="sunken",borderwidth=5)
frame.pack(side="right")

label1=tk.Label(frame,text="File Name")
label1.grid(row=0,column=0)
entry1=tk.Entry(frame,width=15)
entry1.grid(row=0,column=1)
button1=tk.Button(frame,text="Browse",bg="grey",fg="black",command=browse)
button1.grid(row=0,column=2,padx=5)

label2=tk.Label(frame,text="Sheet Name")
label2.grid(row=1,column=0)
entry2=tk.Entry(frame,width=15)
entry2.grid(row=1,column=1)

label3=tk.Label(frame,text="Sheet Column Names")
label3.grid(row=2,column=0)
entry3=tk.Entry(frame,width=15)
entry3.grid(row=2,column=1)

button2=tk.Button(frame,text="Run",bg="grey",fg="black",command=get_values)
button2.grid(row=3,column=1,pady=5)

#i=tk.PhotoImage(file=r"C:\Users\dell\Desktop\GO_Enrichment_code\GO_image1.png")
#image_label=tk.Label(window,image=i,bg="black",height=300,width=500)
#image_label.pack(side="left",fill="y")




window.mainloop()

#sheet_col_name_list = ["GO Biological Process Term","GO Cellular Component Term","GO Molecular Function Term"]
#go_en("GO_Enrichment_Analysis.xlsx","UpRegulated",sheet_col_name_list)