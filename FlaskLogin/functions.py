import bcrypt, json

def hash_password(plain_text):
    plain_text = plain_text.encode()
    return bcrypt.hashpw(plain_text,bcrypt.gensalt())

def CheckUserList():
    data_file = open("database.json","r")
    database = json.load(data_file)
    data_file.close()
    
    user_list = []

    for i in database["users"]:
        user_list.append(i["username"])
    
    return user_list

def check_pw(username,password):
    data_file = open("database.json","r")
    database = json.load(data_file)
    data_file.close()

    a=0
    for i in database["users"]:
        if (i["username"] == username):
            if (bcrypt.checkpw(password.encode(),i["password"].encode())):
                return True
        a+=1
    return False

def save_user(username, password):
    password = bytes.decode(hash_password(password))
    data_file = open("database.json","r")
    database = json.load(data_file)
    data_file.close()

    database["users"].append({"username":username,"password":password})

    data_file = open("database.json","w")
    json.dump(database,data_file,indent=4)