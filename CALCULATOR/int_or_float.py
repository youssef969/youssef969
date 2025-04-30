class Check:
    
    @staticmethod
    def check_int_or_float(s:str):
        try:
            int_value = int(s)
            return int_value
        except ValueError:
            try:
                if s.endswith(".0") == True:
                    return int(s.removesuffix(".0"))
                else:
                    float_value = float(s)
                    return float_value
            except ValueError:
                pass    