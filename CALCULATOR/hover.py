from flet import * 

class Hover:
    @staticmethod
    def Button_hover (e,button :ElevatedButton, hover_icon:Icons,old_icon:Icons): 
        if e.data == "true":
            button.icon = hover_icon 
        elif e.data == "false":
            button.icon = old_icon 
        button.update()