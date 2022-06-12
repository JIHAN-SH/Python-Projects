#Fatima Shrateh 
#Jihan Alshafei 
#----------------------------
# The libraries are used
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os.path
from os import path
import fileinput
import sys
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import glob, os


converted_list=[]                                                                   # store all students ids from file
filesDirctory = []
idList = []
listForSearching = []                       #list to store all the students id's and their avg for the searching option
listForSearching2 = []              #list to store all the students id's and their taken hours for the searching option
f = open("IDsFile.txt", "a")

w = Tk()  # Login Window
# login window settings
w.geometry('390x430')
w.title(' LOGIN ')
w.resizable(0, 0)
# ------------------------
# Fnction to set gradient color for the background
def gradient(x):
    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(423512 + r)
        Frame(x, width=15, height=500, bg="#" + c).place(x=j, y=0)
        j = j + 15
        r = r + 1

gradient(w)                                                             # set the gradient color for the login window
#help label in the login window
note = Label(w, bg='white', text='#for student login:enter the Username as the format (id.txt)')
o = ('Time New Roman', 8)
note.config(font=o)
note.place(x=1, y=410)
# ---------------------------------------------------------------------
Frame(w, width=250, height=380, bg='white').place(x=70, y=22)              # set a white background abov the grdient one
# ---------------------------------------------------------------------------------------
#This function will plot a histogram show the distribution between student numbers and their AVGs
def histogram():
    global listForSearching
    global studentsAvg

    plt.style.use('ggplot')                                        #set the color of histo
    plt.xlabel('Averages')                                         # set the x label
    plt.ylabel('Number of students')                               #set the y label
    plt.title('Distribution of students grades')                   #set the title
    plt.hist(studentsAvg, bins=17)                                 #bins is how we can plot a data column in the graph
    plt.show()
#-----------------------------------------------------------------------------------------
# function to Add a new record file
def creatFile():
    global identery
    global idwindow
    global FileName
    Input = identery.get()                                      # the value in the message box that will take file name

    if Input in idList:

        messagebox.showinfo("Error", "This number is exist")     # show an error message box if the number isn't unique

    else:                                        # if number is unique , creat the file and insert its name to IDs file
        idList.append(Input)
        with open('IDsFile.txt', 'a') as f:
            f.write(Input + ".txt")
            f.write('\n')

        FileName = str("" + Input + ".txt")
        TextFile = open(FileName, "w")
        successMsg = Label(idwindow, relief=RIDGE, text='The file successfully created', fg='white', bg='#1CB044')
        successMsg.place(x=25, y=130)

# -------------------------------------------------------------------------------------------
# This function is used for submit student information which are added by the admin
def submit():
    # global is used to use these variables in another functions
    global eId
    global eyear
    global semester
    global eCourse
    global stuWindow
    global FileName
    global semesterInside
    fileName = str("" + eId.get() + ".txt")

    Input = f"{eyear.get()}/{semester.get()} ; {eCourse.get()}"
    # Check if there is an entry box is empty to show an error
    if len(eId.get()) == 0 or len(eyear.get()) == 0 or len(semester.get()) == 0 or len(eCourse.get()) == 0:
        messagebox.showinfo("Error", "You have missed something! All the fields are required")

    #check if the file is exist in the directory
    elif (path.exists(fileName) == True):
        txtFile = open(fileName, "a") # 'a' is to prevent overwrite on the file
        write = f"{Input}\n"
        txtFile.write(write)

        warning1 = Label(stuWindow, relief=RIDGE, text='The data is added to file successfully', fg='white',bg='#1CB044')
        warning1.place(x=60, y=356)
    else:
        warning2 = Label(stuWindow, relief=RIDGE, text='The id is not exist, you have to create file', fg='white',bg='#A30F13')
        warning2.place(x=60, y=356)
# ---------------------------------------------
# this function is to update course name or a grade in a student file
def Update():
    # global is used to use these variables in another functions
    global updateWindow
    global update_eId
    global old_Ecourse_grade
    global new_Ecourse_grade
    index = 0

    # Check if there is an entry box is empty to show an error
    if len(update_eId.get()) == 0 or len(old_Ecourse_grade.get()) == 0 or len(new_Ecourse_grade.get()) == 0:
        messagebox.showinfo("Error", "You have missed something! All the fields are required")

    # check if the file is exist in the directory
    elif (path.exists(update_eId.get()) == True):

        with open(update_eId.get(), 'r+') as usersFile: # 'r' is to read from the file
            usersRec = usersFile.readlines() #'userRec' is a list store all the file lines, each line in index
            findVar = old_Ecourse_grade.get() # to get the old value to update
            for i, elem in enumerate(usersRec):
                if findVar in elem:
                    print(i)
                    index = i

            courseName = usersRec[index].split(',')                                                # split all the lines
            #replace the old one by the new one
            newCourse = usersRec[index].replace(str(old_Ecourse_grade.get()), str(new_Ecourse_grade.get()))

            #check if the cource is in student file or not
            if (any(findVar in s for s in usersRec) == False):
                warning = Label(updateWindow, relief=RIDGE, text='The course you entered is not exist', fg='white',
                                bg='#A30F13')
                warning.place(x=100, y=375)
            else :
                warning1 = Label(updateWindow, relief=RIDGE, text='The file is successfully updated ', fg='white',
                                 bg='#1CB044')
                warning1.place(x=100, y=400)

       #function to replace and write into the file the new value
        def replacement(file, previousw, nextw):
            for line in fileinput.input(file, inplace=1):
                line = line.replace(previousw, nextw)
                sys.stdout.write(line)
        #function call
        replacement(update_eId.get(), usersRec[index], newCourse)

    else:
        warning2 = Label(updateWindow, relief=RIDGE, text='The id you want to update is not exist', fg='white',
                         bg='#A30F13')
        warning2.place(x=100, y=375)
# ---------------------------------------------
# Show all student Statistic
def StudentStatADMINFunc():
    # global is used to use these variables in another functions
    global stuStatWindow
    global studentStat_eId
    global usersRec
    global course_of_semester
    global grade
    global AvgPerSemester
    global listForSearching
    global listForSearching2
    global semester
    index = 0
    Hours_of_Semester1 = 0
    Total_hours = 0 #sum of student hours
    overallSum = 0  #the sum of student grades
    overallAvg = 0  #the Avg of student grades

    # Check if there is an entry box is empty to show an error
    if len(studentStat_eId.get()) == 0:
        messagebox.showinfo("Error", "You have missed something! All the fields are required")
    #check if the file is exist
    elif (path.exists(studentStat_eId.get()) == True):
        with open(studentStat_eId.get(), 'r+') as usersFile:                                 #open the file and read it
            usersRec = usersFile.readlines()                                   #userRec is a list has lines of the file
        for j in range(0, len(usersRec)):
            semester1 = usersRec[j]                                                 #semester1 store each line(semester)
            var1 = semester1[14:]                               #take the semester from the begining of the first course

            course_of_semester = var1.split(',') #split each course alone
