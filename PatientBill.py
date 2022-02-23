import PatientClass as pa
import ProcedureClass as proc

Matt = pa.Patient(1,"Matt Jones", '123 Main st, Waco TX 76706','254-555-7415',True)

proc1 = proc.Procedure('Physical Exam','2/15/2022','Dr. Irvine',250,1)
proc2 = proc.Procedure("MRI",'2/15/2022','Dr. Hamilton',1500,1)
proc3 = proc.Procedure('CT Scan','2/17/2022','Dr. Drey',1200,2)


listofprocs = [proc1,proc2,proc3]
patientTCost = 0

print('*** Patient Bill ***')
print("Name: ",Matt.get_Name())
print("Address: ", Matt.get_addy())
print('Phone: ',Matt.get_phone())

for Procedure in listofprocs:
    if Procedure.get_patientID() == Matt.get_ID():
        print("")
        print('Procedure: ', Procedure.get_procName())
        print('Practitioner: ', Procedure.get_practitioner())
        print('Date: ', Procedure.get_date())
        print('Charge: ', Procedure.get_cost())
        patientTCost += Procedure.get_cost()
if  Matt.get_vetstat() == True:
    patientTCost = patientTCost*.6

print('')
print('Total Charges: $',format(patientTCost,',.2f'))


