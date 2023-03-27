import tkinter as tk
import pyodbc

class Login:
    def __init__(self):
        self.main_window = tk.Tk()

        self.main_window.geometry("300x150")
        self.main_window.title("SQL Server Login")

        self.login_frame = tk.Frame(self.main_window)
        self.password_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)

        self.login_label = tk.Label(self.login_frame,text = "Login",width= 10)
        self.login_entry = tk.Entry(self.login_frame,width = 20)

        self.login_label.pack(side = "left")
        self.login_entry.pack(side = "left")

        self.pass_label = tk.Label(self.password_frame,text = "Password",width=10)
        self.pass_entry = tk.Entry(self.password_frame,show = "*",width = 20)
        
        self.pass_label.pack(side = "left")
        self.pass_entry.pack(side = "left")

        self.button = tk.Button(self.button_frame,text = "Login",command = self.access_database)
        
        self.button.pack()
        self.login_frame.pack()
        self.password_frame.pack()
        self.button_frame.pack()

        tk.mainloop()

    # def confirm (self):
    #     tkinter.messagebox.showinfo("Confirmation","Thank you ")

    #     self.main_window.destroy()

    def access_database(self):

        login = self.login_entry.get()
        password = self.pass_entry.get()

        self.main_window.destroy()

        login = "caleb_buchanan1"
        password = "MIS4322student"
        
        preList = {}
        courseList = []
        cn_str = (
    
    'Driver={SQL Server Native Client 11.0};'

    'Server=MIS-SQLJB;'

    'Database=School;'

    'UID='+login+';'

    'PWD='+password+';'

    )

        cn = pyodbc.connect(cn_str)

        cursor = cn.cursor()
        cursor.execute('select * from School.dbo.Course')

        data = cursor.fetchall()

        for course in data:
            courseID = course[0]
            title =  course[1]
            credits = course[2]
            deptID = course[3]
            preList = {'CourseID': courseID, 'Title': title, 'Credits': credits, 'DeptID': deptID}

            courseList.append(preList)

            #print(courseList)

        a = int(input('Enter Course ID: '))

        for dictionary in courseList:
            if a == dictionary['CourseID']:
                print(f'Title: {dictionary["Title"]}')
                print(f'Credits: {dictionary["Credits"]}')
                print(f'Dept ID: {dictionary["DeptID"]}')



'''
        for course in data:
            print("Course ID:      ", course[0])
            print("Course Name:    ", course[1])
            print("Credit Hours:   ", course[2])
            print("Department ID:  ", course[3])
            print()

        #print(data)
'''

x = Login()
print(x)
