import insectclass as bugs

def main():
    ladybug = bugs.insect()
    ladybug.fly()
    print("your bug can fly " + ladybug.getflight().__str__() + " miles.")

main()
