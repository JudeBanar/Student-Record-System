# Importing the libraries needed in amking this Program
import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# Generating the Main Window
window = tkinter.Tk()
window.title("Student Record System")

# Making the title in the Main Window
title = tkinter.Label(text="STUDENT RECORD SYSTEM", font=("Anton 40 bold"))
title.pack()

# This is to configure the spacing of the widgets in the Main Window
for widget in window.winfo_children():
    widget.pack_configure(padx=20, pady=20)


# This add function contains the program that adds the student data to the database
def add():
    # This is to make another window for "Add Students"
    window1 = tkinter.Toplevel()
    window1.title("Add Students")
    window1.config(width=300, height=200)

    # This is to make a frame inside the window where the user inputs data
    frame = tkinter.Frame(window1)
    frame.pack()

    info_frame = tkinter.LabelFrame(frame, text="Student Data")
    info_frame.grid(row=0, column=0, sticky="news", padx=10, pady=10)

    firstname_label = tkinter.Label(info_frame, text="First Name")
    firstname_entry = tkinter.Entry(info_frame)
    firstname_label.grid(row=0, column=0, padx=10, pady=10)
    firstname_entry.grid(row=1, column=0, padx=10, pady=10)

    surname_label = tkinter.Label(info_frame, text="Surname")
    surname_entry = tkinter.Entry(info_frame)
    surname_label.grid(row=0, column=1, padx=10, pady=10)
    surname_entry.grid(row=1, column=1, padx=10, pady=10)

    studno_label = tkinter.Label(info_frame, text="Student Number")
    studno_entry = tkinter.Entry(info_frame)
    studno_label.grid(row=0, column=2, padx=10, pady=10)
    studno_entry.grid(row=1, column=2, padx=10, pady=10)

    course_label = tkinter.Label(info_frame, text="Course")
    course_combobox = ttk.Combobox(info_frame, width=25,
                                   values=["BS in Industrial Engineering", "BS in Electrical Engineering"])
    course_label.grid(row=0, column=3, padx=10, pady=10)
    course_combobox.grid(row=1, column=3, padx=10, pady=10)

    # This function is utilized when the user clicked the next button. This function shows the subjects where the user inputs grades.
    def nxt():
        course = course_combobox.get()

        # This function is utilized if the selected course is IE
        def industrial():

            # This function is used to check if the needed data is complete
            def submit_btn():

                name = firstname_entry.get()
                surname = surname_entry.get()
                studno = studno_entry.get()
                course = course_combobox.get()
                sub1 = float(sub1_entry.get())
                sub2 = float(sub2_entry.get())
                sub3 = float(sub3_entry.get())

                if name == "":
                    messagebox.showerror("Error", "Please input your First Name")
                elif surname == "":
                    messagebox.showerror("Error", "Please input your Last Name")
                elif studno == "":
                    messagebox.showerror("Error", "Please input your Student Number")
                elif course == "":
                    messagebox.showerror("Error", "Please input your Course")
                elif sub1 == "":
                    messagebox.showerror("Error", "Please complete the grades.")
                elif sub2 == "":
                    messagebox.showerror("Error", "Please complete the grades.")
                elif sub3 == "":
                    messagebox.showerror("Error", "Please complete the grades.")
                else:
                    submit()

            # Making Widgets for subjects and grades
            ie_frame = tkinter.LabelFrame(frame, text="Grades")
            ie_frame.grid(row=2, column=0, padx=10, pady=10)

            ie_label = tkinter.Label(ie_frame, text="Input grades(1-5) in the following subjects:")
            ie_label.grid(row=0, column=1, columnspan=2, padx=15, pady=15)

            sub1_label = tkinter.Label(ie_frame, text="Work Study and Measurement (3 units)")
            sub1_entry = tkinter.Entry(ie_frame, width=10)
            sub1_label.grid(row=1, column=1, padx=10, pady=10)
            sub1_entry.grid(row=1, column=2, padx=10, pady=10)

            sub2_label = tkinter.Label(ie_frame, text="Principles of IE (3 units)")
            sub2_entry = tkinter.Entry(ie_frame, width=10)
            sub2_label.grid(row=2, column=1, padx=10, pady=10)
            sub2_entry.grid(row=2, column=2, padx=10, pady=10)

            sub3_label = tkinter.Label(ie_frame, text="Industrial Materials and Processes (3 units)")
            sub3_entry = tkinter.Entry(ie_frame, width=10)
            sub3_label.grid(row=3, column=1, padx=10, pady=10)
            sub3_entry.grid(row=3, column=2, padx=10, pady=10)

            submit_button = tkinter.Button(frame, text="Submit", command=submit_btn)
            submit_button.grid(row=3, columnspan=1, sticky="news", padx=10, pady=10)

            # This is where the inputted data are saved to the database.
            def submit():
                messagebox.showinfo("Success!", "Student added!")

                name = firstname_entry.get()
                surname = surname_entry.get()
                studentno = studno_entry.get()
                sub1 = float(sub1_entry.get())
                sub2 = float(sub2_entry.get())
                sub3 = float(sub3_entry.get())
                ave = ((sub1 * 3) + (sub2 * 3) + (sub3 * 3)) / 9

                # Used to connect the database to the program
                conn = sqlite3.connect('classrec.db')

                # Create a Table in the database
                table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Record_IE
                        (Name TEXT, Surname TEXT, StudentNo INT, Subject1 INT, 
                        Subject2 INT, Subject3 INT, Average INT)
                '''
                conn.execute(table_create_query)

                # Saves the data in the table
                data_insert_query = '''INSERT INTO Student_Record_IE (name, surname, studentno, subject1,
                        subject2, subject3, average) VALUES (?,?,?,?,?,?,?)'''
                data_insert_tuple = (name, surname, studentno, sub1, sub2, sub3, ave)
                cursor = conn.cursor()
                cursor.execute(data_insert_query, data_insert_tuple)
                conn.commit()
                conn.close()

                # Used to terminate the window after submitting
                window1.destroy()

        # This function is utilized if the selected course is EE
        def electrical():

            # This function is used to check if the needed data is complete
            def submit_btn():

                name = firstname_entry.get()
                surname = surname_entry.get()
                studno = studno_entry.get()
                course = course_combobox.get()
                sub1 = float(sub1_entry.get())
                sub2 = float(sub2_entry.get())
                sub3 = float(sub3_entry.get())

                if name == "":
                    messagebox.showerror("Error", "Please input your First Name")
                elif surname == "":
                    messagebox.showerror("Error", "Please input your Last Name")
                elif studno == "":
                    messagebox.showerror("Error", "Please input your Student Number")
                elif course == "":
                    messagebox.showerror("Error", "Please input your Course")
                elif sub1 == "":
                    messagebox.showerror("Error", "Please complete the grades.")
                elif sub2 == "":
                    messagebox.showerror("Error", "Please complete the grades.")
                elif sub3 == "":
                    messagebox.showerror("Error", "Please complete the grades.")
                else:
                    submit()

            # Making Widgets for subjects and grades
            ie_frame = tkinter.LabelFrame(frame, text="Grades")
            ie_frame.grid(row=2, column=0, padx=10, pady=10)

            ie_label = tkinter.Label(ie_frame, text="Input grades(1-5) in the following subjects:")
            ie_label.grid(row=0, column=1, columnspan=2, padx=15, pady=15)

            sub1_label = tkinter.Label(ie_frame, text="Electrical Circuits (3 units)")
            sub1_entry = tkinter.Entry(ie_frame, width=10)
            sub1_label.grid(row=1, column=1, padx=10, pady=10)
            sub1_entry.grid(row=1, column=2, padx=10, pady=10)

            sub2_label = tkinter.Label(ie_frame, text="Electronic Circuits: Devices and Analysis (3 units)")
            sub2_entry = tkinter.Entry(ie_frame, width=10)
            sub2_label.grid(row=2, column=1, padx=10, pady=10)
            sub2_entry.grid(row=2, column=2, padx=10, pady=10)

            sub3_label = tkinter.Label(ie_frame, text="Engineering Electromagnetics (3 units)")
            sub3_entry = tkinter.Entry(ie_frame, width=10)
            sub3_label.grid(row=3, column=1, padx=10, pady=10)
            sub3_entry.grid(row=3, column=2, padx=10, pady=10)

            submit_button = tkinter.Button(frame, text="Submit", command=submit_btn)
            submit_button.grid(row=3, columnspan=1, sticky="news", padx=10, pady=10)

            # This is where the inputted data are saved to the database.
            def submit():
                messagebox.showinfo("Success!", "Student added!")

                name = firstname_entry.get()
                surname = surname_entry.get()
                studentno = studno_entry.get()
                sub1 = float(sub1_entry.get())
                sub2 = float(sub2_entry.get())
                sub3 = float(sub3_entry.get())
                average = ((sub1 * 3) + (sub2 * 3) + (sub3 * 3)) / 9

                # Used to connect the database to the program
                conn = sqlite3.connect('classrec.db')

                # Create a Table in the database
                table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Record_EE
                        (Name TEXT, Surname TEXT, StudentNo INT, Subject1 INT, 
                        Subject2 INT, Subject3 INT, Average INT)
                '''
                conn.execute(table_create_query)

                # Saves the data in the table
                data_insert_query = '''INSERT INTO Student_Record_EE (name, surname, studentno, subject1,
                        subject2, subject3, average) VALUES (?,?,?,?,?,?,?)'''
                data_insert_tuple = (name, surname, studentno, sub1, sub2, sub3, average)
                cursor = conn.cursor()
                cursor.execute(data_insert_query, data_insert_tuple)
                conn.commit()
                conn.close()

                # Used to terminate the window after submitting
                window1.destroy()

        # Condition after the course is selected
        if course == 'BS in Industrial Engineering':
            industrial()

        elif course == 'BS in Electrical Engineering':
            electrical()

    # A button that execute the "nxt" function above.
    next_button = tkinter.Button(frame, text="Next", command=nxt)
    next_button.grid(row=1, columnspan=1, sticky="news", padx=5, pady=5)


