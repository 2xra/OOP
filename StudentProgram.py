import StudentClass as k

Superboy = k.Kid(1234,'Clark Kent','12/1/1938',"Sr")

Superboy.set_age()
print(Superboy.get_Name().__str__()+" is " +Superboy.get_age().__str__())

Superboy.when_do_i_reg()
print("and he registers between "+Superboy.get_regtime())
