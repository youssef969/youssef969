from flet import *  
from flet_core import *  
import string
import random
from password_strength import PasswordStats
from Json_file import * 

class Func():
    @staticmethod
    def Button_hover (e,button :ElevatedButton, hover_icon:icons,old_icon:icons): 
        if e.data == "true":
            button.icon = hover_icon 
        elif e.data == "false":
            button.icon = old_icon 
        button.update()


    def __init__(self,page:Page,Text_feild:TextField,Radio:RadioGroup,
                 Generete_button:ElevatedButton,Save_buuton:ElevatedButton,Clear_button:ElevatedButton,
                 password_text:Text,password_text_icon:Icon,password_strenght_icon:Icon,password_strenght_text:Text,
                 row1:Row,row2:Row,row3:Row,row4:Row,row5:Row,Row6:Row,snackbar:SnackBar) :
        self.page = page
        self.Text_feild = Text_feild
        self.Radio = Radio
        self.Generete_button = Generete_button
        self.Save_button = Save_buuton
        self.Clear_button = Clear_button
        self.password_text = password_text
        self.password_text_icon = password_text_icon
        self.password_strenght_icon =password_strenght_icon
        self.password_strenght_text = password_strenght_text
        self.row1= row1
        self.row2 = row2
        self.row3 = row3
        self.row4 = row4
        self.row5 = row5
        self.Row6 = Row6
        self.snackbar = snackbar
        
    def Text_feild_on_change(self): 
        try:
            password = str(self.Text_feild.value)
            password_strenght = PasswordStats(password)
            percent = password_strenght.strength()*100

            if 20 >= percent >= 0:
                self.password_strenght_text.color= self.password_strenght_icon.color = Colors.RED_900
                

            elif 40 >= percent >= 20:
                self.password_strenght_text.color = self.password_strenght_icon.color = Colors.RED_400

            elif 60 >= percent >= 40:
                self.password_strenght_text.color = self.password_strenght_icon.color = Colors.ORANGE

            elif 80 >= percent >= 60:
                self.password_strenght_text.color =self.password_strenght_icon.color =  Colors.LIGHT_GREEN_400

            elif 100 >= percent >=80 :
                self.password_strenght_text.color = self.password_strenght_icon.color = Colors.GREEN_700

            self.password_strenght_text.value = f"strength of password: {round(percent,3)}%"
            self.Row6.opacity = 1
            
        except ValueError:
            self.password_strenght_text.value =  f"strength of password: {0}%"
        self.page.update()


   
    def Generate_password_button (self,options:list):
        self.Text_feild.error_text = ""
        self.Text_feild.border_color = "White"
        try:
            serial_list = []
            count = int(self.Text_feild.value) 
        
            self.Generete_button.text = "Regenerate"
            
            all_chars = [string.digits ,  string.ascii_uppercase , string.ascii_lowercase ,  string.punctuation  ]
            word = [option for choice , option in zip(options,all_chars) if choice == True]
            Password_choice = "".join(word)
            
            
            while count > 0:
                random_number = random.randint(0, len(Password_choice) - 1)
                random_character = Password_choice[random_number]
                serial_list.append(random_character)
                count -= 1     
            password = "".join(serial_list)
            self.password_text.value = password 
            self.row5.opacity = 1
        
            
        except ValueError as ve:
            if str(ve) == "empty range in randrange(0, 0)" :
                self.Text_feild.error_text = "You Must Choose the type of your Password"
            else:
                self.Text_feild.error_text = "You Must Enter the number of Charcters"
        self.page.update()




    def Clear(self,option1:Checkbox,option2:Checkbox,option3:Checkbox,option4:Checkbox):
        self.Generete_button.text = "Generate"
        self.row5.opacity = 0
        self.Text_feild.value = ""
        self.Text_feild.label = "Number Of Charcters"
        self.Text_feild.border_color = "White"
        self.Text_feild.error_text = ""
        option1.value = option2.value = option3.value = option4.value = False
        self.page.update()
        
        
    
    def Radio_change(self,option1:Checkbox,option2:Checkbox,option3:Checkbox,option4:Checkbox,Radio1:Radio,Radio2:Radio):

        
        if self.Radio.value == "True":
            self.row3.opacity = self.row4.opacity =  1
            self.Generete_button.visible =self.Save_button.visible = self.Clear_button.visible =  self.row5.visible= True
            self.row1.offset = transform.Offset(0,0)
            self.row2.offset = transform.Offset(0,0)
            self.Text_feild.on_change = None
            self.Row6.visible = False
            self.Text_feild.value = ""
            self.Text_feild.label = "Number Of Charcters"
            self.Text_feild.border_color = "White"
            self.Text_feild.error_text = ""
            self.password_strenght_text.value = ""
            self.Row6.opacity = 0
            Radio1.label_style = TextStyle(size=12,color=Colors.LIGHT_BLUE_500,weight=FontWeight.W_700)
            Radio2.label_style = TextStyle(size=12,color=Colors.WHITE,weight=FontWeight.W_700)

        elif self.Radio.value == "False":
            self.Text_feild.value = ""
            self.Text_feild.label = "Password"
            self.Text_feild.border_color = "White"
            self.Text_feild.error_text = ""
            self.row3.opacity = self.row4.opacity =   0
            self.Generete_button.visible =self.Save_button.visible = self.Clear_button.visible = False
            option1.value = option2.value = option3.value = option4.value = self.row5.visible =  False
            
            self.Row6.visible = True
            

            Radio2.label_style = TextStyle(size=12,color=Colors.LIGHT_BLUE_500,weight=FontWeight.W_700)
            Radio1.label_style = TextStyle(size=12,color=Colors.WHITE,weight=FontWeight.W_700)

            self.row1.offset = transform.Offset(0,2)
            self.row2.offset = transform.Offset(0,3.5)
            self.Text_feild.on_change = lambda e: self.Text_feild_on_change()
        self.page.update()

    def open_bs(self,BottemSheet:BottomSheet,SB_text:Text):
        if str(self.password_text.value).isspace() == True or str(self.password_text.value) == "":
            BottemSheet.open = False
            self.snackbar.open = True
            SB_text.value = "oops! You didn't Generate Password"
        else:
            BottemSheet.open = True
        self.page.update()

    def Save_button_func(self,BottemSheet:BottomSheet,t1:TextField,t2:TextField,SB_text:Text):
        
        Json_file.add(t1.value,t2.value,self.password_text.value)
        BottemSheet.open = False
        self.snackbar.open = True
        SB_text.value = "Your Generated Password is Saved"
        self.page.update()