# Function that used in deleting a data in IE Course
def delete_ie():
    # Used in creating another Window for delete
    window3 = tkinter.Toplevel()
    window3.title("Delete a data")
    window3.config(width=300, height=200)

    frame = tkinter.Frame(window3)
    frame.pack()

    ie_delete = tkinter.LabelFrame(frame, text="Industrial Engineering")
    ie_delete.grid(row=0, column=0, padx=10, pady=10)

    ie_del_label = tkinter.Label(ie_delete, text="Enter the Student No. and Surname\nof the record you want to delete.")
    ie_del_label.grid(row=0, column=0, padx=10, pady=10)

    studno_label = tkinter.Label(ie_delete, text="Student No.")
    studno_label.grid(row=1, column=0, padx=10, pady=10)

    studno_del = tkinter.Entry(ie_delete, )
    studno_del.grid(row=2, column=0, padx=10, pady=10)

    # Function that deleted the chosen data in the database
    def del_student():
        conn = sqlite3.connect('classrec.db')

        studentno = studno_del.get()

        delete_statement = "DELETE FROM Student_Record_IE WHERE studentno=?"

        conn.execute(delete_statement, (studentno,))

        conn.commit()

        messagebox.showinfo("Success", "Data Deleted\nRestart the List Window to see changes.")

        window3.destroy()

    # Button that execute the "del_student" function when clicked
    del_button = tkinter.Button(ie_delete, text="Delete", command=del_student)
    del_button.grid(row=5, column=0, padx=10, pady=10)


