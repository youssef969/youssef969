from flet import * 
import json
import datetime


class Date_clac(Column):
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
        
        self.date1 = datetime.date.today()
        self.date2 = datetime.date.today()
        self.date1_ans = [0] 
        self.date2_ans = [0] 
        self.from_text = Row([Text("From",color="#a7a7a7",font_family="Elephant")])
        
        self.combo_Box = Dropdown(width=220,
                            autofocus=False,
                            value="Diffrance between Dates",
                            border_radius=BorderRadius(10,10,10,10),
                            border_width=1,
                            max_menu_height=30,
                            on_change=self.Switch_mode,
                            
                            color ="#36618e",
                            text_style=TextStyle(weight=FontWeight.W_500),
                            
                            options=[dropdown.Option(text="Diffrance between Dates",key="Diffrance between Dates"),dropdown.Option(text="Add or Subtruct days",key="Add or Subtruct days")])
        
        #! ============================================================= Container 1 ========================================================
        self.to_text = Text("to",color="#a7a7a7",font_family="Elephant")
        self.Date1_picker = DatePicker(last_date=datetime.date(2600,12,31),on_change=self.change_date)
        self.Date2_picker = DatePicker(last_date=datetime.date(2600,12,31),on_change=self.change_date2)
        self.date1_button = ElevatedButton(icon=Icons.DATE_RANGE_ROUNDED,text=self.date1,on_click=lambda e: page.open(self.Date1_picker))
        self.date2_button = ElevatedButton(icon=Icons.DATE_RANGE_ROUNDED,text=self.date2,on_click=lambda e: page.open(self.Date2_picker))
        self.result_text = Text(value="0 days")
        self.result_text2 = Text(color="#989898")
        
        #! ============================================================= Container 2 ========================================================
        self.to_text = Text("to",color="#a7a7a7",font_family="Elephant")
        self.Date1_picker = DatePicker(last_date=datetime.date(2600,12,31),on_change=self.change_date)
        self.date1_button = ElevatedButton(icon=Icons.DATE_RANGE_ROUNDED,text=self.date1,on_click=lambda e: page.open(self.Date1_picker))
        self.rb = RadioGroup(on_change=self.clear,value=True,content=Row([Radio(label="Add",value=True),Radio(label="Subtract",value=False)]))
        
        self.option = [dropdown.Option(datetime.timedelta(i).days) for i in range(0, 1000)]
        
        self.drop_year = Dropdown(width=110,label="Year",value=0,options= self.option,border_radius=BorderRadius(10,10,10,10),on_change=self.Add)
        self.drop_month = Dropdown(width=110,label="Month",value=0,options= self.option,border_radius=BorderRadius(10,10,10,10),on_change=self.Add)    
        self.drop_day = Dropdown(width=110,label="Day",value=0,options= self.option,border_radius=BorderRadius(10,10,10,10),on_change=self.Add)  
        self.day_diff = Text()                                       
        self.continer_2 = Container(padding=10,content=Column([self.from_text,self.date1_button,self.rb,Row([self.drop_year,self.drop_month,self.drop_day]),self.day_diff],spacing=25))                                      
        
        
        self.continer_1 = Container(padding=10,height=440,content=Column([self.from_text,self.date1_button,Row([self.to_text]),self.date2_button,Row([self.result_text]),Row([self.result_text2])]))
        self.continer_1.visible = True
        
        
        self.Add(e=5)
        self.Calc(e=5)
        self.controls = [Row([self.combo_Box],wrap=True),self.continer_1,self.continer_2]
    
        
        
        
    # def theme_changed(self,e):
    #         if c.value == True:
    #             c.label = "Dark theme"
    #             page.theme_mode = ThemeMode.DARK
    #         else:
    #             c.label = "Light theme" 
    #             page.theme_mode = ThemeMode.LIGHT
    #         state = {"switch_state": c.value}
    #         with open("D:\\Python\\Mobile Application - Flet\\CALCULATOR\\switch_state.json", "w+") as f:
    #             json.dump(state, f)
    #         self.update()
            
    # def load(self,e):
    #         with open("D:\\Python\\Mobile Application - Flet\\CALCULATOR\\switch_state.json","r") as f:
    #             state = json.load(f)
    #             c.value = state["switch_state"]
    #             if state["switch_state"] == True:
    #                     c.value = True
    #                     c.label = "Dark theme"
    #                     page.theme_mode = ThemeMode.DARK
    #             else:   
    #                     c.value = False
    #                     c.label = "Light theme" 
    #                     page.theme_mode = ThemeMode.LIGHT
    def clear(self,e):
        self.drop_year.value = self.drop_month.value = self.drop_day.value = 0
        date_object = datetime.datetime.strptime(str(self.date1_button.text), '%Y-%m-%d')
        day_of_week = date_object.strftime("%A")
        self.day_diff.value = f"{day_of_week}, {date_object.date()}"  
        self.update()
        
        
    def change_date(self,e):
            from datetime import datetime
            self.date1_button.text = e.control.value.strftime('%Y-%m-%d')
            self.date1_button.text = datetime.strptime(self.date1_button.text, '%Y-%m-%d').date()
            self.date1_ans.append(self.date1_button.text)
            self.Date1_picker.current_date = self.date1_ans[-1]
            self.Calc(e=5)
            self.update()  
    
    def change_date2(self,e):
            from datetime import datetime
            self.date2_button.text = e.control.value.strftime('%Y-%m-%d')
            self.date2_button.text = datetime.strptime(self.date2_button.text, '%Y-%m-%d').date()
            self.date2_ans.append(self.date2_button.text)
            self.Date2_picker.current_date = self.date2_ans[-1]
            self.Calc(e=5)
            self.update()  
        
    def Calc(self,e):
            
            from datetime import datetime
            from dateutil.relativedelta import relativedelta
            
            difference = relativedelta(self.date2_button.text, self.date1_button.text)
            years = difference.years
            months = difference.months
            weeks = difference.weeks
            days = weeks * 7 - difference.days
            
            date1 = datetime.strptime(str(self.date1_button.text), '%Y-%m-%d').date()
            date2 = datetime.strptime(str(self.date2_button.text), '%Y-%m-%d').date()
            result = abs((date2 - date1))
            result = int(result.total_seconds() / 86400)
            
            
            
            message_parts = []
            if years == 0 and months == 0 and days == 0 and weeks == 0:
                self.result_text.value = "0 days"
            else:
                if years:
                    message_parts.append(f"{abs(years)} year{'s' if years > 1 else ''}")
                if months:
                    message_parts.append(f"{abs(months)} month{'s' if months > 1 else ''}")
                if weeks:
                    message_parts.append(f"{abs(weeks)} week{'s' if weeks > 1 else ''}")
                if days:
                    message_parts.append(f"{abs(days)} day{'s' if days > 1 else ''}")
                
                self.result_text.value = ", ".join(message_parts)
                self.result_text2.value = f"{result} days"
                
            self.update()
        
    def Add(self,e):
            from dateutil.relativedelta import relativedelta
            add_or_subtract = self.rb.value
            date = self.date1_button.text
            year =self.drop_year.value
            month = self.drop_month.value 
            day = self.drop_day.value
            if add_or_subtract == True:
                new_date =  date + relativedelta(years=int(year),months=int(month),days=int(day))
                date_object = datetime.datetime.strptime(str(new_date), '%Y-%m-%d')
                day_of_week = date_object.strftime("%A")
                self.day_diff.value = f"{day_of_week}, {date_object.date()}"
            else:
                new_date =  date - relativedelta(years=int(year),months=int(month),days=int(day))
                date_object = datetime.datetime.strptime(str(new_date), '%Y-%m-%d')
                day_of_week = date_object.strftime("%A")
                self.day_diff.value = f"{day_of_week}, {date_object.date()}"
            self.update()
            
    def Switch_mode (self,e):
        if self.combo_Box.value == "Add or Subtruct days":
            self.combo_Box.autofocus == False
            
            self.continer_2.visible = True
            self.continer_1.visible = False
        else:
            self.combo_Box.autofocus == False
            self.continer_2.visible = False
            self.continer_1.visible = True
        
        self.page.update()
        
