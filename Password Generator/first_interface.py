from Buttons_func import *
from flet import *


class PSG(Column):
    def __init__(self,page:Page) :
        super().__init__()
        page.window.width = 900
        page.window.height = 1000
        page.window.maximizable= page.window.resizable =  False
        page.padding = 0
        page.window.center()

        
        #! ===================================================== Number Of Char (TextField) ===============================================
        n_char_TextField = TextField(
            label="Number Of Charcters",
            color="White",     
            width=400,
            border_color=Colors.WHITE38,
            focused_border_color="white",
            cursor_color="White",
            error_text="",
            input_filter=InputFilter(r"[0-9]*"),
            label_style=TextStyle(size=15,color="White",weight=FontWeight.W_500))
        #! ===================================================== Radio Group  ===============================================
        
        fill_color={
        ControlState.SELECTED: Colors.LIGHT_BLUE_700,
        ControlState.HOVERED: Colors.LIGHT_BLUE_600,
        ControlState.DEFAULT: Colors.WHITE,
        }
        
        Generete = Radio("Generete",value="True",fill_color=fill_color,label_style=TextStyle(size=12,color=Colors.LIGHT_BLUE_500,weight=FontWeight.W_700))   
        Evaluation = Radio("Evaluation",value="False",fill_color=fill_color,label_style=TextStyle(size=12,color="White",weight=FontWeight.W_700))
        Generete_or_test = RadioGroup(value="True",content=Row([Generete,Evaluation],
            spacing=100))
        
        
        #! ===================================================== Password Options (Checkbox) ===============================================
        fill_color={
        ControlState.SELECTED: Colors.LIGHT_BLUE_900,
        ControlState.HOVERED: Colors.LIGHT_BLUE_800,
        ControlState.DEFAULT: "#2d2f41",
        }
        number_option = Checkbox("Numbers",fill_color=fill_color,label_style=TextStyle(size=12,color="white",weight=FontWeight.W_700),value=False,border_side=BorderSide(1,"White"),) 
        capital_option = Checkbox("Capaital letters ",fill_color=fill_color,label_style=TextStyle(size=12,color="White",weight=FontWeight.W_700),value=False,border_side=BorderSide(1,"White"),) 
        small_option = Checkbox("Small letters ",fill_color=fill_color,label_style=TextStyle(size=12,color="White",weight=FontWeight.W_700),value=False,border_side=BorderSide(1,"White"),) 
        Punc_option = Checkbox("Punctuation ",fill_color=fill_color,label_style=TextStyle(size=12,color="White",weight=FontWeight.W_700),value=False,border_side=BorderSide(1,"White"),)
        
        #! ===================================================== Interface Buttons (Buttons) ===============================================
        
        Tooltip_ = Tooltip("Generete Password with random Charcters",border_radius=BorderRadius(10,10,10,10),wait_duration=Duration(milliseconds=400))
        generate_btn = ElevatedButton(icon=icons.GENERATING_TOKENS_OUTLINED,text="Generate",tooltip=Tooltip_,)
        generate_btn.on_hover =lambda e:Func.Button_hover(e,generate_btn, hover_icon=icons.GENERATING_TOKENS_ROUNDED, old_icon=icons.GENERATING_TOKENS_OUTLINED) # type: ignore
        
        
        Tooltip_2 = Tooltip("Save Genereted Password",border_radius=BorderRadius(10,10,10,10),wait_duration=Duration(milliseconds=400))
        save_btn = ElevatedButton(icon=icons.SAVE_OUTLINED,text="Save",tooltip=Tooltip_2,on_hover=lambda e: Func.Button_hover(e,save_btn, hover_icon=icons.SAVE, old_icon=icons.SAVE_OUTLINED)) # type: ignore
         

        Tooltip_3 = Tooltip("Clear All Inputs",border_radius=BorderRadius(10,10,10,10),wait_duration=Duration(milliseconds=400))
        clear_btn = ElevatedButton(icon=icons.CLEAR_ALL_OUTLINED,tooltip=Tooltip_3,text="Clear",on_hover=lambda e: Func.Button_hover(e,clear_btn, hover_icon=icons.CLEAR_ALL_ROUNDED, old_icon=icons.CLEAR_ALL_OUTLINED)) # type: ignore
        
        #! ===================================================== Password Generate (Text) ===============================================
        password_text_icon = Icon(icons.PASSWORD_ROUNDED,color="White",size=25)
        password_text = Text(value="",size=25,color="White",selectable=True)
        
        #! ===================================================== Password Generate (Text) ===============================================
        password_Strenght_icon = Icon(icons.LOCK,color="White",size=25)
        password_strenght_text = Text(size=25,color="White")
        
        #! ============================================================= Bottem Sheet =====================================================
        self.link_textfeild = TextField(label="Link",hint_text="ex:www.Google.com",width=200,hint_style=TextStyle(weight=FontWeight.NORMAL,color=Colors.BLACK38,italic=True))
        self.Name_textfeild = TextField(label="Website Name",hint_text="ex:Google",width=200,hint_style=TextStyle(weight=FontWeight.NORMAL,color=Colors.BLACK38,italic=True))
        self.save_btn_bs = ElevatedButton(icon=icons.SAVE_OUTLINED,text="Save",on_hover=lambda e: Func.Button_hover(e,self.save_btn_bs, hover_icon=icons.SAVE, old_icon=icons.SAVE_OUTLINED))
        
        self.SB_text = Text(value="")
        self.Snackbar = SnackBar(content=self.SB_text,open=False,show_close_icon=True)

        self.bs = BottomSheet(open=False,
        content=Container(width=450,height=200,
            padding=0,
            alignment=alignment.center,
            content=Column(tight=True,alignment=MainAxisAlignment.CENTER,
                
                controls=[
                    Row([Text("Another Step to Save Password!",weight=FontWeight.W_600)],alignment=MainAxisAlignment.CENTER),
                    Row([self.Name_textfeild,self.link_textfeild],alignment=MainAxisAlignment.CENTER),
                    Row([self.save_btn_bs],alignment=MainAxisAlignment.CENTER)
                ],
            ),
        ),
        )

        #! ===================================================== Container 1 ===============================================
        row1 = Row([Icon(icons.LOCK,color="White"),n_char_TextField],alignment=MainAxisAlignment.CENTER,offset=transform.Offset(0, 0),animate_offset=500)
        row2 = Row([Generete_or_test],alignment=MainAxisAlignment.CENTER,spacing=2,offset=transform.Offset(0, 0),animate_offset=500)
        row3 = Row([number_option, capital_option,small_option,Punc_option],alignment=MainAxisAlignment.SPACE_BETWEEN,spacing=20,animate_opacity=300)
        row4 = Row([generate_btn,save_btn,clear_btn],alignment=MainAxisAlignment.CENTER,spacing=100,animate_opacity=300)
        row5 = Row([password_text_icon,password_text],alignment=MainAxisAlignment.CENTER,opacity=0,animate_opacity=300,visible=True)
        Row6 = Row([password_Strenght_icon,password_strenght_text],alignment=MainAxisAlignment.CENTER,opacity=0,animate_opacity=300,visible=False)
        null = Row([Text("")])
        column_1 = Column(controls=[null,row1,row2,null,row3,null,row4,null,row5,Row6,self.bs,self.Snackbar])
        
        self.Continer_1= Container(content=column_1,width=900,height=440,expand=2,alignment=alignment.center,padding=8,
        gradient=RadialGradient(
        center=alignment.bottom_left,
        radius= 4.4,
        colors=["#42445f","#393b52","#33354a","#2f3143","#292b3c" ,"#222331","#1a1a25","#1a1b26" ,"#21222f","#1d1e2a","Black"]))
        
        #! ===================================================== Functions ===============================================
        functions = Func(page,n_char_TextField,Generete_or_test,generate_btn,save_btn,clear_btn,password_text,password_text_icon,password_Strenght_icon,password_strenght_text,
                        row1,row2,row3,row4,row5,Row6,self.Snackbar)
        
        generate_btn.on_click = lambda E: functions.Generate_password_button(options=[number_option.value,capital_option.value,small_option.value,Punc_option.value])
        clear_btn.on_click = lambda e: functions.Clear(number_option,capital_option,small_option,Punc_option)
        Generete_or_test.on_change = lambda f: functions.Radio_change(number_option,capital_option,small_option,Punc_option,Generete,Evaluation)
        self.save_btn_bs.on_click = lambda f: functions.Save_button_func(self.bs,self.Name_textfeild,self.link_textfeild,self.SB_text)
        save_btn.on_click = lambda t: functions.open_bs(self.bs,self.SB_text)
        
        self.controls = [self.Continer_1]
        
         
# def main(page:Page):
#     page.appbar = AppBar(
#         actions=[IconButton(icon=icons.EXIT_TO_APP_ROUNDED,on_click=lambda e: page.window.destroy())] ,
#         leading=IconButton(icon=icons.MENU),
#         title=Text("Passwords Manger",size=20),
#         elevation=5,
#         surface_tint_color="#1d1e2a",
#         shadow_color="#1d1e2a",
#         bgcolor="#1d1e2a",
#         color="White"
#     )
#     interface = PSG(page)
#     page.add(interface)
#     page.update()
# app(main)