# Function that used in deleting a data in IE Course
def delete_ee():
    # Used in creating another Window for delete
    window3 = tkinter.Toplevel()
    window3.title("Delete a data")
    window3.config(width=300, height=200)

    frame = tkinter.Frame(window3)
    frame.pack()

    ee_delete = tkinter.LabelFrame(frame, text="Electrical Engineering")
    ee_delete.grid(row=0, column=0, padx=10, pady=10)

    ee_del_label = tkinter.Label(ee_delete, text="Enter the Student No. and Surname\nof the record you want to delete.")
    ee_del_label.grid(row=0, column=0, padx=10, pady=10)

    studno_label = tkinter.Label(ee_delete, text="Student No.")
    studno_label.grid(row=1, column=0, padx=10, pady=10)

    studno_del = tkinter.Entry(ee_delete, )
    studno_del.grid(row=2, column=0, padx=10, pady=10)

    # Function that deleted the chosen data in the database
    def del_student():
        conn = sqlite3.connect('classrec.db')

        studentno = studno_del.get()

        delete_statement = "DELETE FROM Student_Record_EE WHERE studentno=?"

        conn.execute(delete_statement, (studentno,))

        conn.commit()

        messagebox.showinfo("Success", "Data Deleted\nRestart the List Window to see changes.")

        window3.destroy()

    # Button that execute the "del_student" function when clicked
    del_button = tkinter.Button(ee_delete, text="Delete", command=del_student)
    del_button.grid(row=5, column=0, padx=10, pady=10)


