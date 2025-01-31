import Project_2
import string
from random import choices, sample, choice, shuffle, randint, password_gen, password_check, password_specs

Pass_list = [password_gen(min_spec=2, min_upper = 1, repeat = False, spec_char = '@!&'),password_gen(min_spec=2, min_upper = 1, repeat = False, spec_char = '@!&'),password_gen(min_spec=2, min_upper = 1, repeat = False, spec_char = '@!&'),password_gen(min_spec=2, min_upper = 1, repeat = False, spec_char = '@!&')]

print(Pass_list)

i = 0
checked = []
while len(Pass_list) > i:
    result = check_password(Pass_list[i], 14, 2, 0, 1)
    checked += [result]
    i += 1
print(checked)