#----------------------------------AVG PER SEMESTER --------------------------------------------------------------------
            Sum = 0                                                                                   #sum of the grades
            count = 0                        #number of grades that is the grade are in th odd indices in the grade list
            AvgPerSemester = 0
            #grade is a list that has the grades and the cources seperately
            grade = [words for segments in course_of_semester for words in segments.split()]
            for k in range(1, len(grade)):
                equation = k % 2                                        #take only the odd indices(wich have the grades)
                if (equation != 0):  # odd
                    count = count + 1                                               #to count these indices to find avg
                    Sum = Sum + int(grade[k])                                       #to add each sum to the sum variable
            AvgPerSemester = Sum / count                                                      #find the avg per semester
            overallSum = overallSum + AvgPerSemester                                    #sum of grades for all semesters
            print(f'the over all sum is {overallSum}')
            # ---------- IN Window ------------------
            # it will print avg per semester in the window
            AVG = Label(stuStatWindow, relief=RIDGE,text=f'The AVG grade of semester {j + 1} is => {round(AvgPerSemester, 2)}',fg='white', bg='#7A437A')
            AVG.place(x=3, y=(225 + (32 * j)))                #(32*j) is to put each semester avg in a place in a window
            l = ('Comic Sans MS', 13)
            AVG.config(font=l)
            # ----------The first index(course)-------------
            var2 = course_of_semester[0]                                  #is a list has the first course and its grade
            Hours_of_course = int(var2[5])      #index 5 of var2 is the hours number of the first course of the semester
            # ------------------------------AVG grade per semster ---------------------------
            Total_hours = Total_hours + Hours_of_course       #add the first hour of the first course to the total hours
            # ----------The remaining indices (courses)-------------
            for i in range(1, int(len(course_of_semester))):              # index 1 is the second course of the semester
                var2 = course_of_semester[i]
                Hours_of_course = int(var2[6])       #because there is a space before the cource the grade is in index 6
                Total_hours = Total_hours + Hours_of_course       #add the hours of remaining courses to the total hours

        overallAvg = overallSum / (len(usersRec)) # over all avg for each student
        # these to print the calculated data into the window
        a1 = Label(stuStatWindow, relief=FLAT, text='The overall Avg of', fg='white', bg='#472747')
        a1.place(x=3, y=160)
        l = ('Comic Sans MS', 14)
        a1.config(font=l)

        a2 = Label(stuStatWindow, relief=RIDGE, text=f' {Total_hours} ', fg='white', bg='#1CB044')
        a2.place(x=174, y=160)
        l = ('Comic Sans MS', 14)
        a2.config(font=l)

        a3 = Label(stuStatWindow, relief=FLAT, text='hours is', fg='white', bg='#472747')
        a3.place(x=208, y=160)
        l = ('Comic Sans MS', 14)
        a3.config(font=l)

        a4 = Label(stuStatWindow, relief=RIDGE, text=f' {round(overallAvg, 2)} ', fg='white', bg='#1CB044')
        a4.place(x=282, y=160)
        l = ('Comic Sans MS', 14)
        a4.config(font=l)

        #these list are defined to store avg and total hour to use it in search option
        listForSearching.append(studentStat_eId.get())
        listForSearching.append(overallAvg)

        listForSearching2.append(studentStat_eId.get())
        listForSearching2.append(Total_hours)


    else:
        warning2 = Label(stuStatWindow, relief=RIDGE, text='The id you want to show is not exist', fg='white',bg='#A30F13')
        warning2.place(x=80, y=360)
        l = ('Comic Sans MS', 10)
        warning2.config(font=l)
    return print(overallAvg)
# -------------------------------------------------------------------------------
#function to get the remaining cources that the student does not take it
def RemainingCourses4ADMIN():
    global grade
    global stuStatWindow
    global studentStat_eId
    global usersRec
    global course_of_semester
    global RemainCoursesWindow
    listwithoutSPACE = []  # list to store all courses names without spaces
    TakenCourses = []

    RemainCoursesWindow = Tk()
    RemainCoursesWindow.title('Remaining Courses ')
    RemainCoursesWindow.geometry('500x630')
    RemainCoursesWindow.resizable(0, 0)
    stuStat_label1 = Label(RemainCoursesWindow, relief=RIDGE, text='Remaining Courses', fg='black', bg='#FCC653')
    l = ('Comic Sans MS', 15)
    stuStat_label1.config(font=l)
    stuStat_label1.place(x=150, y=1)

    # this file contain all the courses name , check if it's exist , read and split and store in a list
    if (path.exists('AllCourses.txt') == True):
        with open('AllCourses.txt', 'r+') as AllCoursesFile:
            courseFile = AllCoursesFile.readlines()
            for element in courseFile:
                listwithoutSPACE.append(element.strip())

        if (path.exists(studentStat_eId.get()) == True):
            with open(studentStat_eId.get(), 'r+') as usersFile:
                usersRec = usersFile.readlines()
                print(usersRec)
            for j in range(0, int(len(usersRec))):
                semester1 = usersRec[j]
                var1 = semester1[14:]

                course_of_semester = var1.split(',')
                ##Courses is a list that has the cources seperately
                Courses = [words for segments in course_of_semester for words in segments.split()]
                for k in range(0, len(Courses)):
                    equation1 = k % 2
                    if (equation1 == 0):  # even indices that have the courses
                        TakenCourses.append(Courses[k]) # list has the taken courses

            # to compare two lists (all courses & taken courses)
            temp3 = [item for item in listwithoutSPACE if item not in TakenCourses]

            # -------------------------------- IN Window ---------------------------
            for m in range(0, 11):
                R_courses = Label(RemainCoursesWindow, relief=RIDGE, text=f' {temp3[m]}', fg='white', bg='#f50000')
                R_courses.place(x=5, y=(60 + (50 * m)))
                l = ('Comic Sans MS', 12)
                R_courses.config(font=l)

            for s in range(11, 22):
                R_courses = Label(RemainCoursesWindow, relief=RIDGE, text=f' {temp3[s]}', fg='white', bg='#f50000')
                R_courses.place(x=140, y=(-490 + (50 * s)))
                l = ('Comic Sans MS', 12)
                R_courses.config(font=l)

            for q in range(22, 33):
                R_courses = Label(RemainCoursesWindow, relief=RIDGE, text=f' {temp3[q]}', fg='white', bg='#f50000')
                R_courses.place(x=275, y=(-1040 + (50 * q)))
                l = ('Comic Sans MS', 12)
                R_courses.config(font=l)

            for f in range(33, len(temp3)):
                R_courses = Label(RemainCoursesWindow, relief=RIDGE, text=f' {temp3[f]}', fg='white', bg='#f50000')
                R_courses.place(x=410, y=(-1590 + (50 * f)))
                l = ('Comic Sans MS', 12)
                R_courses.config(font=l)

        else:
            warning = Label(stuStatWindow, relief=RIDGE, text='The id you want to show is not exist', fg='white',
                            bg='#A30F13')
            warning.place(x=80, y=420)
            l = ('Comic Sans MS', 10)
            warning.config(font=l)

    else:
        warning1 = Label(stuStatWindow, relief=RIDGE, text='The file that has all course names is not exist',
                         fg='white',
                         bg='#A30F13')
        warning1.place(x=80, y=400)
        l = ('Comic Sans MS', 10)
        warning1.config(font=l)
# -------------------------------------------------------------------------------
# this function is to show statistic of student
def StudentStatSTUDENTFunc():
    # global is used to use these variables in another functions
    global stuStatWindow
    global usersRec
    global course_of_semester
    global grade
    global AvgPerSemester
    global eId
    global e1
    index = 0
    Hours_of_Semester1 = 0
    Total_hours = 0
    overallSum = 0
    overallAvg = 0

    # Check if the entry box is empty to show an error
    if len(e1.get()) == 0:
        messagebox.showinfo("Error", "You have missed something! All the fields are required")

    elif (path.exists(e1.get()) == True):
        with open(e1.get(), 'r+') as usersFile:
            usersRec = usersFile.readlines()
        for j in range(0, int(len(usersRec))):
            semester1 = usersRec[j]  # ····
            var1 = semester1[14:]

            course_of_semester = var1.split(',')
