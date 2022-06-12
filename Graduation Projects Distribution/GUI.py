# Fatima shrateh 1181550
# Jihan Alshafei 1181641
#----------------------------------------------------------------------------------------

#standard GUI library for Python
from tkinter import *
#File dialog library is to open, save files or directories
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showinfo,showerror
import tkinter.ttk

class main(Frame):
#The master parameter is the parent widget and it is an optional parameter (by default it is none)
#that will be passed to the new instance of main class
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_main()

    def init_main(self):
        #Title of the window
        self.master.title("Welcome")

        #text for each button in the main window
        #bg --> is the background text color
        #fg --> text color
        #ttk.Separator --> add a vertical divider between each choice
        # grid is to arrange based on row and column num
        self.WelText = Label(self.master,relief=RIDGE, text=" Welcome to Project distribution program for students ", fg="BLACK")
        self.stuText = Label(self.master,relief=RIDGE,text=" student selection xlsx file ",bg='#133337', fg="white")
        self.stuText.grid(row=0, column=0)
        tkinter.ttk.Separator(self.master, orient=VERTICAL).grid(column=1, row=1, rowspan=4, sticky='ns')
        tkinter.ttk.Separator(self.master, orient=VERTICAL).grid(column=3, row=1, rowspan=4, sticky='ns')
        self.resText = Label(self.master,relief=RIDGE,text=" place of result file",bg='#133337', fg="white")
        self.resText.grid(row=0,column=5,pady=30)
#-------------------------------------------------------------------------------------------------
        #the buttons to let the user enter the input files and the output file save place
        # grid is to arrange based on row and column num
        browse1 = Button(self.master,text="Browse",command=self.browse1)
        browse1.grid(row=1, column=0)

        save= Button(self.master,text="Save As",command=self.save)
        save.grid(row=1, column=5)

        run = Button(self.master,width=20, text="Run",command=self.RUN)
        run.grid(row=4,padx=40,column=2,pady=60)
#----------------------------------------------------------------------------------------------------------
        #Parameters
        self.student_File = None
        self.result_File = None

    def browse1(self):
        # select student names file button command
        filename = askopenfilename(title="Select Student file",filetypes=[("Excel Files","*.xlsx")])
        self.student_File = filename
        toshow = "Student File = \n "+filename.split("/")[-1]
        self.stuText['text']=toshow

    def save(self):
        #Save button command
        filename = asksaveasfilename(title="choose place of result file",filetypes=[("Excel Files","*.xlsx")])
        self.result_File = filename
        self.resText['text']= filename + ".xlsx"

    def RUN(self):
        #check if student and result files have been selected
        if self.student_File != None or self.result_File!=None:

            filename = self.result_File.split("/")[-1] + ".xlsx"
            showinfo("Done","The output is in the "+filename+".")
        else:
            showerror("Error!!")           # show error message

#---------------------------Tkinter window settings ------------------------------------------------------
root = Tk()
root.geometry("550x250")        #window dimension
root['background']='#6191FA'    #set window color

bg = PhotoImage(file = "12.png") # add image into the window
label1 = Label( root, image = bg) #set the image as a label
label1.place(x = 195, y = 30)    # set the image place by x and y
root.resizable(True, True)       # window is sizeable using curser
Interface = main(root)
root.mainloop()
