from flet import * 
import json

class Json_file():
    
    @staticmethod
    def add(name_:str,link_:str,password_:str):

        passwords_list = []
        with open(r"D:\Flet - Cross Platform\2.Password_generator\Passwords.json","r") as file:
            passwords = json.load(file)
        with open(r"D:\Flet - Cross Platform\2.Password_generator\Passwords.json","w+") as file:
            try: 
                for password in passwords["passwords"]:
                    passwords_list.append(password)
                passwords_list.append({"name":name_,"link":link_,"password":password_})
                name = dict(passwords = passwords_list)
            except:
                passwords_list.append({"name":name_,"link":link_,"password":password_})
                name = dict(passwords = passwords_list)
            json.dump(name,file,indent=2)
        

    @staticmethod
    def Passwords_list():
        with open(r"D:\Flet - Cross Platform\2.Password_generator\Passwords.json","r") as file:
                passwords_list = []
                passwords = json.load(file)
                for x in range(len(passwords["passwords"])):
                        (A:=passwords["passwords"][x]["name"])
                        (B:=passwords["passwords"][x]["link"])
                        (C:=passwords["passwords"][x]['password'])
                        passwords_list.append([A,B,C])
        return passwords_list

    @staticmethod
    def delete(index:int):
        list_1 = Json_file.Passwords_list()
        edit_list = []
        list_1.pop(index)
        for A,B,C , in list_1:
            
            edit_list.append({"name":A,"link":B,"password":C})
        name = dict(passwords = edit_list, youssef = "20")
        with open(r"D:\Flet - Cross Platform\2.Password_generator\Passwords.json","w+") as file:
    
    
            json.dump(name,file,indent=2)

    @staticmethod
    def Number_of_passwords():
        passwords_list = []
        with open(r"D:\Flet - Cross Platform\2.Password_generator\Passwords.json","r") as file:
            passwords = json.load(file)
            for password in passwords["passwords"]:
                    passwords_list.append(password)
        return len(passwords_list)



    

        





    