# ----------------------------------- find AVG per semester ------------------------------------------------
            Sum = 0
            count = 0
            AvgPerSemester = 0

            grade = [words for segments in course_of_semester for words in segments.split()]
            print(f"grade is {grade}")
            for k in range(1, len(grade)):
                equation = k % 2
                if (equation != 0):  # odd
                    count = count + 1
                    # print(f"the grade is {grade[k]}")
                    Sum = Sum + int(grade[k])
                    # print(f"SUM for the {j} semester is : {Sum}")
            AvgPerSemester = Sum / count
            overallSum = overallSum + AvgPerSemester
            # ---------- IN Window ------------------
            AVG = Label(stuStatWindow, relief=RIDGE,
                        text=f'The AVG grade of semester {j + 1} is => {round(AvgPerSemester, 2)}',
                        fg='white', bg='#7A437A')
            AVG.place(x=3, y=(210 + (32 * j)))
            l = ('Comic Sans MS', 13)
            AVG.config(font=l)
            # ----------- IN WINDOW ------------------
#---------------------------------------- find the AVG -----------------------------------------------------------------
            # ----------The grade of the first course in each semester line (course)------------------------------------
            var2 = course_of_semester[0]
            Hours_of_course = int(var2[5])
            # ------------------------------AVG grade per semster ---------------------------
            Total_hours = Total_hours + Hours_of_course
            # ----------The remaining indices (courses)-------------
            for i in range(1, int(len(course_of_semester))):
                var2 = course_of_semester[i]
                Hours_of_course = int(var2[6])
                Total_hours = Total_hours + Hours_of_course

        overallAvg = overallSum / (len(usersRec))
        a1 = Label(stuStatWindow, relief=FLAT, text='The overall Avg of', fg='white', bg='#472747')
        a1.place(x=3, y=140)
        l = ('Comic Sans MS', 14)
        a1.config(font=l)

        a2 = Label(stuStatWindow, relief=RIDGE, text=f' {Total_hours} ', fg='white', bg='#1CB044')
        a2.place(x=174, y=140)
        l = ('Comic Sans MS', 14)
        a2.config(font=l)

        a3 = Label(stuStatWindow, relief=FLAT, text='hours is', fg='white', bg='#472747')
        a3.place(x=208, y=140)
        l = ('Comic Sans MS', 14)
        a3.config(font=l)

        a4 = Label(stuStatWindow, relief=RIDGE, text=f' {round(overallAvg, 2)} ', fg='white', bg='#1CB044')
        a4.place(x=282, y=140)
        l = ('Comic Sans MS', 14)
        a4.config(font=l)

    else:
        warning2 = Label(stuStatWindow, relief=RIDGE, text='The id you want to show is not exist', fg='white',
                         bg='#A30F13')
        warning2.place(x=80, y=360)
        l = ('Comic Sans MS', 10)
        warning2.config(font=l)
# --------------------------------------------------------------------------------
# show remaining courses for student
def RemainingCourses4StudentStat():
    global grade
    global stuStatWindow
    global studentStat_eId
    global usersRec
    global course_of_semester
    global RemainCoursesWindow
    global e1
    listwithoutSPACE = []
    TakenCourses = []

    RemainCoursesWindow = Tk()
    RemainCoursesWindow.title('Remaining Courses ')
    RemainCoursesWindow.geometry('500x630')
    RemainCoursesWindow.resizable(0, 0)
    stuStat_label1 = Label(RemainCoursesWindow, relief=RIDGE, text='Remaining Courses', fg='black', bg='#FCC653')
    l = ('Comic Sans MS', 15)
    stuStat_label1.config(font=l)
    stuStat_label1.place(x=150, y=1)

    if (path.exists('AllCourses.txt') == True):
        with open('AllCourses.txt', 'r+') as AllCoursesFile:
            courseFile = AllCoursesFile.readlines()
            for element in courseFile:
                listwithoutSPACE.append(element.strip())

        if (path.exists(e1.get()) == True):
            with open(e1.get(), 'r+') as usersFile:
                usersRec = usersFile.readlines()
                print(usersRec)
            for j in range(0, int(len(usersRec))):
                semester1 = usersRec[j]  # ····
                var1 = semester1[14:]

                course_of_semester = var1.split(',')

                Courses = [words for segments in course_of_semester for words in segments.split()]

                for k in range(0, len(Courses)):
                    equation1 = k % 2
                    if (equation1 == 0):  # even indices
                        TakenCourses.append(Courses[k])

            temp3 = [item for item in listwithoutSPACE if item not in TakenCourses]
            # ------------------------------------ IN Window ------------------------------------------
            for m in range(0, 11):
                R_courses = Label(RemainCoursesWindow, relief=RIDGE, text=f' {temp3[m]}', fg='white', bg='#f50000')
                R_courses.place(x=5, y=(60 + (50 * m)))
                l = ('Comic Sans MS', 12)
                R_courses.config(font=l)

            for s in range(11, 22):
                R_courses = Label(RemainCoursesWindow, relief=RIDGE, text=f' {temp3[s]}', fg='white', bg='#f50000')
                R_courses.place(x=140, y=(-490 + (50 * s)))
                l = ('Comic Sans MS', 12)
                R_courses.config(font=l)

            for q in range(22, 33):
                R_courses = Label(RemainCoursesWindow, relief=RIDGE, text=f' {temp3[q]}', fg='white', bg='#f50000')
                R_courses.place(x=275, y=(-1040 + (50 * q)))
                l = ('Comic Sans MS', 12)
                R_courses.config(font=l)

            for f in range(33, len(temp3)):
                R_courses = Label(RemainCoursesWindow, relief=RIDGE, text=f' {temp3[f]}', fg='white', bg='#f50000')
                R_courses.place(x=410, y=(-1590 + (50 * f)))
                l = ('Comic Sans MS', 12)
                R_courses.config(font=l)

        else:
            warning = Label(stuStatWindow, relief=RIDGE, text='The id you want to show is not exist', fg='white',
                            bg='#A30F13')
            warning.place(x=80, y=420)
            l = ('Comic Sans MS', 10)
            warning.config(font=l)

    else:
        warning1 = Label(stuStatWindow, relief=RIDGE, text='The file that has all course names is not exist',
                         fg='white',
                         bg='#A30F13')
        warning1.place(x=80, y=400)
        l = ('Comic Sans MS', 10)
        warning1.config(font=l)
# -------------------------------------------------------------------------------
#show statistic for all students
def globalStatistics():
    # global is used to use these variables in another functions
    global gloStatWindow
    global studentStat_eId
    global usersRec
    global course_of_semester
    global grade
    global AvgPerSemester
    global studentsAvg
    global OverallAVGAllstudents

    studentsAvg = []
    # overallAvg = 0
    OverallSumAllstudents = 0
    OverallAVGAllstudents = 0

    with open('IDsFile.txt', 'r') as file:
        filesDirctory = file.readlines()
        print(filesDirctory)

    for element in filesDirctory:
        converted_list.append(element.strip())


    for k in range(0, len(converted_list)):
        individualId = converted_list[k]  # take files from converted_list that has all the students ids
        idFile = individualId
        print(f"the converted_list[k] is {converted_list[k]}") #open students files one by one
        if (path.exists(idFile) == True):
            overallSum = 0
            overallAvg = 0
            with open(idFile, 'r+') as usersFile:
                usersRec = usersFile.readlines()
                print(f" the user record is {usersRec}")
            for j in range(0, int(len(usersRec))):
                semester1 = usersRec[j]
                var1 = semester1[14:]
                print(f"var1 is {var1}")
                course_of_semester = var1.split(',')
                print(f'fourse_ofsemster is {course_of_semester}')
                Sum = 0
                count = 0
                AvgPerSemester = 0

                grade = [words for segments in course_of_semester for words in segments.split()]
                for k in range(1, len(grade)):
                    equation = k % 2
                    if (equation != 0):  # odd
                        count = count + 1
                        Sum = Sum + int(grade[k])
                AvgPerSemester = Sum / count
                print(f'AvgPerSemester is {AvgPerSemester}')

                overallSum = overallSum + AvgPerSemester # overallsum = sum of semesters avg for one student
                print(f'overall sum is {overallSum}')
