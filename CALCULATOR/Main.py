from flet import * 
from Calculator import Calc_1
from Calculator_2 import Date_clac
from Calculator_3 import Calc_3
from Calculator_4 import Calc_4
from mode import Mode

def Main(page:Page):
     
    page.title = "Calculator"
    page.window.icon = "C:\\Users\\Computec\\Downloads\\Icons\\calculator (2).ico"
    # page.window.width = 660
    # page.window.height = 440
    # page.window.max_width = 660 
    # page.window.max_height = 440
    # page.window.top = 200
    # page.window.left = 200
    page.window.center()
    
    
    def Switch_Interfaces(e):
         
        if end_drawer.selected_index == 0:
            interface1 = Calc_1()
            page.controls.clear()  
            end_drawer.open = False  
            appbar.title = Text("Standard",weight=FontWeight.BOLD) 
            page.window.width =   660
            page.window.height = 400
            page.add(appbar,interface1)
            
        elif end_drawer.selected_index == 1 :
            
            interface2 =Calc_3(page=page)  
           
            page.controls.clear()  
            end_drawer.open = False   
            appbar.title = Text("Sceintific",weight=FontWeight.BOLD)
            page.window.width =   660
            page.window.height =  450
            page.padding =0  
            page.add(appbar,interface2)
           
        elif end_drawer.selected_index == 2 :
            interface3 = Date_clac(page=page)    
            page.controls.clear() 
            end_drawer.open = False   
            appbar.title = Text("Data Calculation",weight=FontWeight.BOLD)
            page.window.width = 660
            page.window.height = 440
            page.padding = 5
            page.add(appbar,interface3)
        
        elif end_drawer.selected_index == 3 :
            interface4 = Calc_4(page=page)    
            page.controls.clear() 
            end_drawer.open = False   
            appbar.title = Text("Numbers System",weight=FontWeight.BOLD)
            page.window.width = 660
            page.window.height = 440
            page.add(appbar,interface4)

        page.update()       
             
    
        
    end_drawer = NavigationDrawer(
        tile_padding= 5,
        selected_index=0,
        indicator_shape=RoundedRectangleBorder(radius=BorderRadius(10,10,10,10)),
        position=NavigationDrawerPosition.START,
        indicator_color=["#e0e0e0","#3b3b3b"],  
        on_change=Switch_Interfaces,
        controls=[
            NavigationDrawerDestination(icon=Icons.CALCULATE_OUTLINED, label="Standard",selected_icon=Icons.CALCULATE),
            NavigationDrawerDestination(icon=Icons.SCIENCE_OUTLINED, label="Scientific",selected_icon=Icons.SCIENCE),
            NavigationDrawerDestination(icon=Icons.CALENDAR_MONTH_OUTLINED, label="Date Calculation",selected_icon=Icons.CALENDAR_MONTH),
            NavigationDrawerDestination(icon=Icons.COMPUTER_OUTLINED, label="Numbers System",selected_icon=Icons.COMPUTER)
          
        ],
    )
    mode = IconButton(icon=Icons.DARK_MODE,on_click=lambda _: Mode.theme_changed(page=page,Button=mode))
    appbar = AppBar(title=Text("Standard",weight=FontWeight.BOLD),leading=IconButton(icon=Icons.MENU,on_click=lambda _:page.open(end_drawer))
                    ,actions=[mode,IconButton(icon=Icons.EXIT_TO_APP_OUTLINED,icon_color="red",on_click=lambda _: page.window.destroy())])   
   
    #! ================================================ Controls ========================================================   
    
    page.add(appbar)
    Switch_Interfaces(e=5)
    Mode.load(page,mode)
    page.update()
app(Main)