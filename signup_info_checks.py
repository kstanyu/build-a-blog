
def is_empty(usr_string):
    empty = True
    if usr_string != "":
        empty = False
    return empty

def contains_aspace(usr_str):
    space = False
    if " " in usr_str:
        space = True
    return space

def is_length_ok(usr_data):
    ok = True
    if len(usr_data) < 3 or len(usr_data) > 20:
        ok = False
    return ok

def is_a_match(usr_str_a, usr_str_b):
    match = False
    if usr_str_a == usr_str_b:
        match = True
    return match

def is_email(usr_email):
    valid_email = False
    if((usr_email.count("@") == 1) and (usr_email.count(".") == 1) and not contains_aspace(usr_email)) or usr_email == "": 
    
        valid_email = True
    return valid_email    
     