#---------------------------------- find Over All AVG ------------------------------------------------------------
            overallAvg = round(overallSum / (len(usersRec)),2)
            studentsAvg.append(overallAvg) # add each student avg into studentsAvg list

#find over all avg for all students
    for d in range(len(studentsAvg)):
        OverallSumAllstudents = OverallSumAllstudents + studentsAvg[d] # find overall sum of all students averages
    OverallAVGAllstudents = round(OverallSumAllstudents / len(studentsAvg),2) # find overallAvg of all students averages

#print in window the above data

    a1 = Label(gloStatWindow, relief=FLAT, text='The Overall AVG for All students is', fg='white', bg='#472747')
    a1.place(x=20, y=150)
    l = ('Comic Sans MS', 12)
    a1.config(font=l)

    a2 = Label(gloStatWindow, relief=RIDGE, text=f' {OverallAVGAllstudents} ', fg='white', bg='#1CB044')
    a2.place(x=300, y=150)
    l = ('Comic Sans MS', 12)
    a2.config(font=l)
#-------------------------------------------------------------------------------
def globalStatistics2():
    #This function is as the global statisticc for admin , but here without printing the lables of the admin window
    # global is used to use these variables in another functions
    global gloStatWindow
    global studentStat_eId
    global usersRec
    global course_of_semester
    global grade
    global AvgPerSemester
    global studentsAvg
    global OverallAVGAllstudents

    studentsAvg = []
    # overallAvg = 0
    OverallSumAllstudents = 0
    OverallAVGAllstudents = 0
# open file that has all the files
    with open('IDsFile.txt', 'r') as file:
        filesDirctory = file.readlines()
        print(filesDirctory)

    for element in filesDirctory:
        converted_list.append(element.strip())

    for k in range(0, len(converted_list)):
        individualId = converted_list[k]  # take files from converted_list that has all the students ids
        idFile = individualId
        print(f"the converted_list[k] is {converted_list[k]}") #open students files one by one
        if (path.exists(idFile) == True):
            overallSum = 0
            overallAvg = 0
            with open(idFile, 'r+') as usersFile:
                usersRec = usersFile.readlines()
                print(f" the user record is {usersRec}")
            for j in range(0, int(len(usersRec))):
                semester1 = usersRec[j]
                var1 = semester1[14:]
                print(f"var1 is {var1}")
                course_of_semester = var1.split(',')
                print(f'fourse_ofsemster is {course_of_semester}')
                Sum = 0
                count = 0
                AvgPerSemester = 0

                grade = [words for segments in course_of_semester for words in segments.split()]
                for k in range(1, len(grade)):
                    equation = k % 2
                    if (equation != 0):  # odd
                        count = count + 1
                        Sum = Sum + int(grade[k])
                AvgPerSemester = Sum / count
                print(f'AvgPerSemester is {AvgPerSemester}')

                overallSum = overallSum + AvgPerSemester # overallsum = sum of semesters avg for one student
                print(f'overall sum is {overallSum}')
#------------------------------------- finding AVG ----------------------------------
            overallAvg = round(overallSum / (len(usersRec)),2)
            print(f'overallAVG is {overallAvg}')
            studentsAvg.append(overallAvg) # add each student avg into studentsAvg list
            print(f"student avg is {studentsAvg}")


    for d in range(len(studentsAvg)):
        OverallSumAllstudents = OverallSumAllstudents + studentsAvg[d] # find overall sum of all students averages
    print(f"over al sum is {OverallSumAllstudents}")
    OverallAVGAllstudents = round(OverallSumAllstudents / len(studentsAvg),2) # find overallAvg of all students averages

    print(f"the final final avg is {OverallAVGAllstudents}")


    return OverallAVGAllstudents
#-------------------------------------------------------------------------------
# function to calculate avg hours per semester (1 ,2 and 3 )
def avgHourPerSem():
    global gloStatWindow

    listwithoutSpaces = []  # store the semesters without spaces
    listOfSemester1 = []    #list 1 and 2 and 3 to store courses of each semster
    listOfSemester2 = []
    listOfSemester3 = []
    index = 0
    Hours_of_Semester1 = 0
    Total_hours = 0  # sum of student hours
    Total_hours2 = 0  # sum of student hours
    Total_hours3 = 0  # sum of student hours

    with open('IDsFile.txt', 'r') as file:
        filesDirctory2 = file.readlines()
        print(filesDirctory2)

    for element in filesDirctory2:
        listwithoutSpaces.append(element.strip())
    print(listwithoutSpaces)
    for k in range(0, len(listwithoutSpaces)):
        individualStudent = listwithoutSpaces[k]          # take files from converted_list that has all the students ids
        if (path.exists(individualStudent) == True):
            with open(individualStudent, 'r+') as usersFile:
                StudentFile = usersFile.readlines()

                for j in range(0, int(len(StudentFile))):
                    semester = StudentFile[j]
                    year_Semester = semester.split(';')                                          # split all the lines
                    del year_Semester[1]

                    if (int(year_Semester[0][10]) == 1):
                        listOfSemester1.append(semester)

                    elif (int(year_Semester[0][10]) == 2):
                        listOfSemester2.append(semester)

                    elif (int(year_Semester[0][10]) == 3):
                        listOfSemester3.append(semester)

    for j in range(0, len(listOfSemester1)):
        semester1 = listOfSemester1[j]  # semester1 store each line(semester)
        var1 = semester1[14:]  # take the semester from the begining of the first course

        course_of_semester = var1.split(',')  # split each course alone
    #------------------------------------------------------------------------------

        var2 = course_of_semester[0]  # is a list has the first course and its grade
        Hours_of_course = int(var2[5])  # index 5 of var2 is the hours number of the first course of the semester
        # ------------------------------Total hours per semster ---------------------------
        Total_hours = Total_hours + Hours_of_course  # add the first hour of the first course to the total hours
        # ----------The remaining indices (courses)-------------
        for i in range(1, int(len(course_of_semester))):  # index 1 is the second course of the semester
            var3 = course_of_semester[i]
            Hours_of_course = int(var3[6])  # because there is a space before the cource the grade is in index 6
            Total_hours = Total_hours + Hours_of_course  # add the hours of remaining courses to the total hours

    #-------------------------------- list 2---------------------------------------------
    for j in range(0, len(listOfSemester2)):
        semester1 = listOfSemester2[j]  # semester1 store each line(semester)
        var1 = semester1[14:]  # take the semester from the begining of the first course

        course_of_semester = var1.split(',')  # split each course alone
#---------------------------------------------------------------------------------------

        var2 = course_of_semester[0]  # is a list has the first course and its grade
        Hours_of_course = int(var2[5])  # index 5 of var2 is the hours number of the first course of the semester
        # ------------------------------total hours per semster ---------------------------
        Total_hours2 = Total_hours2 + Hours_of_course  # add the first hour of the first course to the total hours
        # ----------The remaining indices (courses)-------------
        for i in range(1, int(len(course_of_semester))):  # index 1 is the second course of the semester
            var3 = course_of_semester[i]
            Hours_of_course = int(var3[6])  # because there is a space before the cource the grade is in index 6
            Total_hours2 = Total_hours2 + Hours_of_course  # add the hours of remaining courses to the total hours

#------------------------------------------list 3---------------------------------------------------
    for j in range(0, len(listOfSemester3)):
        semester1 = listOfSemester3[j]  # semester1 store each line(semester)
        var1 = semester1[14:]  # take the semester from the begining of the first course

        course_of_semester = var1.split(',')  # split each course alone
