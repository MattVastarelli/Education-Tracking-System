from Source import forms
import tkinter as tk
import os

data = [1,2,3,4]
btn_list = list()

top = tk.Tk()
top.geometry("350x150")

# main frame
frame = tk.Frame(top)
frame.pack()

# frames
itter_frame = tk.Frame(frame)
itter_frame.pack()

for item in data:
    btn_list.append(tk.Button(itter_frame, text="New Btn", command=""))

for item in btn_list:
    item.pack(padx=2)

tk.mainloop()

"""
view class types
add new classes
"""


"""
script_dir = os.path.dirname(__file__)  # absolute dir the script is in
rel_path = "db/test.txt"
abs_file_path = os.path.join(script_dir, rel_path)

return_list = list()

with open(abs_file_path) as f:
    content = f.readlines()
    content = [x.strip() for x in content]

    for line in content:
        split = line.split()  # choose split type
        if split[0]  == str(1):
            return_list = line.split()
            break
    f.close()



    print(return_list)
"""





'''
Process to handle form 

1 create instance
2 call the method to receive the top level object
3 add the buttons to the frame that use the methods you want 
    to use to grab the data from the attributes of the From class 
4 process the data in the correct object
5 direct user to the correct view
'''
#d = forms.Form()  # create instance
#top = d.view_institution(0, None)  # call the method to receive the top level obj


# declaration of local func
def foobar(form_instace, data):

    # process the data
    # do what you want with the forms
    print(data)

    return None


'''
add the buttons you want to the frame to use the methods you want
to use to check the data
'''

"""
button_frame = tk.Frame(top)
button_frame.pack()

save_button = tk.Button(button_frame, text="Save", command= lambda: foobar(d.get_login_data()))
save_button.pack(side=tk.LEFT)

close_button = tk.Button(button_frame, text="Close", command=top.destroy)
close_button.pack(side=tk.LEFT)
"""


#top.mainloop()  # run the code

"""
script_dir = os.path.dirname(__file__)  # absolute dir the script is in
rel_path = "db/info.txt"
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path, 'r')
print(file.readlines())
file.close()

"""

"""
 # private
    def __viewStudent(self, studentname):
        # What an Educator sees on a Student's profile
        # passed in argument is student's full name
        searchlist = []

        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/students.txt"
        abs_file_path = os.path.join(script_dir, rel_path)

        # processing the rows of the file to find correct Institute account info
        file = open(abs_file_path, 'r')
        readrows = csv.reader(file, delimiter='\t')
        for row in readrows:
            searchlist.append(row)
        file.close()

        # searching for row with matching name
        index = 0
        for record in searchlist:
            name = record[4] + ' ' + record[5]
            if name == studentname:
                break
            index += 1

        StudForm = [1, 0]
        # want to add items 4, 5, 10, 11, 12 from list at indicated index to StudForm
        StudForm.append(name)
        for i in range(10, 13):
            StudForm.append(searchlist[index][i])

        # returns list: [viewer profile access level, viewed profile access level, Student Name,
        # Current Grade Level, Grades, Grade Notes]
        return StudForm

    # private
    def __viewInstitution(self, instname):
        # What an Educator sees on an Institution's profile
        searchlist = []

        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/institutions.txt"
        abs_file_path = os.path.join(script_dir, rel_path)

        # processing in the rows of the file
        file = open(abs_file_path, 'r')
        readRows = csv.reader(file,delimiter='\t')
        for row in readRows:
            searchlist.append(row)
        file.close()

        # searching for row with matching name
        index = 0
        for record in searchlist:
            if record[4] == instname:
                break
            index += 1

        InstForm = [1, 0]
        # want to add items 4, 5, 6, 7, 8, 9 from list at indicated index to InstForm
        for i in range(4,10):
            InstForm.append(searchlist[index][i])

        # returns list: [viewer profile access level, viewed profile access level, Institute Name,
        # Institute Address, Institute Type, min Grade Level, max Grade Level, Phone Number]
        return InstForm

"""


