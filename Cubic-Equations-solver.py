import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
    

def SolveCubicEqutions(a : float,b : float,c : float,d : float,e : float ,Low : int = -200 , High:int = 200) -> list :   
        if e == d :
            delta = b*b - 4*a*c
            if delta < 0:
                return []
            else :
                return [(-b + (delta**0.5)) / (2*a), (-b - (delta**0.5)) / (2*a)]
        else:
            Solve_Cubic_Equation_xess = [x*0.0001 for x in range(int(f'{Low}0000'), int(f'{High}0000')+1)]
            xss = []
            for x in Solve_Cubic_Equation_xess :
                if ((a*x ** 3) + (b*x**2) + (c * x) + (d) == e) :
                    xss.append(x)
                else :
                    continue
            return xss

def main() :         
    app3=tk.Tk()
    
    app3.geometry("588x310+382+121")
    app3.minsize(120, 1)
    app3.maxsize(1370, 749)
    app3.resizable(0,  0)
    app3.title("حل المعادلات المعقدة من الدرجة الثالثة")
    app3.configure(background="#313131")
    app3.configure(highlightbackground="#d9d9d9")
    app3.configure(highlightcolor="black")
    
    Label1 = tk.Label(app3,activebackground="#f9f9f9",activeforeground="black",background="#11aaf4",compound='center',disabledforeground="#a3a3a3",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",text='''حل المعادلات المعقدة من الدرجة الثالثة''')
    Label1.place(relx=0.0, rely=0.0, height=50, width=594)
    
    B4E = tk.Entry(app3,background="#5b5b5b",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",relief="flat",selectbackground="blue",selectforeground="white")
    B4E.place(relx=0.782, rely=0.426, height=20, relwidth=0.058)
    
    C4E = tk.Entry(app3,background="#5b5b5b",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",relief="flat",selectbackground="blue",selectforeground="white")
    C4E.place(relx=0.612, rely=0.426, height=20, relwidth=0.058)

    D4E = tk.Entry(app3,background="#5b5b5b",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",relief="flat",selectbackground="blue",selectforeground="white")
    D4E.place(relx=0.442, rely=0.419, height=20, relwidth=0.058)
    
    E4E = tk.Entry(app3,background="#5b5b5b",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",relief="flat",selectbackground="blue",selectforeground="white")
    E4E.place(relx=0.136, rely=0.419, height=20, relwidth=0.092)
    
    F4E = tk.Entry(app3,background="#5b5b5b",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",relief="flat",selectbackground="blue",selectforeground="white")
    F4E.place(relx=0.289, rely=0.419, height=20, relwidth=0.058)
    
    Label2_2 = tk.Label(app3,activebackground="#f9f9f9",activeforeground="black",anchor='w',background="#313131",compound='left',disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 11",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",text='''س''')
    Label2_2.place(relx=0.731, rely=0.426, height=28, width=23)
    
    Label2_1_1_1 = tk.Label(app3,activebackground="#f9f9f9",activeforeground="black",anchor='w',background="#313131",compound='left',disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 10",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",text='''3''')
    Label2_1_1_1.place(relx=0.714, rely=0.384, height=27, width=14)
    
    Label2_1_2 = tk.Label(app3,activebackground="#f9f9f9",activeforeground="black",anchor='w',background="#313131",compound='left',disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 11",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",text='''+''')
    Label2_1_2.place(relx=0.68, rely=0.426, height=28, width=14)
    
    Label2_2_1 = tk.Label(app3,activebackground="#f9f9f9",activeforeground="black",anchor='w',background="#313131",compound='left',disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 11",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",text='''س''')
    Label2_2_1.place(relx=0.561, rely=0.426, height=28, width=23)
    
    Label2_1_1_1_1 = tk.Label(app3,activebackground="#f9f9f9",activeforeground="black",anchor='w',background="#313131",compound='left',disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 10",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",text='''2''')
    Label2_1_1_1_1.place(relx=0.544, rely=0.387, height=28, width=14)
    
    Label2_1_2_1 = tk.Label(app3,activebackground="#f9f9f9",activeforeground="black",anchor='w',background="#313131",compound='left',disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 11",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",text='''+''')
    Label2_1_2_1.place(relx=0.51, rely=0.426, height=28, width=14)
    
    Label2_1_2_1_1 = tk.Label(app3,activebackground="#f9f9f9",activeforeground="black",anchor='w',background="#313131",compound='left',disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 11",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",text='''=''')
    Label2_1_2_1_1.place(relx=0.255, rely=0.419, height=18, width=14)
    
    Label2_1_2_1_2 = tk.Label(app3,activebackground="#f9f9f9",activeforeground="black",anchor='w',background="#313131",compound='left',disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 11",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",text='''+''')
    Label2_1_2_1_2.place(relx=0.357, rely=0.432, height=18, width=14)
    
    def start():
        if B4E.get().replace(" ","") == "" :
            a = 1
        elif B4E.get().replace(" ","") == "-" :
            a= -1
        elif '-' in B4E.get() :
            a = float(B4E.get().replace('-',""))
        else :
            a=float(B4E.get())

        if C4E.get().replace(" ","") == "" :
            b = 1
        elif C4E.get().replace(" ","") == "-" :
            b= -1
        elif '-' in C4E.get() :
            b = float(C4E.get().replace('-',""))
        else :
            b=float(C4E.get())

        if D4E.get().replace(" ","") == "" :
            c = 1
        elif D4E.get().replace(" ","") == "-" :
            c= -1
        elif '-' in D4E.get() :
            c = float(D4E.get().replace('-',""))
        else :
            c=float(D4E.get())
  

        if F4E.get().replace(" ","") == "" :
            d = 0
        elif '-' in F4E.get() :
            d = float(F4E.get().replace('-',""))
        else :
            d=float(F4E.get())


        if E4E.get().replace(" ","") == "" :
            e = 0
        elif '-' in E4E.get() :
            e = float(E4E.get().replace('-',""))
        else :
            e=float(E4E.get())

        SOLVERS = SolveCubicEqutions(a,b,c,d,e)
        if SOLVERS == [] :
            messagebox.showinfo("",
                                "عذرا - ليمكن حل هذه المعادلة")
        else :
            Listbox1.delete(0,tk.END)
            for i in SOLVERS :
                Listbox1.insert(tk.END,i)
    
    Button1 = tk.Button(app3,activebackground="#ececec",command=start,activeforeground="#000000",background="#11aaf4",compound='left',disabledforeground="#a3a3a3",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",relief="flat",text='''Solve''')
    Button1.place(relx=0.068, rely=0.742, height=54, width=127)
    
    Label2_2_2 = tk.Label(app3,activebackground="#f9f9f9",activeforeground="black",anchor='w',background="#313131",compound='left',disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 11",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",text='''= س''')
    Label2_2_2.place(relx=0.918, rely=0.742, height=28, width=43)
    
    Label2_2_1_1 = tk.Label(app3,activebackground="#f9f9f9",activeforeground="black",anchor='w',background="#313131",compound='left',disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 11",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",text='''س''')
    Label2_2_1_1.place(relx=0.391, rely=0.419, height=28, width=23)
    
    Listbox1 = tk.Listbox(app3,background="#0f78b7",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",relief="flat",selectbackground="blue",selectforeground="white")
    Listbox1.place(relx=0.629, rely=0.677, relheight=0.265, relwidth=0.245)
    
    
    app3.mainloop()
main()