#--------------------------------------------------------------------------------------------------

        var2 = course_of_semester[0]  # is a list has the first course and its grade
        Hours_of_course = int(var2[5])  # index 5 of var2 is the hours number of the first course of the semester

        # ------------------------------Total hours per semster ---------------------------
        Total_hours3 = Total_hours3 + Hours_of_course  # add the first hour of the first course to the total hours

        # ---------------------------------The remaining houres of the remaining courses------------------
        for i in range(1, int(len(course_of_semester))):  # index 1 is the second course of the semester
            var3 = course_of_semester[i]
            Hours_of_course = int(var3[6])  # because there is a space before the cource the grade is in index 6
            Total_hours3 = Total_hours3 + Hours_of_course  # add the hours of remaining courses to the total hours
     # calculate avg hours per semester
    AvgSemester1 = Total_hours / len(listOfSemester1)
    AvgSemester2 = Total_hours2 / len(listOfSemester2)
    AvgSemester3 = Total_hours3 / len(listOfSemester3)


    a1 = Label(gloStatWindow, relief=FLAT, text='The average hours per semesters (1,2,3) are', fg='white', bg='#472747')
    a1.place(x=20, y=190)
    l = ('Comic Sans MS', 12)
    a1.config(font=l)

    a2 = Label(gloStatWindow, relief=RIDGE, text=f' {AvgSemester1} , {AvgSemester2}, {AvgSemester3} ', fg='white', bg='#1CB044')
    a2.place(x=350, y=190)
    l = ('Comic Sans MS', 12)
    a2.config(font=l)

#-------------------------------------------------------------------------------
# this is function as the before one for the admin , but because not to show the labels of admin labels
def avgHourPerSem2():
    listwithoutSpaces = []
    listOfSemester1 = []
    listOfSemester2 = []
    listOfSemester3 = []
    index = 0
    Hours_of_Semester1 = 0
    Total_hours = 0  # sum of student hours
    Total_hours2 = 0  # sum of student hours
    Total_hours3 = 0  # sum of student hours

    with open('IDsFile.txt', 'r') as file:
        filesDirctory2 = file.readlines()
        print(filesDirctory2)

    for element in filesDirctory2:
        listwithoutSpaces.append(element.strip())
    print(listwithoutSpaces)
    for k in range(0, len(listwithoutSpaces)):
        individualStudent = listwithoutSpaces[k]  # take files from converted_list that has all the students ids
        if (path.exists(individualStudent) == True):
            with open(individualStudent, 'r+') as usersFile:
                StudentFile = usersFile.readlines()

                for j in range(0, int(len(StudentFile))):
                    semester = StudentFile[j]
                    year_Semester = semester.split(';')  # split all the line
                    del year_Semester[1]

                    if (int(year_Semester[0][10]) == 1):
                        listOfSemester1.append(semester)

                    elif (int(year_Semester[0][10]) == 2):
                        listOfSemester2.append(semester)

                    elif (int(year_Semester[0][10]) == 3):
                        listOfSemester3.append(semester)

    for j in range(0, len(listOfSemester1)):
        semester1 = listOfSemester1[j]  # semester1 store each line(semester)
        var1 = semester1[14:]  # take the semester from the begining of the first course

        course_of_semester = var1.split(',')  # split each course alone
    #---------------------------------------------------------------------------------------------

        var2 = course_of_semester[0]  # is a list has the first course and its grade
        Hours_of_course = int(var2[5])  # index 5 of var2 is the hours number of the first course of the semester
        # ------------------------------AVG grade per semster ---------------------------
        Total_hours = Total_hours + Hours_of_course  # add the first hour of the first course to the total hours
        # ----------The remaining indices (courses)-------------
        for i in range(1, int(len(course_of_semester))):  # index 1 is the second course of the semester
            var3 = course_of_semester[i]
            Hours_of_course = int(var3[6])  # because there is a space before the cource the grade is in index 6
            Total_hours = Total_hours + Hours_of_course  # add the hours of remaining courses to the total hours
    #--------------------------------list 2---------------------------------------------
    for j in range(0, len(listOfSemester2)):
        semester1 = listOfSemester2[j]  # semester1 store each line(semester)
        var1 = semester1[14:]  # take the semester from the begining of the first course

        course_of_semester = var1.split(',')  # split each course alone
    #--------------------------------------------------------------------------------------

        var2 = course_of_semester[0]  # is a list has the first course and its grade
        Hours_of_course = int(var2[5])  # index 5 of var2 is the hours number of the first course of the semester
        # ------------------------------total hours per semster ---------------------------
        Total_hours2 = Total_hours2 + Hours_of_course  # add the first hour of the first course to the total hours
        # -------------------------------------------------------------------------------
        for i in range(1, int(len(course_of_semester))):  # index 1 is the second course of the semester
            var3 = course_of_semester[i]
            Hours_of_course = int(var3[6])  # because there is a space before the cource the grade is in index 6
            Total_hours2 = Total_hours2 + Hours_of_course  # add the hours of remaining courses to the total hours
#------------------------------------------list 3---------------------------------------------------
    for j in range(0, len(listOfSemester3)):
        semester1 = listOfSemester3[j]  # semester1 store each line(semester)
        var1 = semester1[14:]  # take the semester from the begining of the first course

        course_of_semester = var1.split(',')  # split each course alone
    #-----------------------------------------------------------------------------------------------

        var2 = course_of_semester[0]  # is a list has the first course and its grade
        Hours_of_course = int(var2[5])  # index 5 of var2 is the hours number of the first course of the semester
        # ------------------------------AVG grade per semster ---------------------------
        Total_hours3 = Total_hours3 + Hours_of_course  # add the first hour of the first course to the total hours
        # ----------The remaining indices (courses)-------------
        for i in range(1, int(len(course_of_semester))):  # index 1 is the second course of the semester
            var3 = course_of_semester[i]

            Hours_of_course = int(var3[6])  # because there is a space before the cource the grade is in index 6
            Total_hours3 = Total_hours3 + Hours_of_course  # add the hours of remaining courses to the total hours

    AvgSemester1 = Total_hours / len(listOfSemester1)
    AvgSemester2 = Total_hours2 / len(listOfSemester2)
    AvgSemester3 = Total_hours3 / len(listOfSemester3)

    return AvgSemester1 , AvgSemester2 , AvgSemester3
