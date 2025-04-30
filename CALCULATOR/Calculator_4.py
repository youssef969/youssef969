from flet import * 
from Number_systems import number_sys
from  hover import Hover

class Calc_4(Column):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        page.title = "Calculator"
        page.window.icon = "C:\\Users\\Computec\\Downloads\\Icons\\calculator (2).ico"
        page.window.width = 660
        page.window.height = 440
        page.window.max_width = 660 
        page.window.max_height = 440
        page.window.top = 200
        page.window.left = 500
        page.padding =0
        page.scroll = "auto"
        


        

        options = [dropdown.Option(text="Binary",key="Binary"),dropdown.Option(text="Decimal",key="Decimal"),dropdown.Option(text="Octal",key="Octal"),dropdown.Option(text="Hexadecimal",key="Hexadecimal"),dropdown.Option(text="Text",key="Text")]
        options2 = [dropdown.Option(text="Binary",key="Binary"),dropdown.Option(text="Octal",key="Octal"),dropdown.Option(text="Hexadecimal",key="Hexadecimal"),dropdown.Option(text="Text",key="Text")]
        from_ = TextField(hint_text="Decimal",bgcolor=["#dbdbdb","#3b3b3b"],color=["black","White"],prefix_icon=Icons.NUMBERS,border_radius=border_radius.all(10))
        from_input = Dropdown(width=180,
                            autofocus=False,
                            value="Decimal",
                            border_radius=BorderRadius(10,10,10,10),
                            border_width=1,
                            max_menu_height=30,
                            color ="#36618e",
                            text_style=TextStyle(weight=FontWeight.W_500),options=options)
        
        to_ = TextField(border=InputBorder.UNDERLINE,hint_text="Binary",multiline=False,prefix_icon=Icons.NUMBERS,read_only=True,color=["black","White"])
        to_input = Dropdown(width=180,
                            autofocus=False,
                            value="Binary",
                            border_radius=BorderRadius(10,10,10,10),
                            border_width=1,
                            max_menu_height=30,
                            color ="#36618e",
                            text_style=TextStyle(weight=FontWeight.W_500),options=options2)


        b1 = ElevatedButton(text="Convert")
        b2 = ElevatedButton(text="Swap",icon=Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED)
        b3 = ElevatedButton(text="Reset",icon=Icons.CLEAR)
        row0 = Row([Text("         "),from_],alignment=MainAxisAlignment.CENTER)
        row1 = Row([Text("from",color="#a7a7a7",font_family="Elephant",size=20),from_input,Text("to",color="#a7a7a7",font_family="Elephant",size=20),to_input],alignment=MainAxisAlignment.CENTER)
        row2 = Row([Text("         "),to_],alignment=MainAxisAlignment.CENTER)
        row3 = Row([b1,b2,b3],alignment=MainAxisAlignment.CENTER)
        null = Row([Text("\n")])


        self.column = Column(controls=[row0,row1,null,row2,null,row3],spacing=10)
        self.continer = Container(content=self.column,padding=5)


        from_input.on_change = to_input.on_change = lambda e: number_sys.change_dropdpwn(page,from_,to_,from_input,to_input)
        b1.on_click = lambda e: number_sys.convert_number_system(page,from_,to_,from_input,to_input)
        b2.on_click = lambda e: number_sys.Swap(page,from_,to_,from_input,to_input)
        b3.on_click = lambda e: number_sys.clear(page,from_,to_)

        b2.on_hover = lambda e: Hover.Button_hover(e,b2,Icons.SWAP_HORIZONTAL_CIRCLE,Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED)
        b3.on_hover = lambda e: Hover.Button_hover(e,b3,Icons.CLEAR,Icons.CLEAR_OUTLINED)
        self.controls = [self.continer]
        
# def main(page:Page):
    
    
#     #! ================================================ Controls ========================================================   
#     #c= Switch(label="Light theme", on_change=theme_changed ,label_position=LabelPosition("right"))
    
    
#     end_drawer = NavigationDrawer(
#         tile_padding= 5,
#         selected_index=3,
#         indicator_shape=RoundedRectangleBorder(radius=BorderRadius(10,10,10,10)),
#         position=NavigationDrawerPosition.START,
#         indicator_color=["#e0e0e0","#3b3b3b"],
#         controls=[
#             NavigationDrawerDestination(icon=Icons.CALCULATE_OUTLINED, label="Standard",selected_icon=Icons.CALCULATE),
#             NavigationDrawerDestination(icon=Icons.SCIENCE_OUTLINED, label="Scientific",selected_icon=Icons.SCIENCE),
#             NavigationDrawerDestination(icon=Icons.CALENDAR_MONTH_OUTLINED, label="Date Calculation",selected_icon=Icons.CALENDAR_MONTH),
#             NavigationDrawerDestination(icon=Icons.COMPUTER_OUTLINED, label="Numbers System",selected_icon=Icons.COMPUTER),
            
            
#         ],
#     )
    
#     appbar = AppBar(title=Text("Numbers System",weight=FontWeight.BOLD),leading=IconButton(icon=Icons.MENU,on_click=lambda _:page.open(end_drawer))
#                     ,actions=[IconButton(icon=Icons.EXIT_TO_APP_OUTLINED,icon_color="red",on_click=lambda _: page.window.destroy())]
#                     ,shadow_color="black",elevation=0)   
                                                
#     appli = Calc_4(page)
#     page.add(appbar,appli)  
#     page.update()   
# app(target=main)