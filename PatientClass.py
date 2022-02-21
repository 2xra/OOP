class patient:
    def __init__(self,ID,name,address,phone,vetstat):
        self.__ID = ID
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__vetstatus = vetstat

    def get_ID(self):
        return self.__ID
        
    def get_Name(self):
        return self.__name

    def get_addy(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_vetstat(self):
        return self.__vetstatus