from PasswordManager import *
import string
from random import randint, shuffle, sample, choices

#Fill in your Main Program Here = PasswordManager("Student", 'Final')
test = PasswordManager('Student', 'FINAL')
test.add_password('www.gmail.com', 'a_student')
test.add_password('www.wm.edu', 'WMstudent', criteria = {'max_spec': 2, 'min_upper': 2})
test.change_password('www.gmail.com', 'Final',new_pass = 'update1235')
test.get_site_info('www.wm.edu')
