from flet import *


class number_sys:
    @staticmethod
    def numbersystem_to_text(number_system:int,data:str):
        if number_system ==10:
            text = ''.join(chr(int(decimal)) for decimal in data.split())
        else:
            binary_list = [int(byte, number_system) for byte in data.split()]
            binary_bytes = bytes(binary_list)
            text = binary_bytes.decode('utf-8')
        return text

    @staticmethod
    def convert_number_system(page:Page,Textfeild:TextField,output_textFeild:TextField,from_d:Dropdown, to_d :Dropdown):
        number = Textfeild.value
        from_base = from_d.value
        to_base = to_d.value
        #! Text Converter from and to 
        if to_base == "Text":
            output_textFeild.multiline = True
            
            if from_base == "Binary":
                output_textFeild.value = number_sys.numbersystem_to_text(2,str(number))
            elif from_base == "Decimal":
                output_textFeild.value = number_sys.numbersystem_to_text(10,str(number))
            elif from_base == "Hexadecimal":
                output_textFeild.value = number_sys.numbersystem_to_text(16,str(number))
            elif from_base == "Octal":
                output_textFeild.value = number_sys.numbersystem_to_text(8,str(number))
        elif from_base == "Text":
            Textfeild.multiline = True
            
            if to_base == 'Binary':
                output_textFeild.value = ' '.join(format(ord(char), '08b') for char in number)
            elif to_base == 'Decimal':
                output_textFeild.value = ' '.join(str(ord(char)) for char in number)
            elif to_base == 'Hexadecimal':
                output_textFeild.value = ' '.join(format(ord(char), '02x') for char in number)
            elif to_base == 'Octal':
                output_textFeild.value = ' '.join(format(ord(char), '03o') for char in number)
        else:    
            Textfeild.multiline = False
            output_textFeild.multiline = False
            
            #! Number Convertr from and to    
            if from_base == 'Binary':
                    decimal_number = int(number, 2)
            elif from_base == 'Octal':
                    decimal_number = int(number, 8)
            elif from_base == 'Decimal':
                    decimal_number = int(number)
            elif from_base == 'Hexadecimal':
                    decimal_number = int(number, 16)
                
            if to_base == 'Binary':
                    output_textFeild.value = bin(decimal_number)[2:]  
            elif to_base == 'Octal':
                    output_textFeild.value = oct(decimal_number)[2:]  
            elif to_base == 'Decimal':
                    output_textFeild.value = str(decimal_number)
            elif to_base == 'Hexadecimal':
                    output_textFeild.value = hex(decimal_number)[2:]
        page.update()

    
    @staticmethod
    def change_dropdpwn(page:Page,Textfeild:TextField,output_textFeild:TextField,from_d:Dropdown, to_d :Dropdown):

        Textfeild.hint_text = from_d.value
        output_textFeild.hint_text = to_d.value
       

        to_d.options = [dropdown.Option(text="Binary",key="Binary"),dropdown.Option(text="Decimal",key="Decimal"),dropdown.Option(text="Octal",key="Octal"),dropdown.Option(text="Hexadecimal",key="Hexadecimal"),dropdown.Option(text="Text",key="Text")]

        if from_d.value == "Text":
            Textfeild.prefix_icon = Icons.ABC_ROUNDED
            
        elif to_d.value == "Text":
            output_textFeild.prefix_icon = Icons.ABC_ROUNDED
            
        else:
            output_textFeild.prefix_icon = Textfeild.prefix_icon = Icons.NUMBERS
            if from_d.value == "Binary":
                to_d.options.pop(0)
            if from_d.value == "Decimal":
                to_d.options.pop(1)
            if from_d.value == "Octal":
                to_d.options.pop(2)
            if from_d.value == "Hexadecimal":
                to_d.options.pop(3)
            if from_d.value == "Text":
                to_d.options.pop(4)
        
        page.update()
        Textfeild.update()

    @staticmethod
    def Swap(page:Page,Textfeild:TextField,output_textFeild:TextField,from_d:Dropdown, to_d :Dropdown):
        to_d.options = [dropdown.Option(text="Binary",key="Binary"),dropdown.Option(text="Decimal",key="Decimal"),dropdown.Option(text="Octal",key="Octal"),dropdown.Option(text="Hexadecimal",key="Hexadecimal"),dropdown.Option(text="Text",key="Text")]
        From = from_d.value 
        To = to_d.value
        to_d.value = From
        from_d.value = To
        number_sys.change_dropdpwn(page,Textfeild,output_textFeild,from_d,to_d)
        page.update()

    @staticmethod
    def clear(page:Page,Textfeild:TextField,output_textFeild:TextField):
        Textfeild.value = ""
        output_textFeild.value = ""
        page.update()