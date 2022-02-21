

class Cell:
    def __init__(self, manuf,modL,RetPrice):
        self.__manufact = manuf
        self.__model = modL
        self.__retail_price = RetPrice
    

    def set_manufact(self,new_manuf):
        self.__manufact = new_manuf
    
    def set_model(self,new_modL):
        self.__model = new_modL
    
    def set_retail_price(self,newRetPrice):
        self.__retail_price = newRetPrice
    
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
