from flet import * 
from Second_interface import *
from first_interface import PSG
def main(page:Page):
    
    def Switch_Interfaces(e):
         
        if end_drawer.selected_index == 0:
            interface1 = PSG(page)
            page.controls.clear()  
            end_drawer.open = False  
            appbar.title = Text("Password Generator",weight=FontWeight.BOLD) 
            page.window.width =   900
            page.window.height = 500
            page.add(appbar,interface1)
            
        elif end_drawer.selected_index == 1 :
            
            interface2 =PSG_2(page=page)  
           
            page.controls.clear()  
            end_drawer.open = False   
            appbar.title = Text("Password Manager",weight=FontWeight.BOLD)
            page.window.width =   900
            page.window.height =  500
            page.padding =0  
            page.add(appbar,interface2)
        page.update()       
             
    
        
    end_drawer = NavigationDrawer(
        tile_padding= 5,
        selected_index=0,
        shadow_color="white",
        indicator_shape=RoundedRectangleBorder(radius=BorderRadius(10,10,10,10)),
        position=NavigationDrawerPosition.START,
        indicator_color="#e0e0e0",  
        bgcolor="#191c20",
        on_change=Switch_Interfaces,
        
        controls=[
            NavigationDrawerDestination(icon=Icons. PASSWORD_OUTLINED, label="Password Generator",selected_icon=Icons.PASSWORD),
            NavigationDrawerDestination(icon=Icons.DATA_ARRAY, label="Password Manager",selected_icon=Icons.DATA_ARRAY_OUTLINED),
        ],
    )

    appbar = AppBar(
        actions=[IconButton(icon=Icons.EXIT_TO_APP_ROUNDED,on_click=lambda e: page.window.destroy())] ,
        leading=IconButton(icon=Icons.MENU, on_click=lambda e: page.open(end_drawer)),
        title=Text("Passwords Table",size=20),
        elevation=5,
        surface_tint_color="#1d1e2a",
        shadow_color="#1d1e2a",
        bgcolor="#1d1e2a",
        color="White"
    )

    page.add(appbar)
    Switch_Interfaces(e=5)
    page.update()
app(main)