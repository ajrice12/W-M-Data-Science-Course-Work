#You may add/edit import lines as needed but
#may not use structures and modules we have not discussed
import string

from random import randint, choice, choices, sample, shuffle

def password_specs(length = 14, min_spec = 0, min_num = 0, min_upper = 0):
    number = []#making a list to hold everything
    spec = randint(min_spec,length-min_num-min_upper)#checking to make sure the above variables are being met
    num = randint(min_spec,(length - spec - min_upper))#checking to make sure the above variables are being met
    upper = randint(min_spec,(length-num-spec))#checking to make sure the above variables are being met
    lowercase = (length-upper-num-spec)#checking to make sure the above variables are being met
    number = [spec, num, upper, lowercase]#Filling the empty list
    return number

def password_specs_test(length = 14, min_spec = 0, min_num = 0, min_upper = 0):
    return [1,3,3,7]

#Correct this function
#You may not add or delete lines
#You must correct lines in place, focus on indentation, logic, and correct usage of functions and variables
def password_gen(length = 14, spec_char = '@!&', repeat = True, min_spec = 0, min_num = 0, min_upper = 0):
    required = [min_upper, min_num, min_spec]
    if required[0]+required[1]+required[2] <= length and (repeat or len (spec_char) >= min_spec):
        specs = password_specs(length, min_spec, min_num, min_upper)
        if(repeat):
            password = choices(string.ascii_lowercase, k=specs[3]) + choices(string.ascii_uppercase, k=specs[2]) + choices(string.digits, k=specs[1]) + choices(spec_char, k=specs[0])#process for creating a password
            
        else:
            ok = False #DO NOT CHANGE THIS LINE
            while (not ok): #DO NOT CHANGE THIS LINE
                if specs[0] > len(spec_char) or specs[1] > len(string.digits) or specs[2] > len(string.ascii_uppercase)or specs[3] > len(string.ascii_lowercase):#
                    specs = password_specs(length, min_spec, min_num, min_upper)
                else:
                    ok = True #DO NOT CHANGE THIS LINE
            password = sample(string.ascii_lowercase, specs[3]) + sample(string.ascii_uppercase, specs[2]) + sample(string.digits, specs[1]) + sample(spec_char, specs[0])#
                    
        shuffle(password)
        pass_w = ''
        for i in password:
            pass_w += i
        print(pass_w)
    else:
        print('Invalid specifications!')


def check_password(password, length, min_spec, min_num, min_upper):
#fill in your function code and delete pass
#if you have not completed this function DO NOT delete pass
    scount = 0#variable declarition
    ncount = 0#variable declarition
    ucount = 0#variable declarition
    lcount = 0#variable declarition
    if len(password) != length:#stops the code if password doesn't meet requirements
        return False
    else:#process for checking password requirements
        for char in password:
            if char in string.digits:
                 ncount = ncount + 1
            elif char in string.ascii_uppercase:
                ucount = ucount + 1
            elif char in string.ascii_lowercase:
                lcount = lcount + 1
            else:
                scount = scount + 1
    if scount >= min_spec and ncount >= min_num and ucount >= min_upper:
        return True
    else:
        print(scount, ncount, ucount, lcount)
        return False

#there should be no main program or test code in this file
#and especially NO INPUT LINES