# Function for the "List" window
def list():
    # Making another window for the List
    window2 = tkinter.Toplevel()
    window2.title("Class List")
    window2.config(width=300, height=200)

    # making the frame for deleting a student
    frame = tkinter.Frame(window2)
    frame.pack()

    delete_frame = tkinter.LabelFrame(frame, text="Delete Data")
    delete_frame.grid(row=0, column=0, padx=10, pady=10)

    ie_delete = tkinter.Button(delete_frame, text="Delete a data in IE", command=delete_ie)
    ee_delete = tkinter.Button(delete_frame, text="Delete a data in EE", command=delete_ee)
    ie_delete.grid(row=0, column=0, padx=10, pady=10)
    ee_delete.grid(row=0, column=1, padx=10, pady=10)

    # To style the tabel in the List window
    style = ttk.Style()

    style.theme_use('default')

    style.configure("Treeview",
                    background="#D3D3D3",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#D3D3D3"
                    )

    # Function to show the table of IE and the data in it.
    def ie():
        global records_ie

        tree_frame1 = tkinter.LabelFrame(frame, text="Industrial Engineering")
        tree_frame1.grid(row=2, column=0)

        tree_scroll = tkinter.Scrollbar(tree_frame1)
        tree_scroll.pack(side="right", fill="y")

        my_tree = ttk.Treeview(tree_frame1, yscrollcommand=tree_scroll.set, selectmode="extended")
        my_tree.pack()

        # This sets the appearance of the tabel in the window
        tree_scroll.config(comman=my_tree.yview)

        my_tree['columns'] = ("Surname", "Name", "Student No.", "Work Study and Measurement", "Principles of IE",
                              "Industrial Materials and Processes", "GPA")

        my_tree.column('#0', width=0, stretch=0)
        my_tree.column("Surname", anchor='center', width=90)
        my_tree.column("Name", anchor='center', width=90)
        my_tree.column("Student No.", anchor='center', width=80)
        my_tree.column("Work Study and Measurement", anchor='center', width=190)
        my_tree.column("Principles of IE", anchor='center', width=100)
        my_tree.column("Industrial Materials and Processes", anchor='center', width=200)
        my_tree.column("GPA", anchor='center', width=50)

        my_tree.heading("#0", text="", anchor='w')
        my_tree.heading("Surname", text="Surname", anchor='center')
        my_tree.heading("Name", text="Name", anchor='center')
        my_tree.heading("Student No.", text="Student No.", anchor='center')
        my_tree.heading("Work Study and Measurement", text="Work Study and Measurement", anchor='center')
        my_tree.heading("Principles of IE", text="Principles of IE", anchor='center')
        my_tree.heading("Industrial Materials and Processes", text="Industrial Materials and Processes",
                        anchor='center')
        my_tree.heading("GPA", text="GPA", anchor='center')

        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="light green")

        # To access the data in the database
        conn = sqlite3.connect('classrec.db')

        c = conn.cursor()

        c.execute("SELECT * FROM Student_Record_IE")
        records_ie = c.fetchall()

        conn.commit()

        conn.close()

        count = 0

        # Sets the position of the data in the table
        for record in records_ie:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[0], record[2], record[3], record[4], record[5], record[6]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[0], record[2], record[3], record[4], record[5], record[6]),
                               tags=('oddrow',))

            count += 1

    # Function to show the table of IE and the data in it.
    def ee():

        global records_ee

        tree_frame1 = tkinter.LabelFrame(frame, text="Electrical Engineering")
        tree_frame1.grid(row=3, column=0)

        tree_scroll = tkinter.Scrollbar(tree_frame1)
        tree_scroll.pack(side="right", fill="y")

        my_tree = ttk.Treeview(tree_frame1, yscrollcommand=tree_scroll.set, selectmode="extended")
        my_tree.pack()

        # This sets the appearance of the tabel in the window
        tree_scroll.config(comman=my_tree.yview)

        my_tree['columns'] = (
        "Surname", "Name", "Student No.", "Electrical Circuit", "Electronic Circuit: Device and Analysis",
        "Engineering Electromagnetics", "GPA")

        my_tree.column('#0', width=0, stretch=0)
        my_tree.column("Surname", anchor='center', width=90)
        my_tree.column("Name", anchor='center', width=90)
        my_tree.column("Student No.", anchor='center', width=70)
        my_tree.column("Electrical Circuit", anchor='center', width=100)
        my_tree.column("Electronic Circuit: Device and Analysis", anchor='center', width=220)
        my_tree.column("Engineering Electromagnetics", anchor='center', width=200)
        my_tree.column("GPA", anchor='center', width=50)

        my_tree.heading("#0", text="", anchor='w')
        my_tree.heading("Surname", text="Surname", anchor='center')
        my_tree.heading("Name", text="Name", anchor='center')
        my_tree.heading("Student No.", text="Student No.", anchor='center')
        my_tree.heading("Electrical Circuit", text="Electrical Circuit", anchor='center')
        my_tree.heading("Electronic Circuit: Device and Analysis", text="Electronic Circuit: Device and Analysis",
                        anchor='center')
        my_tree.heading("Engineering Electromagnetics", text="Engineering Electromagnetic", anchor='center')
        my_tree.heading("GPA", text="GPA", anchor='center')

        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="light blue")

        # To access the data in the database
        conn = sqlite3.connect('classrec.db')

        c = conn.cursor()

        c.execute("SELECT * FROM Student_Record_EE")
        records_ee = c.fetchall()

        conn.commit()

        conn.close()

        count = 0

        # Sets the position of the data in the table
        for record in records_ee:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[0], record[2], record[3], record[4], record[5], record[6]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[0], record[2], record[3], record[4], record[5], record[6]),
                               tags=('oddrow',))

            count += 1

    # To show the table in the List Window
    ie()
    ee()


# Buttons in Main Window
record_button = tkinter.Button(window, text="Add Student", command=add)  # Button to execute the "add" function above
list_button = tkinter.Button(window, text="View List", command=list)  # Button to execute the "list" function above
record_button.pack(padx=100, pady=20)
list_button.pack(padx=100, pady=20)

# To execute the main Window
window.mainloop()
