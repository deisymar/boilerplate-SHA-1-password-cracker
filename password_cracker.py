import hashlib

def crack_sha1_hash(hash, use_salts=False):
    passwords_arr=[]
    read_and_add_to_regpass("top-10000-passwords.txt", passwords_arr)
    
    if use_salts:
        top_salts_file = []
        top_salts_passwords = {}
        read_and_add_to_regpass("known-salts.txt", top_salts_file)
        for bsalt in top_salts_file:
            for bpass in passwords_arr:
                appended = hashlib.sha1(bpass+bsalt).hexdigest()
                prepended = hashlib.sha1(bsalt+bpass).hexdigest()
                top_salts_passwords[appended] = bpass.decode("utf-8")
                top_salts_passwords[prepended] = bpass.decode("utf-8")          
        if hash in top_salts_passwords:
            return top_salts_passwords[hash]
            
    hashed_passwords = {}
    for p in passwords_arr:
        hash_line= hashlib.sha1(p).hexdigest()
        hashed_passwords[hash_line]= p.decode("utf-8")
        
    if hash in hashed_passwords:
        return hashed_passwords[hash]   

    #print(password_dict)
    return "PASSWORD NOT IN DATABASE"

def read_and_add_to_regpass(file_name, regpass):
    with open(file_name, "rb") as passwords_file:
        line= passwords_file.readline().strip()
        while line:
            regpass.append(line)
            line = passwords_file.readline().strip()
    #print(regpass)