from datetime import date

class Kid:
    def __init__(self, studentIg,Name,DOB,classification):
        self.__studentID = studentIg
        self.__Name = Name
        self.__DOB = DOB
        self.__classification = classification
   

    def get_Name(self):
        return self.__Name

    def set_age(self):
        age = date.today().year-int(self.__DOB[-4:])
        self.__age = age
    
    def when_do_i_reg(self):
        if self.__classification == 'F':
            self.__regtime = '4/10 thru 4/12'
        elif self.__classification == 'S':
            self.__regtime = '4/7 thru 4/9'
        elif self.__classification == 'Jr':
            self.__regtime = '4/4 thru 4/6'
        elif self.__classification == 'Sr':
            self.__regtime = '4/1 thru 4/3'
        else:
            self.__regtime = "did that guy graduate or something?"
    
    def get_age(self):
        return self.__age
    
    def get_regtime(self):
        return self.__regtime
