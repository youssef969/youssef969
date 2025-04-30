from flet import * 
from DT_Handling import *

# "#42445f","#393b52","#33354a","#2f3143","#292b3c" ,"#222331","#1a1a25","#1a1b26" ,"#21222f","#1d1e2a"
        
class PSG_2(Column):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        page.window.width = 900
        page.window.height = 500
        page.window.maximizable= page.window.resizable =  False
        page.padding = 0
        page.scroll = "Auto"
        page.window.center()

        #! ================================================================ DataTable ======================================================
        data = DataTable(width=900,bgcolor="#222331",border=border.all(3, Colors.WHITE30),border_radius=5,vertical_lines=BorderSide(3, Colors.AMBER_700),
            horizontal_lines=BorderSide(1, Colors.AMBER_500),sort_column_index=0,sort_ascending=True,heading_row_color="#2f3143",
            heading_row_height=60,data_row_color={ControlState.HOVERED: "#FF0000"},show_checkbox_column=False,divider_thickness=0,show_bottom_border=True,
            column_spacing=100,
            
            columns=[
                DataColumn(
                    Text("Website Name",color="White"), 
                ),
                DataColumn(
                    Text("Website Link",color="White"),
                  
                ),
                DataColumn(
                    Text("Password",color="White"),
                ),
                DataColumn(
                    Text("Actions",color="White"),
                ),
            ],
            
        )

        self.SB_text = Text(value="")
        self.Snackbar = SnackBar(content=self.SB_text,open=False,show_close_icon=True)

        data_table = DT(page,data,self.Snackbar,self.SB_text)
        data_table.Show_data()

        self.column= Column(controls=[data,self.Snackbar])
        self.Continer_1= Container(content=self.column,width=900,height=440,expand=2,alignment=alignment.center,padding=2,
        gradient=RadialGradient(
        center=alignment.bottom_left,
        radius= 4.4,
        colors=["#42445f","#393b52","#33354a","#2f3143","#292b3c" ,"#222331","#1a1a25","#1a1b26" ,"#21222f","#1d1e2a","Black"]))

        
        self.controls = [self.Continer_1]



    









# def main(page:Page):
    
#     page.appbar = AppBar(
#         actions=[IconButton(icon=icons.EXIT_TO_APP_ROUNDED,on_click=lambda e: page.window.destroy())] ,
#         leading=IconButton(icon=icons.MENU),
#         title=Text("Passwords Table",size=20),
#         elevation=5,
#         surface_tint_color="#1d1e2a",
#         shadow_color="#1d1e2a",
#         bgcolor="#1d1e2a",
#         color="White"
#     )
#     interface = PSG_2(page)
#     page.add(interface)
#     page.update()
# app(main)