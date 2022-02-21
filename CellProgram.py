import CellClass as c

def main():
    mitelefono = c.Cell('Pear',"i720",750)

    print(mitelefono.get_manufact())
    print(mitelefono.get_model())
    print(mitelefono.get_retail_price())

    mitelefono.set_manufact("Googol")
    mitelefono.set_model("universe")
    mitelefono.set_retail_price(420)

    print(mitelefono.get_manufact())
    print(mitelefono.get_model())
    print(mitelefono.get_retail_price())

main()