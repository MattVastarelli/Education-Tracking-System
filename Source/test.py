from Source import forms
import tkinter as tk
import os

"""
login
view class types
add new classes

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
d = forms.Form()  # create instance
top = d.add_new(access_level=2)  # call the method to receive the top level obj

'''
add the buttons you want to the frame to use the methods you want
to use to check the data
'''
button_frame = tk.Frame(top)
button_frame.pack()

save_button = tk.Button(button_frame, text="Save", command=None)
save_button.pack(side=tk.LEFT)

close_button = tk.Button(button_frame, text="Close", command=top.destroy)
close_button.pack(side=tk.LEFT)


#top.mainloop()  # run the code

script_dir = os.path.dirname(__file__)  # absolute dir the script is in
rel_path = "db/info.txt"
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path, 'r')
file.close()

print(file.readlines())
