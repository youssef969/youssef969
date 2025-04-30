from flet import *
import re
from int_or_float import Check

class Calc_1 (Column):
    def __init__(self):
        super().__init__()
        
        
        self.text =TextField(width=630,value="",text_align=TextAlign.END,border_width=0,keyboard_type=KeyboardType.NUMBER,disabled=True,color=["black","White"],input_filter=InputFilter(regex_string=r"[0-9]+[x/+-]{0,1}",allow=True),data=[])
        self.Calc_tx = TextField(value="0",
                                show_cursor=False,
                                read_only=True,
                                width=630,
                                keyboard_type=KeyboardType.NUMBER,
                                border_radius=BorderRadius(10,10,10,10),
                                bgcolor=["#dbdbdb","#3b3b3b"],
                                color=["black","White"],    
                                border_width=0,
                                text_align=TextAlign.END,
                                autofocus=True,
                                input_filter=InputFilter(regex_string=r"[0-9]",allow=True),
                                data=[]
                                )
        self.row0 = Row([
            ElevatedButton(text ="AC",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.Clear,bgcolor="#cfd8dc",color="black"),
            ElevatedButton(text ="%",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.functions,bgcolor="#cfd8dc",color="black"),
            ElevatedButton(text ="Ans",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.Ans,bgcolor="#cfd8dc",color="black"),
            ElevatedButton(text ="÷",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#ff9800",color="white"),
            
            ],spacing=2)
        
        self.row1 = Row([
            ElevatedButton(text ="7",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text ="8",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text ="9",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text ="×",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#ff9800",color="white"),
            
            ],spacing=2,)
        
        self.row2 = Row([
            ElevatedButton(text ="4",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text ="5",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text ="6",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text ="-",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#ff9800",color="white"),
            
            ],spacing=2)
        
        self.row3 = Row([
            ElevatedButton(text ="1",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text ="2",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text ="3",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text ="+",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#ff9800",color="white"),
        
            ],spacing=2)
        
        self.row4 = Row([
            ElevatedButton(text ="0",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=302,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text =".",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text ="=",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=150,on_click=self.equal,bgcolor="#ff9800",color="white"),
            
        
            ],spacing=2)
        
        buttons_contianer = Container(content=Column(controls=[self.row0,self.row1,self.row2,self.row3,self.row4],wrap=True,tight=True,spacing=2,scroll="auto"))
        self.controls = [Row([self.text],alignment=MainAxisAlignment.END),Row([self.Calc_tx],alignment=MainAxisAlignment.END),Row([buttons_contianer],alignment=MainAxisAlignment.CENTER)]
        self.pattern = []
        self.ans = [0]  
    
        
    def button_clicked(self,e):
        self.Calc_tx.label = ""
        e.control.data = e.control.text 
        data = e.control.data
        
        self.pattern.append(data)
        self.text.data.append(data)
        
        pattern = "".join(self.text.data)
        result = re.findall(r"[0-9%]+[×÷+-.]{0,1}",pattern)           #! this regex to don't allow user to repeat ×÷+- operations
        final = "".join(result)
        self.text.value = final
        
        if data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".","%"):
            self.Calc_tx.data.append(data)
            self.Calc_tx.value = "".join(self.Calc_tx.data)
                
        elif data in ("×", "÷", "+", "-",):
            self.Calc_tx.data.clear()
        self.update()
            
                
    def equal(self,e):
        # try:
            self.Calc_tx.label = ""
            pattern = "".join(self.pattern)
            result = re.findall(r"[0-9%]+[×÷+-.]{0,1}",pattern)           #! this regex to don't allow user to repeat ×÷+- operations
            final = "".join(result)
            r = re.findall(r"[×÷+-.%]{0,1}[0-9]+",final)                  #! this regex to prevent syntax error in Eval() Func.
            
            g = "".join(r)
            g = g.replace("×","*")
            g = g.replace("÷","/")
            g = g.replace("%","/100")
            
            
            self.Calc_tx.value = Check.check_int_or_float(s=str(eval(g)))
            self.ans.append(self.Calc_tx.value) 
            
            self.pattern.clear() 
            self.pattern.append(str(self.Calc_tx.value))   
            
            self.text.value = self.pattern[-1]
            self.text.data.clear()
            self.text.data.append(self.pattern[-1])
            
        # except ZeroDivisionError:
        #     self.Calc_tx.label = "Syntax Error : Zero Division"
        #     self.Calc_tx.label_style =TextStyle(size=20,weight=FontWeight.W_700,color=.RED_600)
        #     self.Calc_tx.value = "0"
        #     self.text.value = "0"
        #     self.Calc_tx.data.clear()
        #     self.text.data.clear()
            
            self.update()
    
        
    def Clear(self,e):
        self.Calc_tx.label = ""
        self.Calc_tx.value = "0"
        self.text.value = ""
        self.Calc_tx.data.clear()
        self.text.data.clear()
        self.pattern.clear()
        self.update()
    
    def Ans(self,e):
        Answer = self.ans[-1]
        self.pattern.append(str(Answer))
        self.text.data.append(str(Answer))
        pattern = "".join(self.text.data.copy())
        self.text.value = pattern 
        self.Calc_tx.value =Answer
        self.update()
    
    def Helper_functions(self,e,data,text:str,pattern):                  
            self.text.data.append(text)
            for x in range(len(data)):
                self.text.data.pop(-2)
            self.text.value = "".join(self.text.data) 
            
            self.pattern.append(str(pattern))
            for x in range(len(data)):
                self.pattern.pop(-2)
            
            self.Calc_tx.value = Check.check_int_or_float(str(self.pattern[-1]))
            
    def functions(self,e):
        event = e.control.text
        data = self.Calc_tx.value
        data = Check.check_int_or_float(data)
        
        if event == "%":
            result = data/100
            self.Helper_functions(e=5,data=str(data),text=f"{data}%",pattern=result)
            
        pattern = "".join(self.text.data)
        result = re.findall(r"[-]{0,1}[0-9a-zA-z)√∛/πe%^(]+[×÷+-.]{0,1}",pattern)
        self.text.value = "".join(result)   
        self.update()

                
# def main(page:Page):  
#     page.title = "Calculator"
#     page.window.icon = "C:\\Users\\Computec\\Downloads\\\\calculator (2).ico"
#     page.window.width = 660
#     page.window.height = 400
#     page.window.max_width = 660 
#     page.window.max_height = 400
#     page.window.top = 200
#     page.window.left = 500
    
#     #! =============================================================== Functions =========================================
#     # def theme_changed(e):
#     #     if c.value == True:
#     #         c.label = "Dark theme"
#     #         page.theme_mode = ThemeMode.DARK
#     #     else:
#     #         c.label = "Light theme" 
#     #         page.theme_mode = ThemeMode.LIGHT
#     #     state = {"switch_state": c.value}
#     #     with open("D:\\Python\\Mobile Application - Flet\\CALCULATOR\\switch_state.json", "w+") as f:
#     #         json.dump(state, f)
#     #     page.update()
        
#     # def load(e):
#     #     with open("D:\\Python\\Mobile Application - Flet\\CALCULATOR\\switch_state.json","r") as f:
#     #         state = json.load(f)
#     #         c.value = state["switch_state"]
#     #         if state["switch_state"] == True:
#     #                 c.value = True
#     #                 c.label = "Dark theme"
#     #                 page.theme_mode = ThemeMode.DARK
#     #         else:   
#     #                 c.value = False
#     #                 c.label = "Light theme" 
#     #                 page.theme_mode = ThemeMode.LIGHT
                    
#     #! ================================================ Controls ========================================================   
#     # c= Switch(label="Light theme", on_change=theme_changed ,label_position=LabelPosition("right"))
    
    
#     end_drawer = NavigationDrawer(
#         tile_padding= 5,
#         selected_index=0,
#         indicator_shape=RoundedRectangleBorder(radius=BorderRadius(10,10,10,10)),
#         position=NavigationDrawerPosition.START,
#         indicator_color=["#e0e0e0","#3b3b3b"],
#         controls=[
#             NavigationDrawerDestination(icon=.CALCULATE_OUTLINED, label="Standard",selected_icon=.CALCULATE),
#             NavigationDrawerDestination(icon=.SCIENCE_OUTLINED, label="Scientific",selected_icon=.SCIENCE),
#             NavigationDrawerDestination(icon=.CALENDAR_MONTH_OUTLINED, label="Date",selected_icon=.CALENDAR_MONTH),
#             # Divider(thickness=1,height=10,leading_indent=5,trailing_indent=5),Row([c],alignment=MainAxisAlignment.CENTER)
            
#         ],
#     )
    
#     appbar = AppBar(title=Text("Standard",weight=FontWeight.BOLD),leading=IconButton(icon=.MENU,on_click=lambda _:page.open(end_drawer))
#                     ,actions=[IconButton(icon=.EXIT_TO_APP_OUTLINED,icon_color="red",on_click=lambda _: page.window.destroy())]
                    
#                     )   
#     page.add(Calc_1(),appbar)
#     # load(e=5)
#     page.update()
# app(target=main)