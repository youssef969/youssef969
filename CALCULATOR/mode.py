from flet import *
import json 

class Mode:
    is_dark_mode = False
    
    @staticmethod
    def theme_changed(page:Page , Button :IconButton):
        Mode.is_dark_mode
        Mode.is_dark_mode = not Mode.is_dark_mode
        page.theme_mode = ThemeMode.DARK if Mode.is_dark_mode else ThemeMode.LIGHT
        Button.icon=Icons.DARK_MODE if Mode.is_dark_mode else Icons.LIGHT_MODE
        state = {"switch_state": Mode.is_dark_mode}
        with open(r"D:\Flet - Cross Platform\1.CALCULATOR\switch_state.json", "w+") as f:
            json.dump(state, f)
        
        
        page.update()
        
    @staticmethod
    def load(page:Page , Button :IconButton):
        Mode.is_dark_mode
        with open(r"D:\Flet - Cross Platform\1.CALCULATOR\switch_state.json","r") as f:
            state = json.load(f)
            Mode.is_dark_mode = state["switch_state"]
            if state["switch_state"] == True:
                    Mode.is_dark_mode = True
                    Button.icon=Icons.DARK_MODE
                    page.theme_mode = ThemeMode.DARK
            else:   
                    Mode.is_dark_mode = False
                    Button.icon = Icons.LIGHT_MODE
                    page.theme_mode = ThemeMode.LIGHT
        