#-----------------------------------------------------------------------------
# function to search based on avg or taken hours
def SearchSubmit():
    global value_inside1  # based on what
    global value_inside2  # < or > or =
    global searchentery2  # the entered value to compare
    global listForSearching
    global listForSearching2
    global stuStatWindow
    global search
    avgORTaken_value = searchentery2.get()  #what user choose to search based on
    sign = value_inside2.get()              #the sign < or > or =

   # check if the entry is empty or not
    if ((len(searchentery2.get()) == 0) or ((searchentery2.get().isnumeric()) == False)):
        warning2 = Label(search, relief=RIDGE, text='You have to enter a value to compare', fg='white',bg='#A30F13')
        warning2.place(x=3, y=300)
    else:
        searchSub = Tk()
        searchSub.title('Students that satisfy ')
        searchSub.geometry('355x550')
        searchSub.resizable(0, 0)
        stuStat_label1 = Label(searchSub, relief=RIDGE,text='These are the student files that specifies \n the search operation', fg='black',
                               bg='#FCC653')
        l = ('Comic Sans MS', 13)
        stuStat_label1.config(font=l)
        stuStat_label1.place(x=5, y=1)
        if (value_inside1.get() == 'Average') == True:                                     # if user chose based on avg
            for i in range(0, len(listForSearching)):
                equation2 = i % 2
                if (equation2 != 0):                                  # get the odd indices that have the students AVGs
                    if (value_inside2.get() == 'greater') == True:                                  # if the sign is <
                        if (int(listForSearching[i]) > int(searchentery2.get())): # compare the AVGs with the given avg
                            R_courses = Label(searchSub, relief=RIDGE, text=f"{listForSearching[i - 1]}", fg='white',bg='#f50000')
                            R_courses.place(x=5, y=(50 + (20 * i)))                #to print the result into the window
                            l = ('Comic Sans MS', 12)
                            R_courses.config(font=l)
                    # =======================================================================================================
                    elif (value_inside2.get() == 'less') == True: # if the sign is >
                        if (int(listForSearching[i]) < int(searchentery2.get())): # compare the AVGs with the given avg
                            A1 = Label(searchSub, relief=RIDGE, text=f"{listForSearching[i - 1]}", fg='white', bg='#f50000')
                            A1.place(x=5, y=(50 + (20 * i)))
                            l = ('Comic Sans MS', 12)
                            A1.config(font=l)

                    elif (value_inside2.get() == 'equal') == True: # if the sign is =
                        if (int(listForSearching[i]) == int(searchentery2.get())): # compare the AVGs with the given avg
                            A2 = Label(searchSub, relief=RIDGE, text=f"{listForSearching[i - 1]}", fg='white', bg='#f50000')
                            A2.place(x=5, y=(50 + (20 * i)))
                            l = ('Comic Sans MS', 12)
                            A2.config(font=l)

        elif (value_inside1.get() == 'Taken hours'):                  # if the user chose searching based on taken hours

            for i in range(0, len(listForSearching2)):
                equation2 = i % 2
                if (equation2 == 0):  # get the even indicies that have the taken hours
                    if (value_inside2.get() == 'greater') == True: # if the sign is >
                        if (int(listForSearching2[i - 1]) > int(searchentery2.get())):# compare the taken hours with the given taken hour
                            print(f" the id is {listForSearching2[i]} and the his avg is {listForSearching2[i + 1]}")
                            R_courses = Label(searchSub, relief=RIDGE, text=f"{listForSearching2[i]}", fg='white',
                                              bg='#f50000')
                            R_courses.place(x=5, y=(60 + (20 * i)))
                            l = ('Comic Sans MS', 12)
                            R_courses.config(font=l)

                    # ---------------------------------------------------------------------------------
                    elif (value_inside2.get() == 'less') == True:# if the sign is >
                        if (int(listForSearching2[i - 1]) < int(searchentery2.get())): # compare the taken hours with the given taken hour
                            print(f" the id is {listForSearching2[i]} and the his avg is {listForSearching2[i + 1]}")
                            R_courses = Label(searchSub, relief=RIDGE, text=f"{listForSearching2[i]}", fg='white',
                                              bg='#f50000')
                            R_courses.place(x=5, y=(60 + (20 * i)))
                            l = ('Comic Sans MS', 12)
                            R_courses.config(font=l)

                        # ---------------------------------------------------------------------------------
                    elif (value_inside2.get() == 'equal') == True:# if the sign is =
                        if (int(listForSearching2[i - 1]) == int(searchentery2.get())): # compare the taken hours with the given taken hour
                            print(f" the id is {listForSearching2[i]} and the his avg is {listForSearching2[i + 1]}")
                            R_courses = Label(searchSub, relief=RIDGE, text=f"{listForSearching2[i]}", fg='white',
                                              bg='#f50000')
                            R_courses.place(x=5, y=(60 + (20 * i)))
                            l = ('Comic Sans MS', 12)
                            R_courses.config(font=l)

# --------------------------------------------------------------------------------
# This function is for the RESET button to clear all the entry boxes easily to let the user add a new information
def clearButton():
    global eId
    global eyear
    global eCourse

    eId.delete(0, 'end')   # set the value of the entry to 0 (empty)
    eyear.delete(0, 'end')
    eCourse.delete(0, 'end')
    semester.set('Semester:')
