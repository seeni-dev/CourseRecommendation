import handler

def testCSVHandler():
    csv=handler.CSVHandler("../DATA/input.csv")
    csv.open()
    print(csv.getData())
    return


if __name__ == '__main__':
    testCSVHandler()
