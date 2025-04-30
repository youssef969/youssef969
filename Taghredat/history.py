import json
import os


class History:
    def Add_to_history(topic:str):
        history = []
        try:
            with open(__file__.removesuffix("history.py")+"history.json","r",encoding='utf-8') as file:
                data = json.load(file)
                try:
                    for x in data:
                        history.append(x)
                except:
                    pass
                history.append(topic)
            with open(__file__.removesuffix("history.py")+"history.json","w+",encoding='utf-8') as file:
                json.dump(history, file, indent=2,ensure_ascii=False)
        except FileNotFoundError:
            with open(__file__.removesuffix("history.py")+"history.json","w+",encoding='utf-8') as file:
                history.append(topic)
                json.dump(history, file, indent=2,ensure_ascii=False)
            
         

        

    def read_history():
        try:
            with open(__file__.removesuffix("history.py")+"history.json","r",encoding='utf-8') as f:
                file_path = json.load(f)
                return file_path
        except:
            pass
            
    
    def Delete_history():
        with open(__file__.removesuffix("history.py")+"history.json","w+",encoding='utf-8') as file:
            data = []
            json.dump(data, file, indent=2)