import json 


class Folder_path:

    def save_folder_path(folder:str):
        try:
            with open(__file__.removesuffix("folder_path.py")+"folder_path.json","w",encoding='utf-8') as f:
                image = [folder]
                json.dump(image,f,indent=2,ensure_ascii=False)
        except:
            pass
    
    
    def read_folder_path():
        try:
            with open(__file__.removesuffix("folder_path.py")+"folder_path.json","r",encoding='utf-8') as f:
                file_path = json.load(f)
                return f"{file_path[0]}"
        except:
            pass
        

