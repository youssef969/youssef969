from flet import * 
import json
from Json_file import * 

class DT():
    def __init__(self,page:Page,data:DataTable,sb:SnackBar,text:Text) :
        self.data = data
        self.page = page
        self.sb = sb
        self.text = text
        
    def Show_data(self):       
        with open(r"D:\Flet - Cross Platform\2.Password_generator\Passwords.json","r") as file:
            passwords = json.load(file)
        for x in range(len(passwords["passwords"])):
            action =IconButton(icon=icons.DELETE_FOREVER_OUTLINED,icon_color="red",data=x,on_click=self.delete)
            (A:= passwords["passwords"][x]["name"])
            (B:= passwords["passwords"][x]["link"])
            (C:= passwords["passwords"][x]['password'])
            self.data.rows.append(
                DataRow([
                    DataCell(Text(f"{A}",color="White")), 
                    DataCell(Text(f"{B}",color="White")), 
                    DataCell(Text(f"{C}",color="White")),
                    DataCell(content=Row([action]))
              ])      
            )       
        self.page.update()

    def delete (self,e):
        index = e.control.data
        Json_file.delete(index)
        self.sb.open = True
        self.text.value = "The Password is Deleted"
        self.data.rows = []
        self.Show_data()
        self.page.update()
        self.data.update()
