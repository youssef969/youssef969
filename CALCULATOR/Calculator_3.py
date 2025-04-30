from flet import *  # type: ignore
import re
from math import factorial ,log10 ,log , pi
from math import e as exp
from int_or_float import Check


#! #ff9800 orange color
class Calc_3(Column):
    def __init__(self,page:Page):
        super().__init__()
        page.title = "Calculator"
        page.window.icon = "C:\\Users\\Computec\\Downloads\\Icons\\calculator (2).ico"
        page.window.width = page.window.max_width = 660 
        page.window.height = page.window.max_height = 450
        page.padding = 0
        page.horizontal_alignment = page.vertical_alignment= CrossAxisAlignment.STRETCH # type: ignore
        
        page.window.center()
        
        self.text =TextField(width=630,value="",text_align=TextAlign.END,border_width=0,keyboard_type=KeyboardType.NUMBER,disabled=True,color=["black","White"],input_filter=InputFilter(regex_string=r"[0-9]+[x/+-]{0,1}",allow=True),data=[]) # type: ignore
        self.Calc_tx = TextField(value="0",
                                show_cursor=False,
                                read_only=True,
                                width=630,
                                keyboard_type=KeyboardType.NUMBER,
                                border_radius=BorderRadius(10,10,10,10),
                                bgcolor=["#dbdbdb","#3b3b3b"], # type: ignore
                                color=["black","White"], # type: ignore # type: ignore
                                border_width=0,
                                text_align=TextAlign.END,
                                autofocus=True,
                                input_filter=InputFilter(regex_string=r"[0-9]",allow=True),
                                data=[]
                                )
        self.row0 = Row([
            ElevatedButton(text ="Log10",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.functions,bgcolor="#ccd7df",color="black",),
            ElevatedButton(text ="In",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.functions,bgcolor="#ccd7df",color="black"),
            ElevatedButton(text ="1/x",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.functions,bgcolor="#cfd8dc",color="black"),
            ElevatedButton(text ="AC",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.Clear,bgcolor="#cfd8dc",color="black"),
            ElevatedButton(text ="Ans",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.Ans,bgcolor="#cfd8dc",color="black"),
            ],spacing=2)
        
        self.row1 = Row([
            ElevatedButton(data = "^",text ="x\u02b8",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#cfd8dc",color="black",),
            ElevatedButton(text ="x\u00B2",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.functions,bgcolor="#cfd8dc",color="black"),
            ElevatedButton(text ="x\u00B3",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.functions,bgcolor="#cfd8dc",color="black"),
            ElevatedButton(text ="√",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.functions,bgcolor="#cfd8dc",color="black"),
            ElevatedButton(text =chr(8731),style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.functions,bgcolor="#cfd8dc",color="black"),
            ],spacing=2)
        
        self.row2 = Row([
            ElevatedButton(data=f"{pi}",text ="π",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#ff9800",color="white",),
            ElevatedButton(data=f"{exp}",text ="e",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#ff9800",color="white"),
            ElevatedButton(data="(",text ="(",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#ff9800",color="white",),
            ElevatedButton(data=")",text =")",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#ff9800",color="white"),
            ElevatedButton(data="÷",text ="÷",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#ff9800",color="white"),
            ],spacing=2)
        
        
        self.row3 = Row([
            ElevatedButton(text ="x\u00B9\u2070",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.functions,bgcolor="#ff9800",color="white"),
            ElevatedButton(data="7",text ="7",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(data="8",text ="8",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(data="9",text ="9",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(data="×",text ="×",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#ff9800",color="white"),
            ],spacing=2,)
        
        self.row4 = Row([
            ElevatedButton(text ="x!",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.functions,bgcolor="#ff9800",color="white"),
            ElevatedButton(data="4",text ="4",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(data="5",text ="5",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(data="6",text ="6",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(data="-",text ="-",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#ff9800",color="white"),
            ],spacing=2)
        
        self.row5 = Row([
            ElevatedButton(text ="|x|",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.functions,bgcolor="#ff9800",color="white"),
            ElevatedButton(data="1",text ="1",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(data="2",text ="2",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(data="3",text ="3",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(data="+",text ="+",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#ff9800",color="white"),
            ],spacing=2)
        
        self.row6 = Row([
            ElevatedButton(text ="+/-",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.functions,bgcolor="#ff9800",color="white"),
            ElevatedButton(data="0",text ="0",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=242,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(data=".",text =".",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.button_clicked,bgcolor="#3d3d3d",color="white"),
            ElevatedButton(text ="=",style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),width=120,on_click=self.equal,bgcolor="#ff9800",color="white"),
            ],spacing=2)
        
        buttons_contianer = Container(content=Column(controls=[self.row0,self.row1,self.row2,self.row3,self.row4,self.row5,self.row6],wrap=True,tight=True,spacing=2,scroll="auto")) # type: ignore
        self.controls = [Row([self.text],alignment=MainAxisAlignment.END),Row([self.Calc_tx],alignment=MainAxisAlignment.END),Row([buttons_contianer],alignment=MainAxisAlignment.CENTER)]
        self.ans = [0]  
        self.pattern = []               #! list to store equation and calc it 
        
    def button_clicked(self,e):
        from math import e as exp
        
        self.Calc_tx.label = ""
        data = e.control.data
        
        self.pattern.append(data)
        self.text.data.append(data) # type: ignore
        
        pattern = "".join(self.text.data) # type: ignore
        result = re.findall(r"[-]{0,1}[0-9a-zA-z)√∛π/e(]+[×÷+-.^]{0,1}",pattern)           #! this regex to don't allow user to repeat ×÷+- operations
        
        final = "".join(result)
        final=final.replace("π","3.1415")  
        final=final.replace("e","2.718281828459045")
        self.text.value = final
        
        
        if data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".",f"{pi}",f"{exp}"): #! if_elif condition here is to Texrfelid for numbers only 
            self.Calc_tx.data.append(data) # type: ignore
            self.Calc_tx.value = "".join(self.Calc_tx.data) # type: ignore
        
        elif data in ("×", "÷", "+","-","^"):
            self.Calc_tx.data.clear() # type: ignore
        self.update()           
                
    def equal(self,e):
        #try:
            self.Calc_tx.label = ""
            
            pattern = "".join(self.pattern)
            result = re.findall(r"[-]{0,1}[0-9πe()]+[×÷+-.^]{0,1}",pattern)           #! this regex to don't allow user to repeat ×÷+- operations
            final = "".join(result)
            r = re.findall(r"[-]{0,1}[×÷+-.^]{0,1}[0-9,πe()]+",final)                  #! this regex to prevent syntax error in Eval() Func.
            
            
            g = "".join(r)
            g = g.replace("π","3.1415")  
            g = g.replace("e","2.718281828459045") 
            g = g.replace("×","*")
            g = g.replace("÷","/")
            g = g.replace("^","**")
            
            self.Calc_tx.value =  Check.check_int_or_float(s=str(eval(g))) # type: ignore
      
            self.ans.append(self.Calc_tx.value)
            
            self.pattern.clear() 
            self.pattern.append(str(self.Calc_tx.value)) 
            
            self.text.value = self.pattern[-1]
            self.text.data.clear()
            self.text.data.append(self.pattern[-1])
            
            # print(self.pattern)
            # print(self.text.data)
            self.update()
            
            
            
        # except ZeroDivisionError:
        #     self.Calc_tx.label = "Syntax Error : Zero Division"
        #     self.Calc_tx.label_style =TextStyle(size=20,weight=FontWeight.W_700,color=colors.RED_600)
        #     self.Calc_tx.value = "0"
        #     self.text.value = "0"
        #     self.Calc_tx.data.clear()
        #     self.text.data.clear()
        #     self.update()  
        
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
        if data == f"{pi}" or data == f"{exp}":
            self.text.data.pop(-2)
            self.text.value = "".join(self.text.data) 
            self.pattern.append(str(pattern))
            self.pattern.pop(-2)
            self.Calc_tx.value = Check.check_int_or_float(str(self.pattern[-1]))
            
            
        else:
            try:
                self.pattern.append(str(pattern))
                for x in range(len(data)):
                    self.text.data.pop(-2)
                    self.pattern.pop(-2)
                self.text.value = "".join(self.text.data) 
                self.Calc_tx.value = Check.check_int_or_float(str(self.pattern[-1]))
            except IndexError :
                self.pattern.append(str(pattern))
                self.text.value = "".join(self.text.data) 
                self.Calc_tx.value = Check.check_int_or_float(str(self.pattern[-1]))   
        self.update()
        
    def functions(self,e):
        event = e.control.text
        data = self.Calc_tx.value
        data = Check.check_int_or_float(data)
        
        if event == "x!":
            result = factorial(data)
            self.Helper_functions(5,data=str(data),text=f"Fact({data})",pattern=result)
        elif event == "|x|":
            result = abs(data)
            self.Helper_functions(e=0,data=str(data),text=f"abs({data})",pattern=result)
            
        elif event == "x\u00B9\u2070":
            result = data ** 10
            self.Helper_functions(e=0,data=str(data),text=f"10 ^ ({data})",pattern=result)
        elif event == "+/-":
            result = data * -1
            self.Helper_functions(0,data=str(data),text=f"{result}",pattern=result)
        
        elif event == "√":
            result = data ** 0.5
            self.Helper_functions(0,data=str(data),text=f"√({data})",pattern=result)
            
        elif event == chr(8731):
            result = data ** (1/3)
            self.Helper_functions(0,data=str(data),text=f"{chr(8731)}({data})",pattern=result)
            
        elif event ==   "x\u00B3"  :
            result = data ** 3
            self.Helper_functions(0,data=str(data),text=f"cub({data})",pattern=result)
            
        elif event ==   "x\u00B2"  :
            result = data ** 2
            self.Helper_functions(0,data=str(data),text=f"sqr({data})",pattern=result)
            
        elif event == "Log10":
            result = log10(data)
            self.Helper_functions(0,data=str(data),text=f"log({data})",pattern=result)
        elif event == "In":
            result = log(data)
            
            self.Helper_functions(0,data=str(data),text=f"ln({data})",pattern=result)
            
        elif event == "1/x":
            result = 1 / data
            self.Helper_functions(0,data=str(data),text=f"1/({data})",pattern=result)
        
        pattern = "".join(self.text.data)
        result = re.findall(r"[-]{0,1}[0-9a-zA-z)√∛/πe^(]+[×÷+-.]{0,1}",pattern)
        self.text.value = "".join(result)   
        self.update()
            
         
# def main(page:Page):  
#     page.title = "Calculator"
#     page.window.icon = "C:\\Users\\Computec\\Downloads\\Icons\\calculator (2).ico"
#     page.window.width = 660
#     page.window.height = 440
#     page.window.max_width = 660 
#     page.window.max_height = 440
#     page.window.top = 200
#     page.window.left = 500
#     page.padding =0
    
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
#         selected_index=1,
#         indicator_shape=RoundedRectangleBorder(radius=BorderRadius(10,10,10,10)),
#         position=NavigationDrawerPosition.START,
#         indicator_color=["#e0e0e0","#3b3b3b"],
#         controls=[
#             NavigationDrawerDestination(icon=Icons.CALCULATE_OUTLINED, label="Standard",selected_icon=Icons.CALCULATE),
#             NavigationDrawerDestination(icon=Icons.SCIENCE_OUTLINED, label="Scientific",selected_icon=Icons.SCIENCE),
#             NavigationDrawerDestination(icon=Icons.CALENDAR_MONTH_OUTLINED, label="Date",selected_icon=Icons.CALENDAR_MONTH),
#             # Divider(thickness=1,height=10,leading_indent=5,trailing_indent=5),Row([c],alignment=MainAxisAlignment.CENTER)
            
#         ],
#     )
    
#     appbar = AppBar(title=Text("Scientific",weight=FontWeight.BOLD),leading=IconButton(icon=Icons.MENU,on_click=lambda _:page.open(end_drawer))
#                     ,actions=[IconButton(icon=Icons.EXIT_TO_APP_OUTLINED,icon_color="red",on_click=lambda _: page.window.destroy())]
                    
#                     )   
#     page.add(Calc_3(page=page),appbar)
#     # load(e=5)
#     page.update()
# app(target=main)