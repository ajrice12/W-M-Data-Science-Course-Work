import unittest
import pandas as pd
from PasswordManager import *

#Test with a private Message class

class Functions_Tester(unittest.TestCase):

  def setUp(self):
    self.__password = PasswordManager('TestCases','only_a_test')# name and mp
  
  def test_invalid_specs(self):
    print('\nTest add_password invalid specs\n')
    try:
        criteria = {'repeat':False,'min_spec':5, 'spec_char':'*&^'}
        self.__password.add_password('www.google.com', 'a_student', criteria)
        self.assertEqual(self.__password.get_site_list(),[])
    except BaseException as e:
            print('Testing failed')
            print(e)

  def test_invalid_specs_2(self):
    print('\nTest add_password invalid specs 2\n')
    try:
        criteria = {'min_spec':5, 'min_num':5, 'min_upper':7}
        self.__password.add_password('www.google.com', 'a_student',criteria)
        self.assertEqual(self.__password.get_site_list(),[])
    except BaseException as e:
            print('Testing failed')
            print(e)

  def test_add(self):
    print('\nTest add_password\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.assertEqual(self.__password.get_site_list(), ['www.google.com'])
    except BaseException as e:
        print('Testing failed')
        print(e)    

  def test_add_mult(self):
    print('\nTest add_password multiple\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)


  def test_add_exists(self):
    print('\nTest add_password site exists\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.__password.add_password('www.wm.edu', 'its_me')
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)
                

  def test_criteria_choose_min(self):
    print('\nTest add_password criteria choose min\n')
    criteria = {'length':10, 'min_spec':1, 'max_spec':5, 'min_num':4, 'min_upper':3}
    try:
        self.__password.add_password('www.google.com', 'a_student',criteria)
        self.assertEqual(self.__password.get_site_list(),['www.google.com'])
        print(self.__password.get_site_info('www.google.com'))
    except BaseException as e:
            print('Testing failed')
            print(e)

  def test_validate_True(self):
    print('\nTest validate True\n')
    try:
        result = self.__password.validate('only_a_test')
        self.assertEqual(result, True)
    except BaseException as e:
            print('Testing failed')
            print(e)


  def test_validate_False(self):
    print('\nTest validate False\n')
    try:
        result = self.__password.validate('Only_a_Test')
        self.assertEqual(result, False)
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_criteria_choose_min(self):
    print('\nTest add_password criteria choose min\n')
    criteria = {'length':10, 'min_spec':1, 'max_spec':5, 'min_num':4, 'min_upper':5}
    try:
        self.__password.add_password('www.google.com', 'a_student',criteria)
        self.assertEqual(self.__password.get_site_list(),['www.google.com'])
        print(self.__password.get_site_info('www.google.com'))
    except BaseException as e:
            print('Testing failed')
            print(e)

  def test_change_no_validate(self):
    print('\nTest change no validate\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        print(self.__password.get_site_info('www.google.com'))
        self.__password.change_password('www.google.com', 'one_pass')
        self.assertEqual(self.__password.get_site_list(),['www.google.com'])
        print(self.__password.get_site_info('www.google.com'))
    except BaseException as e:
            print('Testing failed')
            print(e)

  def test_change_invalid_criteria(self):
    print('\nTest change invalid criteria\n')
    criteria = {'repeat':False,'min_spec':5, 'spec_char':'*&^'}
    try: 
        self.__password.add_password('www.google.com', 'a_student')
        print(self.__password.get_site_info('www.google.com'))
        self.__password.change_password('www.google.com', 'only_a_test', criteria = criteria)
        self.assertEqual(self.__password.get_site_list(),['www.google.com'])
        print(self.__password.get_site_info('www.google.com'))
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_add_one_change_one(self):
    print('\nTest change_password one\n')
    try:
        self.__password.add_password('www.wm.edu', 'this_student')
        print(self.__password.get_site_info('www.wm.edu'))
        self.__password.change_password('www.wm.edu', 'only_a_test')
        print(self.__password.get_site_info('www.wm.edu'))
        self.assertEqual(self.__password.get_site_list(),[ 'www.wm.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_add_mult_change_one(self):
    print('\nTest change_password add multiple change one\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        print(self.__password.get_site_info('www.wm.edu'))
        self.__password.change_password('www.wm.edu', 'only_a_test')
        print(self.__password.get_site_info('www.wm.edu'))
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_add_mult_change_mult(self):
    print('\nTest change_password multiple\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.__password.add_password('www.william.edu', 'william')
        print(self.__password.get_site_info('www.wm.edu'))
        self.__password.change_password('www.wm.edu', 'only_a_test')
        print(self.__password.get_site_info('www.wm.edu'))
        print(self.__password.get_site_info('www.mary.edu'))
        self.__password.change_password('www.mary.edu', 'only_a_test')
        print(self.__password.get_site_info('www.mary.edu'))
        self.__password.change_password('www.wm.edu', 'only_a_test')
        print(self.__password.get_site_info('www.wm.edu'))
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu', 'www.william.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_add_one_change_one_new_pass(self):
    print('\nTest change_password one_new_pass\n')
    try:
        self.__password.add_password('www.wm.edu', 'this_student')
        print(self.__password.get_site_info('www.wm.edu'))
        self.__password.change_password('www.wm.edu', 'only_a_test', new_pass = 'a_new_password')
        print(self.__password.get_site_info('www.wm.edu'))
        self.assertEqual(self.__password.get_site_info('www.wm.edu')[1], 'a_new_password')
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_change_twice(self):
    print('\nTest change_password twice\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.__password.add_password('www.william.edu', 'william')
        print(self.__password.get_site_info('www.mary.edu'))
        self.__password.change_password('www.mary.edu', 'only_a_test')
        print(self.__password.get_site_info('www.mary.edu'))
        self.__password.change_password('www.mary.edu', 'only_a_test')
        print(self.__password.get_site_info('www.mary.edu'))
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu', 'www.william.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_change_twice_one_fail(self):
    print('\nTest change_password twice\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.__password.add_password('www.william.edu', 'william')
        print(self.__password.get_site_info('www.mary.edu'))
        self.__password.change_password('www.mary.edu', 'a_test')
        print(self.__password.get_site_info('www.mary.edu'))
        self.__password.change_password('www.mary.edu', 'only_a_test')
        print(self.__password.get_site_info('www.mary.edu'))
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu', 'www.william.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_change_twice_diff_ways(self):
    print('\nTest change_password twice\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.__password.add_password('www.william.edu', 'william')
        print(self.__password.get_site_info('www.mary.edu'))
        self.__password.change_password('www.mary.edu', 'only_a_test')
        print(self.__password.get_site_info('www.mary.edu'))
        self.__password.change_password('www.mary.edu', 'only_a_test', new_pass = '12345678')
        print(self.__password.get_site_info('www.mary.edu'))
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu', 'www.william.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_change_add_change(self):
    print('\nTest change_password add change\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        print(self.__password.get_site_info('www.mary.edu'))
        self.__password.change_password('www.mary.edu', 'only_a_test')
        self.__password.add_password('www.william.edu', 'william')
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu', 'www.william.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    


  def test_remove_one(self):
    print('\nTest remove one site\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.__password.remove_site('www.wm.edu')
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.mary.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_remove_empty(self):
    print('\nTest remove empty\n')
    try:
        self.__password.remove_site('www.wm.edu')
        self.assertEqual(self.__password.get_site_list(),[])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_remove_twice_try(self):
    print('\nTest remove twice try\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.remove_site('www.wm.edu')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.__password.remove_site('www.wm.edu')
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.mary.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    
    
  def test_remove_mult(self):
    print('\nTest remove mult\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.remove_site('www.wm.edu')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.remove_site('www.wm.edu')
        self.__password.remove_site('www.google.com')
        self.assertEqual(self.__password.get_site_list(),['www.mary.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_remove_DNE(self):
    print('\nTest remove DNE\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.__password.remove_site('www.uiuc.edu')
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    
    
  def test_remove_DNE(self):
    print('\nTest remove DNE\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.__password.remove_site('www.uiuc.edu')
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_site_info_DNE(self):
    print('\nTest site info DNE\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.__password.get_site_info('www.uiuc.edu')
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_get_name(self):
    print('\nTest get name\n')
    try:
        self.assertEqual(self.__password.get_name(),'TestCases')
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_get_site_list_empty(self):
    print('\nTest site list_empty\n')
    try:
        self.assertEqual(self.__password.get_site_list(),[])
    except BaseException as e:
            print('Testing failed')
            print(e)

  def test_get_site_list(self):
    print('\nTest site list\n')
    try:
        self.__password.add_password('www.google.com', 'a_student')
        self.__password.add_password('www.wm.edu', 'this_student')
        self.__password.add_password('www.mary.edu', 'new_student')
        self.assertEqual(self.__password.get_site_list(),['www.google.com', 'www.wm.edu', 'www.mary.edu'])
    except BaseException as e:
            print('Testing failed')
            print(e)    

  def test_str(self):
    print('\nTest __str__\n')
    self.__password.add_password('www.google.com', 'a_student')
    self.__password.add_password('www.wm.edu', 'this_student')
    self.__password.add_password('www.mary.edu', 'new_student')
    print('Expected output')
    x = 'Sites stored for TestCases'+ '\n' + 'www.google.com' +'\n' + 'www.wm.edu'+ '\n' + 'www.mary.edu'
    print(x)
    print('Your output')
    print(self.__password)



if __name__ == '__main__':
  unittest.main()
