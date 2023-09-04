from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
import sqlite3



class PMS:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Project Management System")
        self.root.geometry('1350x790+0+0')
        self.root.configure(background='light green')

        Rno=StringVar()
        name=StringVar()
        Class=StringVar()
        gender=StringVar()
        pna=StringVar()
        ana=StringVar()
        lna=StringVar()
        Dna=StringVar()

        def ireset():
            Rno.set('')
            name.set('')
            Class.set('')
            gender.set('')
            pna.set('')
            ana.set('')
            lna.set('')
            Dna.set('')
            
        def idelete():
            Rno.set('')
            name.set('')
            Class.set('')
            gender.set('')
            pna.set('')
            ana.set('')
            lna.set('')
            Dna.set('')
            self.Student1.delete('1.0',END)

        def display():
            self.Student1.insert(END, Rno.get()+'\t'+ name.get()+'\t\t'+ Class.get()+'\t'+ pna.get()+'\t'+ ana.get()+'\t'+ lna.get()+'\t\t'+ Dna.get()+'\t\t\t' ) 

        def add_student(self):
            cnon=pymysql.connect(host='localhost',user='root',database='PMSS')
            cur=con.cursor()
            cur.execute('insert into project values(%s,%s,%s,%s,%s,%s)',(self.Roll_no_var.get(),
                                                                         self.Name_var.get(),
                                                                         self.Class_var.get(),
                                                                         self.project_var.get(),
                                                                         self.link_var.get(),
                                                                         self.date_var.get()
                                                                         ))
            con.commit()
            con.close()

            
        

        #--------------------FRAME------------------

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width= 1350,bg='light blue', padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle =Label(TitleFrame,width=30,bg='light blue',font=('arial', 35, 'bold'),text="Project Submission Management System",padx=20)
        self.lblTitle.grid()

        ButtonFrame =Frame(MainFrame, bd=20, width=1350, height=50, padx=20,bg='light green', relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail =Frame(MainFrame, bd=20, width=1350, height=100,bg='light green', padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=20, width=1350, height=400, padx=20, bg='light green', relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE, font=('arial', 25,'bold'), bg='light green', text='STUDENT INFO:')
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRight =LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE,bg='light green', font=('arial', 25,'bold'), text='PROJECT INFO:')
        DataFrameRight.pack(side=RIGHT)


        #--------------------Widget------------------
        self.Student = Label(DataFrameLEFT, font=('arialBerlin Sans FB Demi', 15, 'bold'), text="Roll No.:", bg='light green', padx=2, pady=2)
        self.Student.grid(row=0, column=0, sticky=W)
        self.Student = Entry(DataFrameLEFT, font=('arialBerlin Sans FB Demi', 15), width=9, bg='pink', textvariable=Rno)
        self.Student.grid(row=0, column=2)

        self.Student = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="STUDENT Name:", bg='light green', padx=2, pady=2)
        self.Student.grid(row=1, column=0, sticky=W)

        self.Student = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="PROJECT NAME:", bg='light green', padx=2, pady=2)
        self.Student.grid(row=4, column=0, sticky=W)
        self.Student = Entry(DataFrameLEFT, font=('arialBerlin Sans FB Demi', 20), width=29, bg='pink', textvariable=pna)
        self.Student.grid(row=4, column=2)

        self.Student = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="About PROJECT:", bg='light green', padx=2, pady=2)
        self.Student.grid(row=5, column=0, sticky=W)
        self.Student = Text(DataFrameLEFT, font=('arialBerlin Sans FB Demi', 20), width=35, height=2, bg='turquoise')
        self.Student.grid(row=5, column=2)

        self.Student = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="PROJECT LINK:", bg='light green', padx=2, pady=2)
        self.Student.grid(row=6, column=0, sticky=W)
        self.Student = Entry(DataFrameLEFT, font=('arialBerlin Sans FB Demi', 20), width=35, bg='turquoise', textvariable=lna)
        self.Student.grid(row=6, column=2)

        
        self.Student = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="Date of Sumbission:", bg='light green', padx=2, pady=2)
        self.Student.grid(row=7, column=0, sticky=W)
        self.Student = Entry(DataFrameLEFT, font=('arialBerlin Sans FB Demi', 18), width=15, bg='tan', textvariable=Dna)
        self.Student.grid(row=7, column=2)
        
        self.Student = Entry(DataFrameLEFT, font=('arialBerlin Sans FB Demi', 18), width=25, bg='pink', textvariable=name)
        self.Student.grid(row=1, column=2)
        

        self.Student = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="CLASS:", bg='light green', padx=2, pady=2)
        self.Student.grid(row=2, column=0, sticky=W)
        

        self.box = ttk.Combobox(DataFrameLEFT, font=('arial', 18, 'bold'),state='readonly', width=23,textvariable=Class)
        self.box['value']=('',"XI'A'","XI'B'","XI'C'","XII'A'","XI'B'","XII'C'")
        self.box.current(0)
        self.box.grid(row=2, column=2)

        self.Student = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="Gender:", bg='light green', padx=2, pady=2)
        self.Student.grid(row=3, column=0, sticky=W)

        self.box = ttk.Combobox(DataFrameLEFT, font=('arial', 18, 'bold'),state='readonly', width=23, textvariable=gender)
        self.box['value']=('','MALE','FEMALE','OTHERS')
        self.box.current(0)
        self.box.grid(row=3, column=2)

        #-----------------------------------widget2-----------------------------------------------------
        self.Student = Text(DataFrameRight, font=('arialBerlin Sans FB Demi', 20), width=25, height=10, bg='black', fg='red3')
        self.Student.grid(row=5, column=2)

        #----------------------------------------------------------------
        self.lbla =Label(FrameDetail, font=('arial', 15, 'bold'),bg='light green',pady=5, text='Roll no.\t Student Name\t\t Class\t\t Project\t\t  Project Link\t\t Date of Sumbission \t')
        self.lbla.grid(row=0, column=0)
        self.Student1 = Text(FrameDetail, font=('arialBerlin Sans FB Demi', 20), width=85, height=3, bg='white', fg='black')
        self.Student1.grid(row=1, column=0, padx=1, pady=1)

        #------------------------------------Button-------------------

        self.bt1=Button(ButtonFrame, text= 'DISPLAY DATA',font=('arial', 15, 'bold'),bg='red2', fg='white', width=25, bd=4, command=display)
        self.bt1.grid(row=0, column=0)

        self.bt2=Button(ButtonFrame, text= 'RESET',font=('arial', 15, 'bold'),bg='red2', fg='white', width=25, bd=4, command= ireset)
        self.bt2.grid(row=0, column=1)

        self.bt3=Button(ButtonFrame, text= 'DELETE',font=('arial', 15, 'bold'),bg='red2', fg='white', width=25, bd=4, command=idelete)
        self.bt3.grid(row=0, column=2)

        self.bt4=Button(ButtonFrame, text= 'EXIT',font=('arial', 15, 'bold'),bg='red2', fg='white', width=25, bd=4, command= exit)
        self.bt4.grid(row=0, column=3)




        


        

if __name__ == '__main__':
    root=Tk()
    application = PMS(root)
    root.mainloop()
        
