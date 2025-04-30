import os 
import datetime
from flet import *


def main(page:Page):
    page.window.icon = "C:\\Users\\Computec\\Downloads\\Icons\\tablet.ico"
    page.title = "PC Control"
    page.padding = 0
    page.window.width = 600
    page.window.height = 400
    page.window.max_width = page.window.min_width = 600
    page.window.max_height = page.window.min_height = 400
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = False
    page.window.center()
    
    
    def on_dismiss_sh(e):
        try:
            seconds = cupertino_timer_picker.value    
            os.system(f"Shutdown /s /t {seconds}")
            hours,seconds = divmod(seconds,3600)
            minutes ,seconds = divmod(seconds,60)
            current_time = datetime.datetime.now()
            time = str(datetime.timedelta(hours=hours,minutes=minutes,seconds=seconds)+ datetime.timedelta(hours=current_time.hour,minutes=current_time.minute,seconds=current_time.second))
            time = datetime.datetime.strptime(time,"%H:%M:%S")
            formatted_date_time = time.strftime('%I:%M:%S %p')
            text.value = f"\nPC Will Closed in {formatted_date_time}"
            page.update()
        except:
            pass
       
    
    def on_dismiss_re(e):
        try:
            seconds = cupertino_timer_picker.value    
            os.system(f"Shutdown /r /t {seconds}")
            hours,seconds = divmod(seconds,3600)
            minutes ,seconds = divmod(seconds,60)
            current_time = datetime.datetime.now()
            time = str(datetime.timedelta(hours=hours,minutes=minutes,seconds=seconds)+ datetime.timedelta(hours=current_time.hour,minutes=current_time.minute,seconds=current_time.second))
            time = datetime.datetime.strptime(time,"%H:%M:%S")
            formatted_date_time = time.strftime('%I:%M:%S %p')
            text.value = f"\nPC Will Restart in {formatted_date_time}"
            page.update()
        except:
            pass
    
        
    def on_dismiss_cancel(e):
        os.system("shutdown /a")
        text.value = f"\nThe operation has been cancelled."
        page.update()

    #! ===================================================== App Bar ==============================================================
    appbar = AppBar(
        title=Text("PC Control",style=TextStyle(weight=FontWeight.BOLD)),
        shadow_color="red",
        color="red",
        bgcolor="black",
        actions=[IconButton(icon=icons.EXIT_TO_APP,on_click=lambda _:page.window.destroy())]
        )
    #! ===================================================== Container ==============================================================
    cupertino_timer_picker = CupertinoTimerPicker(
        value=0,
        second_interval=1,
        minute_interval=1,
        mode=CupertinoTimerPickerMode.HOUR_MINUTE_SECONDS)
    
   
    image = Image(src="D:\\Python\\Mobile Application - Flet\\Animation - 1724440730680.gif")
    Shutdown_button = ElevatedButton(text="Shutdown",icon=icons.POWER_SETTINGS_NEW_ROUNDED,icon_color="red",color="red",bgcolor="black",on_click=lambda _:   page.open(CupertinoBottomSheet(cupertino_timer_picker,height=100,bgcolor="red",on_dismiss=on_dismiss_sh)))
    restart_button = ElevatedButton(text="Restart",icon=icons.RESTART_ALT_SHARP,icon_color="red",color="red",bgcolor="black",on_click=lambda _: page.open(CupertinoBottomSheet([cupertino_timer_picker],height=100,bgcolor="red",on_dismiss=on_dismiss_re)))
    cancel_button = ElevatedButton(text="Cancel",icon=icons.CANCEL_OUTLINED,icon_color="red",color="red",bgcolor="black",on_click=on_dismiss_cancel)
    elemints = Row([Shutdown_button,restart_button,cancel_button],tight=False,wrap=False,spacing=40,alignment=MainAxisAlignment.CENTER)
    text = Text(style=TextStyle(size=20,weight=FontWeight.BOLD,shadow=BoxShadow(spread_radius=30,color="black",offset=(2,2),blur_radius=5)))
                                                                                                           
    text_2 = Row([text],alignment=MainAxisAlignment.CENTER)
    container = Container(width=600,height=400,
                        gradient=LinearGradient(colors=["black","red"],stops=[0.05,0.75],begin=alignment.top_center,end=alignment.bottom_center),
                        content=Column([Row([image],alignment=MainAxisAlignment.CENTER),elemints,text_2],alignment=MainAxisAlignment.START)
                        )
    page.add(appbar,container)
    page.update() 
app(main) 