# def main(page:Page):
    
    
#     #! ================================================ Controls ========================================================   
#     #c= Switch(label="Light theme", on_change=theme_changed ,label_position=LabelPosition("right"))
    
    
#     end_drawer = NavigationDrawer(
#         tile_padding= 5,
#         selected_index=2,
#         indicator_shape=RoundedRectangleBorder(radius=BorderRadius(10,10,10,10)),
#         position=NavigationDrawerPosition.START,
#         indicator_color=["#e0e0e0","#3b3b3b"],
#         controls=[
#             NavigationDrawerDestination(icon=Icons.CALCULATE_OUTLINED, label="Standard",selected_icon=Icons.CALCULATE),
#             NavigationDrawerDestination(icon=Icons.SCIENCE_OUTLINED, label="Scientific",selected_icon=Icons.SCIENCE),
#             NavigationDrawerDestination(icon=Icons.CALENDAR_MONTH_OUTLINED, label="Date Calculation",selected_icon=Icons.CALENDAR_MONTH),
            
            
#         ],
#     )
    
#     appbar = AppBar(title=Text("Date Calculation",weight=FontWeight.BOLD),leading=IconButton(icon=Icons.MENU,on_click=lambda _:page.open(end_drawer))
#                     ,actions=[IconButton(icon=Icons.EXIT_TO_APP_OUTLINED,icon_color="red",on_click=lambda _: page.window.destroy())]
#                     )   
                                                
#     appli = Date_clac(page=page)
#     page.add(appbar,appli)     
# app(target=main)