# --------------------------------------------
# This function is for the submit button to get the option number of the main menu of the ADMIN
def okbutton():
    global e3
    global Input
    global eId
    global eyear
    global semester
    global eCourse
    global Input
    global identery
    global idwindow
    global stuWindow
    global FileName
    global IDFileCourseNames
    global studentsAvg

    # -------------------------------OPTION 1----------------------------------------------
    if e3.get() == '1': # if the option is 1 do the following

        idwindow = Tk()
        idwindow.geometry('220x155')
        enterId = Label(idwindow, relief=RIDGE, text='Enter the Id number:', fg='white', bg='#7E3AA1')
        l = ('Comic Sans MS', 14)
        enterId.config(font=l)
        enterId.place(x=10, y=10)

        identery = Entry(idwindow)
        button1 = Button(idwindow, width=20, height=1, text="Press to create text file", command=creatFile)
        identery.pack()
        button1.pack()
        button1.place(x=25, y=90)
        identery.place(x=35, y=55)

        idwindow.mainloop()  # to let the TK window be shown

    elif e3.get() == '2':
        global semester

        stuWindow = Tk()
        stuWindow.title(' Student Information ')
        stuWindow.geometry('360x380')
        stuWindow.resizable(0, 0)
        welcome = Label(stuWindow, relief=RIDGE, text='Please enter the following information:', fg='white',
                        bg='#472747')
        l = ('Comic Sans MS', 14)
        welcome.config(font=l)
        welcome.place(x=7, y=1)
        # ======================================================
        Id1 = Label(stuWindow, text='File name *')
        o = ('Time New Roman', 12)
        Id1.config(font=o)
        Id1.place(x=7, y=60)

        Id2 = Label(stuWindow, text='Enter the file name as the format (id) only')
        o = ('Time New Roman', 7)
        Id2.config(font=o)
        Id2.place(x=5, y=80)

        eId = Entry(stuWindow, width=15, border=2)
        eId.grid(sticky=W, columnspan=2)
        l = ('Time New Roman', 12)
        eId.config(font=l)
        eId.place(x=140, y=60)
        # ======================================================
        year = Label(stuWindow, text=' Year *', font='Helvetica 18 bold')
        o = ('Time New Roman', 12)
        year.config(font=o)
        year.place(x=7, y=105)

        yearnote = Label(stuWindow, text='Add yearas the following format: 2021-2022*', font='Helvetica 18 bold')
        o = ('Time New Roman', 7)
        yearnote.config(font=o)
        yearnote.place(x=7, y=125)

        eyear = Entry(stuWindow, width=15, border=2)
        eyear.grid(sticky=W, columnspan=2)
        l = ('Time New Roman', 12)
        eyear.config(font=l)
        eyear.place(x=140, y=105)
        # ======================================================
        # combo box to let the user choose an option from
        options_list1 = ["1", "2", "3"]   # option list of the semster

        # Variable to keep track of the option
        # selected in OptionMenu
        semester = tkinter.StringVar(stuWindow)

        # Set the default value of the option list from outside
        semester.set("Semester:")

        # Create the optionmenu widget and passing the options_list and value_inside to it.
        question_menu1 = tkinter.OptionMenu(stuWindow, semester, *options_list1)
        question_menu1.place(x=150, y=150)
        # ======================================================

        course = Label(stuWindow, text='Add Courses and their grades as the following'
                                       '\n format: Encs2380 81, Encs2210 87  *')
        o = ('Time New Roman', 12)
        course.config(font=o)
        course.place(x=7, y=200)

        eCourse = Entry(stuWindow, width=35, border=4)
        eCourse.grid(sticky=W, columnspan=2)

        l = ('Time New Roman', 13)
        eCourse.config(font=l)
        eCourse.place(x=7, y=260)
        # ======================================================
        SubmitButt = Button(stuWindow, text="Submit", width=15, height=2, command=submit) # submit button settings
        SubmitButt.place(x=180, y=310)

        Reset = Button(stuWindow, text="Reset", width=15, height=2, command=clearButton) # Reset button settings
        Reset.place(x=40, y=310)
        stuWindow.mainloop()
    # -------------------------------OPTION 3----------------------------------------------
    elif e3.get() == '3':
        global updateWindow
        global update_eId
        global update_eyear
        global old_Ecourse_grade
        global new_Ecourse_grade

        updateWindow = Tk()
        updateWindow.title('Update Student Information ')
        updateWindow.geometry('390x400')
        updateWindow.resizable(0, 0)
        update_label1 = Label(updateWindow, relief=RIDGE, text='Please enter the old and new:', fg='white',
                              bg='#472747')
        l = ('Comic Sans MS', 14)
        update_label1.config(font=l)
        update_label1.place(x=7, y=1)
        # ======================================================
        updateId1 = Label(updateWindow, text='File name to be updated')
        o = ('Time New Roman', 12)
        updateId1.config(font=o)
        updateId1.place(x=7, y=60)

        updateId2 = Label(updateWindow, text='Enter the file name as the format (id.txt)')
        o = ('Time New Roman', 8)
        updateId2.config(font=o)
        updateId2.place(x=5, y=80)

        update_eId = Entry(updateWindow, width=20, border=2)
        update_eId.grid(sticky=W, columnspan=2)
        l = ('Time New Roman', 12)
        update_eId.config(font=l)
        update_eId.place(x=185, y=60)
        # ======================================================
        Frame(updateWindow, width=350, height=2, bg='#82A19E').place(x=12, y=103)

        old_course_grade = Label(updateWindow,
                                 text='Add old course and its old grade as the following\nformat: Encs2380 81 *')
        o = ('Time New Roman', 12)
        old_course_grade.config(font=o)
        old_course_grade.place(x=3, y=110)

        old_Ecourse_grade = Entry(updateWindow, width=40, border=4)
        old_Ecourse_grade.grid(sticky=W, columnspan=2)

        l = ('Time New Roman', 13)
        old_Ecourse_grade.config(font=l)
        old_Ecourse_grade.place(x=10, y=170)
        # ======================================================
        new_course_grade = Label(updateWindow,
                                 text='Add new course and its new grade as the following\n format: Encs2130 98  *')
        o = ('Time New Roman', 12)
        new_course_grade.config(font=o)
        new_course_grade.place(x=3, y=220)

        new_Ecourse_grade = Entry(updateWindow, width=40, border=4)
        new_Ecourse_grade.grid(sticky=W, columnspan=2)

        l = ('Time New Roman', 13)
        new_Ecourse_grade.config(font=l)
        new_Ecourse_grade.place(x=10, y=280)

        # ======================================================
        UpdateButt = Button(updateWindow, text="Update", width=15, height=2, command=Update)
        UpdateButt.place(x=125, y=330)

    # -------------------------------OPTION 4-----------------------------------------------

    elif e3.get() == '4':
        global stuStatWindow
        global studentStat_eId
        global AvgPerSemester
        global RemainCoursesWindow

        stuStatWindow = Tk()
        stuStatWindow.title('Student Statistics ')
        stuStatWindow.geometry('420x650')
        stuStatWindow.resizable(0, 0)
        stuStat_label1 = Label(stuStatWindow, relief=RIDGE, text='   Welcome To Student Statistics Window', fg='white',
                               bg='#472747')
        l = ('Comic Sans MS', 15)
        stuStat_label1.config(font=l)
        stuStat_label1.place(x=7, y=1)
        # ======================================================
        stuStatId1 = Label(stuStatWindow, text='File name to be updated')
        o = ('Time New Roman', 12)
        stuStatId1.config(font=o)
        stuStatId1.place(x=7, y=60)

        stuStatId2 = Label(stuStatWindow, text='Enter the file name as the format (id.txt)')
        o = ('Time New Roman', 8)
        stuStatId2.config(font=o)
        stuStatId2.place(x=5, y=80)

        studentStat_eId = Entry(stuStatWindow, width=20, border=2)
        studentStat_eId.grid(sticky=W, columnspan=2)
        l = ('Time New Roman', 12)
        studentStat_eId.config(font=l)
        studentStat_eId.place(x=185, y=60)
        # ======================================================

        StatStudentButton = Button(stuStatWindow, text="Show", width=10, height=1, command=StudentStatADMINFunc)
        StatStudentButton.place(x=280, y=90)

        StatStudentButton = Button(stuStatWindow, text="Remaining Courses", width=15, height=1,
                                   command=RemainingCourses4ADMIN)
        StatStudentButton.place(x=260, y=120)


    # -------------------------------OPTION 5----------------------------------------------

    elif e3.get() == '5':
        global gloStatWindow

        gloStatWindow = Tk()
        gloStatWindow.title('Student Statistics ')
        gloStatWindow.geometry('500x300')
        gloStatWindow.resizable(0, 0)
        gloStat_label1 = Label(gloStatWindow, relief=RIDGE, text='   Welcome To Global Statistics Window', fg='white',
                               bg='#472747')
        l = ('Comic Sans MS', 15)
        gloStat_label1.config(font=l)
        gloStat_label1.place(x=7, y=1)
        # ======================================================
        StatStudentButton1 = Button(gloStatWindow, text="Show overall students average", width=30, height=1, command=globalStatistics)
        StatStudentButton1.place(x=100, y=50)
        StatStudentButton2 = Button(gloStatWindow, text="Show average hours per semester", width=30, height=1, command=avgHourPerSem)
        StatStudentButton2.place(x=100, y=80)
        histogramButton = Button(gloStatWindow, text="Histogram", width=30, height=1, command=histogram)
        histogramButton.place(x=100, y=110)

    # -------------------------------OPTION 6----------------------------------------------

    elif e3.get() == '6':
        global value_inside1
        global value_inside2
        global searchentery2
        global search

        search = Tk()
        search.title('Student Statistics ')
        search.geometry('320x320')
        search.resizable(0, 0)
        searchLabel1 = Label(search, relief=RIDGE, text='Searching Window', fg='white', bg='#472747')
        l = ('Comic Sans MS', 15)
        searchLabel1.config(font=l)
        searchLabel1.place(x=7, y=1)

        searchLabel2 = Label(search, relief=RIDGE, text='value to compare')
        l = ('Time New Roman', 11)
        searchLabel2.config(font=l)
        searchLabel2.place(x=5, y=200)

        searchentery2 = Entry(search, width=20, border=2)
        searchentery2.grid(sticky=W, columnspan=2)
        l = ('Time New Roman', 12)
        searchentery2.config(font=l)
        searchentery2.place(x=130, y=200)

        # Create the list of options in the searching window
        options_list1 = ["Average", "Taken hours"]
        options_list2 = ["greater", "less", "equal"]

        # Variable to keep track of the option selected in OptionMenu
        value_inside1 = tkinter.StringVar(search)
        value_inside2 = tkinter.StringVar(search)

        # Set the default value of the variable
        value_inside1.set("Searching based on:")
        value_inside2.set("Select sign:")

        # Create the optionmenu widget and passing the options_list and value_inside to it.
        question_menu1 = tkinter.OptionMenu(search, value_inside1, *options_list1)
        question_menu1.place(x=100, y=60)

        question_menu2 = tkinter.OptionMenu(search, value_inside2, *options_list2)
        question_menu2.place(x=115, y=110)


       #submit button in the searching window
        submit_button = tkinter.Button(search, text='Submit', width=10, border=3, command=SearchSubmit)
        submit_button.place(x=200, y=270)

        search.mainloop()
    # ------------if the user enter a unvalid entry error will be shown----------------------------------
    else:
        messagebox.showinfo("Error", "Invalid number!")

# -------------------------------LOGIN info Labels and entry boxes settings ----------------------------------------------

l1 = Label(w, text='Username', bg='white')
l = ('Time New Roman', 12)
l1.config(font=l)
l1.place(x=150, y=170)

# e1 entry for username entry
e1 = Entry(w, width=20, border=0)
l = ('Time New Roman', 12)
e1.config(font=l)
e1.place(x=90, y=200)

