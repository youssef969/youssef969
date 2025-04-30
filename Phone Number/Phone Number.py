from flet import * 
from phonenumbers import carrier , timezone , geocoder
import phonenumbers 


def main(page:Page):
    page.title = "Phone Number"
    page.window.icon = "C:\\Users\\Computec\\Downloads\\Icons\\phone.ico"
    page.padding = 0
    page.window.max_width = page.window.min_width = page.window.width = 600
    page.window.max_height = page.window.min_height = page.window.height = 400
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = False
    page.window.center()
    #! ========================================= Functions ==================================================
    
    def Change_textfeild(e):
        if len(phone_number.value) >= 7 :                   #* Search Button is on 
            search_button.disabled = False              
            
        elif len(phone_number.value) < 7:                   #* Search Button is Off
            search_button.disabled = True
        search_button.update()
        
    def search(e):
        try:
            phone_number.error_text = ""
            phonenumber = f"+{phone_number.value}"
            entered_number = phonenumbers.parse(phonenumber)
            geo = geocoder.description_for_number(entered_number,"en")
            cari = carrier.name_for_number(entered_number,"en")
            timez = timezone.time_zones_for_number(entered_number)
            country_text.value = geo
            company_text.value = cari
            city_text.value = timez[0]
            country_icon.opacity = company_icon.opacity = city_icon.opacity = 1 
        except:
            phone_number.error_text = "Something wrong in Phone Number, please try Again "
        page.update() 
            
            
    def claer(e):
        country_text.value = company_text.value = city_text.value = ""
        country_icon.opacity = company_icon.opacity =  city_icon.opacity = 0
        phone_number.value = ""
        phone_number.error_text = ""
        Change_textfeild(e=5)
        page.update()
    
    #! ========================================= AppBar ==================================================
    appbar = AppBar(
        title_spacing=5,
        title= Text("Phone Recognition",style=TextStyle(weight=FontWeight.BOLD,size=20)),
        leading_width=200,
        color="white",
        bgcolor= "#1cb5e0",
        actions=[IconButton(icon=icons.LOGOUT_ROUNDED,icon_color="white",on_click=lambda _:page.window.destroy())])
                 
    #! ========================================= Container ==================================================
    #* ========================================= textFeild ==================================================
    phone_number = TextField(
        multiline=False,
        error_text= "",
        error_style=TextStyle(size=10,weight=FontWeight.W_400),
        label="Phone Number",
        label_style=TextStyle(color="black"),
        prefix_icon=icons.PHONE_ANDROID,
        input_filter=InputFilter(regex_string=r"[0-9]"),
        prefix_text="+",
        prefix_style=TextStyle(color="black"),
        width=300,
        border_radius=10,
        border_width=2,
        focused_border_color="Black",
        on_change=Change_textfeild
        )
    phone_number_row = Row(controls=[phone_number],alignment=MainAxisAlignment.CENTER,tight=False,wrap=False)
    
    #* ========================================= Buttons ==================================================
    search_button = ElevatedButton(icon=icons.SEARCH_ROUNDED,text="Search",disabled=True,on_click=search)
    clear_button = ElevatedButton(icon=icons.CLEAR_ALL_ROUNDED,text="Clear",on_click=claer)
    Bottons_row = Row(controls=[search_button,clear_button],alignment=MainAxisAlignment.CENTER,tight=False,wrap=False,spacing=60)
    
    #* ========================================= Text ==================================================
    country_icon = Icon(icons.LOCATION_ON,color="White",opacity=0,animate_opacity=300)
    country_text = Text(value="",color="white",style=TextStyle(weight=FontWeight.BOLD,size=20),opacity=1,animate_opacity=300)
    country_row = Row(controls=[country_icon,country_text],alignment=MainAxisAlignment.CENTER)
    
    company_icon = Icon(icons.CALL_MADE,color="White",opacity=0,animate_opacity=300)
    company_text = Text(value="",color="white",style=TextStyle(weight=FontWeight.BOLD,size=20),opacity=1,animate_opacity=300)
    company_row = Row(controls=[company_icon,company_text],alignment=MainAxisAlignment.CENTER)
    
    city_icon = Icon(icons.LOCATION_CITY,color="White",opacity=0,animate_opacity=300)
    city_text = Text(value="",color="white",style=TextStyle(weight=FontWeight.BOLD,size=20),opacity=1,animate_opacity=300)
    city_row = Row(controls=[city_icon,city_text],alignment=MainAxisAlignment.CENTER)
    
    
    container = Container(bgcolor="red",width=600,height=340,padding=8,alignment=alignment.top_center,
                        gradient=LinearGradient(colors=["#000853", "#1cb5e0"],stops=[0.3,0.9],end=alignment.top_center,begin=alignment.bottom_center),
                        content=Column(controls=[phone_number_row,Bottons_row,country_row,company_row,city_row],spacing=20)
                        )
    
    page.add(appbar,container)
    page.update()  
app(main)