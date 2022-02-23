class Procedure:
    def __init__(self,procName,opDate,Doc,cost,patID):
        self.__procedurename = procName
        self.__dateOfProcedure = opDate
        self.__Practitioner = Doc
        self.__charges = cost
        self.__patID = patID

    def get_patientID(self):
        return self.__patID
        
    def get_procName(self):
        return self.__procedurename

    def get_date(self):
        return self.__dateOfProcedure

    def get_practitioner(self):
        return self.__Practitioner

    def get_cost(self):
        return self.__charges