# e2 entry for password entry
e2 = Entry(w, width=20, border=0, show='*')
e2.config(font=l)
e2.place(x=90, y=290)

l2 = Label(w, text='Password', bg='white')
l = ('Time New Roman', 12)
l2.config(font=l)
l2.place(x=150, y=260)

Frame(w, width=200, height=2, bg='#141414').place(x=90, y=310)
Frame(w, width=200, height=2, bg='#141414').place(x=90, y=220)

pic = PhotoImage(file="secure.png")  # add image into the window
label1 = Label(w, image=pic, border=0, justify=CENTER)  # set the image as a label
label1.place(x=135, y=25)  # set the image place by x and y

# ------------------------------------------------------------------------------------------------------------------------
def studentStat():
    global stuStatWindow
    global AvgPerSemester
    global RemainCoursesWindow

    stuStatWindow = Tk()
    stuStatWindow.title('Student Statistics ')
    stuStatWindow.geometry('420x650')
    stuStatWindow.resizable(0, 0)
    stuStat_label1 = Label(stuStatWindow, relief=RIDGE, text='   Welcome To Student Statistics Window', fg='white',
                           bg='#472747')
    l = ('Comic Sans MS', 15)
    stuStat_label1.config(font=l)
    stuStat_label1.place(x=7, y=1)
    # ======================================================
    StatStudentButton = Button(stuStatWindow, text="Show", width=15, height=2, command=StudentStatSTUDENTFunc)
    StatStudentButton.place(x=74, y=60)

    StatStudentButton = Button(stuStatWindow, text="Remaining Courses", width=15, height=2,
                               command=RemainingCourses4StudentStat)
    StatStudentButton.place(x=206, y=60)

def studentGlobal():
    global OverallAVGAllstudents
    globalforstudentWin = Tk()
    globalforstudentWin.title('Student Statistics ')
    globalforstudentWin.geometry('500x300')
    globalforstudentWin.resizable(0, 0)
    globalStat_student = Label(globalforstudentWin, relief=RIDGE, text='   Welcome To Global Statistics Window', fg='white',
                           bg='#472747')
    l = ('Comic Sans MS', 15)
    globalStat_student.config(font=l)
    globalStat_student.place(x=7, y=1)
    # ======================================================

    AVgALL= globalStatistics2()
    print(f'avgall is {AVgALL}')

    hoursAvg = avgHourPerSem2()

    a1 = Label(globalforstudentWin, relief=FLAT, text='The Overall AVG for All students is', fg='white', bg='#472747')
    a1.place(x=20, y=120)
    l = ('Comic Sans MS', 12)
    a1.config(font=l)

    a2 = Label(globalforstudentWin, relief=RIDGE, text=f' {AVgALL} ', fg='white', bg='#1CB044')
    a2.place(x=300, y=120)
    l = ('Comic Sans MS', 12)
    a2.config(font=l)

    a3 = Label(globalforstudentWin, relief=FLAT, text='The average hours of semster (1 , 2 ,3)  are ', fg='white', bg='#472747')
    a3.place(x=20, y=160)
    l = ('Comic Sans MS', 12)
    a3.config(font=l)

    a4 = Label(globalforstudentWin, relief=RIDGE, text=f' {hoursAvg} ', fg='white', bg='#1CB044')
    a4.place(x=350, y=160)
    l = ('Comic Sans MS', 12)
    a4.config(font=l)

    histoButt = Button(globalforstudentWin, text='Show Histogram', width=30, height=2, border=3, command=histogram)
    histoButt.place(x=100, y=60)



# This function will run when user press LOGIN BUTTON to take him to the second (Menu) window
def cmd():
    global eId
    global eyear
    global eCourse
    # global eGrade
    global e3
    global e1

    # ------------------------ if the user is the ADMIN ------------------------------------
    if e1.get() == 'admin' and e2.get() == 'admin':  # Username and password of the admin
        qadmin = Tk()
        qadmin.title(' Admin ')
        qadmin.geometry('390x430')
        qadmin.resizable(0, 0)
        gradient(qadmin)

        Frame(qadmin, width=380, height=155, bg='white').place(x=7, y=60)
        welcome = Label(qadmin, relief=RIDGE, text='Welcome to the admin main menu', fg='white', bg='#472747')

        l = ('Comic Sans MS', 18)
        welcome.config(font=l)
        welcome.place(x=7, y=1)
        # ======================================================
        option0 = Label(qadmin, text='1.Add a new record file', bg='white')
        o = ('Comic Sans MS', 12)
        option0.config(font=o)
        option0.place(x=7, y=60)

        # ======================================================
        option1 = Label(qadmin, text='2.Add new semester with student course and grades', bg='white')
        o = ('Comic Sans MS', 12)
        option1.config(font=o)
        option1.place(x=7, y=85)
        # ======================================================
        option2 = Label(qadmin, text='3.Update', bg='white')
        o = ('Comic Sans MS', 12)
        option2.config(font=o)
        option2.place(x=7, y=110)
        # ======================================================
        option3 = Label(qadmin, text='4.Student statistics', bg='white')
        o = ('Comic Sans MS', 12)
        option3.config(font=o)
        option3.place(x=7, y=135)
        # ======================================================
        option4 = Label(qadmin, text='5.Global statistics', bg='white')
        o = ('Comic Sans MS', 12)
        option4.config(font=o)
        option4.place(x=7, y=160)
        # ======================================================
        option5 = Label(qadmin, text='6.Searching', bg='white')
        o = ('Comic Sans MS', 12)
        option5.config(font=o)
        option5.place(x=7, y=185)
        # ======================================================
        choice = Label(qadmin, text='*ENTER CHOICE NUMBER : ', underline=True, fg='white', bg='#472747')
        o = ('Comic Sans MS', 11)
        choice.config(font=o)
        choice.place(x=15, y=240)
        # ======================================================
        e3 = Entry(qadmin, width=5, border=2)
        l = ('Time New Roman', 11)
        e3.config(font=l)
        e3.place(x=243, y=244)
        # ======================================================

        okbutt = Button(qadmin, text='OK', width=20, height=2, border=3, command=okbutton)
        okbutt.place(x=110, y=300)

        qadmin.mainloop()

    # -------------------------------------------------STUDENT WINDOW -----------------------------------------------
    else:  # ------------------------ username and password of the student ------------------------------
        if (path.exists(e1.get()) == True) and (e2.get() == 'student'): #Username = id.txt of the student || password = student
            qstudent = Tk()
            qstudent.geometry('200x180')
            qstudent.resizable(0, 0)
            qstudent.title(' Student Window ')
            gradient(qstudent)

            StuStat = Button(qstudent, text='Student statistics', width=20, height=2, border=2, command=studentStat)
            GlobalStat = Button(qstudent, text='Global statistics', width=20, height=2, border=3, command=studentGlobal)
            StuStat.place(x=20, y=40)
            GlobalStat.place(x=20, y=110)




            qstudent.mainloop()
        else:
            # if the Id is not exist or data false
            messagebox.showinfo("Error", "Invalid password OR Id is not exist!")

# -------------------------------------------------------------------------
# LOGIN button with its settings
class login:
    def bttn(x, y, text, ecolor, lcolor):
        def on_entera(e):
            myButton1['background'] = ecolor  # ffcc66
            myButton1['foreground'] = lcolor  # 000d33

        def on_leavea(e):
            myButton1['background'] = lcolor
            myButton1['foreground'] = ecolor

        myButton1 = Button(w, text=text, width=20, height=2, fg=ecolor, border=3, bg=lcolor, activeforeground=lcolor,
                           activebackground=ecolor, command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)
        myButton1.place(x=x, y=y)

    bttn(115, 335, 'L O G I N', 'black', '#994422') # creat bttn object of the login class for the login button
    w.mainloop()
# ------------------------------------------------------------------------------------------
