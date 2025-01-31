import random
import string
from random import randint, shuffle, sample, choices
import pandas as pd


class PasswordManager:
#'Site','Username','Password'
#self.__passwords.columns = ['Site','Username','Password'] 
    def __init__(self, name, master_pw):
        self.__passwords = pd.DataFrame(columns = ['Site','Username','Password']) 
        self.__passwords.set_index('Site', inplace = True)
        self.__name = name#store name of the user
        self.__master_pw = master_pw#store master password
        
    def __password_specs(self, length = 14, min_spec = 0, max_spec = 0, min_num = 0, min_upper = 0):
        #update this code so that it works with the max_spec argument
        #it is otherwise correct
        #HINT: you only need to change one line of code in this implementation to
        #do this, and it is the FIRST LINE
        #Or you can add a few lines, but they go before the FIRST LINE
        num_sc = randint(min_spec, min(max_spec,(length - min_num - min_upper)))# or min spec, max_spec instead
        num_num = randint(min_num, length - num_sc  - min_upper)
        num_upper = randint(min_upper, length - num_sc - num_num)
        num_lower = length - (num_sc + num_num + num_upper)
        return [num_sc, num_num, num_upper, num_lower]
    
    def __password_gen(self, criteria = None,length = 14, spec_char = '@!&', repeat = True, min_spec = 0, max_spec = 0, min_num = 0, min_upper = 0):
        if criteria != None:
            keys = criteria.keys()
            if ('min_num' in keys):
                min_num = criteria['min_num']
            if ('spec_char' in keys):
                spec_char = criteria['spec_char']
            if ('min_spec' in keys):
                min_spec = criteria['min_spec']
            if ('max_spec' in keys):
                max_spec = criteria['max_spec']
            if ('min_upper' in keys):
                min_upper = criteria['min_upper']
            if ('length' in keys):
                length = criteria['length']
            if ('repeat' in keys):
                repeat = criteria['repeat']
            
        if(max_spec < min_spec): 
            max_spec = min_spec 
        required = sum([min_spec, min_num, min_upper]) 
        if required <= length and (repeat or len(spec_char)>=min_spec): 
            specs = self.__password_specs(length, min_spec, max_spec, min_num, min_upper)
            if(repeat): 
                password = random.choices(string.ascii_lowercase, k=specs[3]) + random.choices(string.ascii_uppercase, k=specs[2]) + random.choices(string.digits, k=specs[1]) + random.choices(spec_char, k=specs[0])
            else:
                while specs[0] > len(spec_char) or specs[1] > len(string.digits) or specs[2] > len(string.ascii_uppercase) or specs[3] > len(string.ascii_lowercase):
                    specs = self.__password_specs(length, min_spec, max_spec, min_num, min_upper)
                password = random.sample(string.ascii_lowercase, specs[3]) + random.sample(string.ascii_uppercase, specs[2]) + random.sample(string.digits, specs[1]) + random.sample(spec_char, specs[0])
            shuffle(password)
            return''.join(password)

    def add_password(self, site, username, criteria = None):
        #generate a new password according to criteria 
        #if site is not already in the df is True 
        password = self.__password_gen(criteria)
        if site not in self.__passwords:
            if password != None:
                self.__passwords.loc[site] = [username,password]
            else:
                print('Invalid Specifications!')
        #add the site, username and password to the df
        #otherwise, print an error message for password generated with invalid specifications
    

    def validate(self, mp):
        #Checks whether mp is the same as the master password
        #Returns a boolean
        #This is one line in my implementation
        return mp == self.__master_pw
  
    def change_password(self, site, master_pass, new_pass = None, criteria = None):
        #If master_password entered correctly
        #If site is present in the df 
        if self.validate(master_pass) == True:
            if site in self.__passwords.index:
                if new_pass != None:
                    self._passwords.loc[site,'Password'] = new_pass
                else:
                    new_password = self.__password_gen(criteria)
                    if new_password != None:
                        self.__passwords.loc[site,'Password'] = new_password
                    else:
                        print('Invalid Specifications!')
            else:
                print('Site does not exist!')
        else:
            print('Incorrect Master Password!')
        #Updates the password to the site
        #This will be new_pass if provided, otherwise, will generate a
        #New password using criteria and store it in the collection of passwords
        #If site does not exist, prints error message
        #If master password is wrong, print an error message
        pass

    def remove_site(self, site):
        #check if site is present in the df
        #Delete a site and the associated data
        #This is two lines in my implementation
        if site in self.__passwords.index:
            self.__passwords.drop(site, inplace = True)#we need a method that can remove both rows and columns

    def get_site_info(self, site):
        #Return a list of username and password for the site passed in as the argument
        #This is two line in my implementation
        return list(self.__passwords.loc[site])

    def get_name(self):
        #Return the name of the owner of the password manager
        #This is one line in my implementation
        return self.__name

    def get_site_list(self):
        #Return a list of all the sites (just the sites, not the passwords)
        #This is one line in my implementation
        return list(self.__passwords.index)

    #def reset_master_password(self, old_pass, new_pass)
    def __str__(self):
        #Return a string representation of ONLY the sites
        #Should look like this
        #Sites stored for NAME_OF_OWNER:
        #www.google.com
        #www.facebook.com
        #www.turtlesareawesome.org
        #One site per line with the header line
        return'Sites stored for'+ self.get_name() + ':\n' + '\n'.join(self.get_site_list()) #check module three, r strip method new line characters
