import Preprocessor as pr
import handler as han


def testOpen():
    csvHandler=han.CSVHandler("../DATA/input.csv")
    csvHandler.open() #todo remove this kind of useless  code
    data=csvHandler.getData()
    print(data)
    print("Done Open")
    return

def testPreProcessor():
    csvHandler = han.CSVHandler("../DATA/input.csv")
    csvHandler.open()  # todo remove this kind of useless  code
    data = csvHandler.getData()
    data=pr.preprocess(data)
    print(data)
    return

def testmakeDict(col):
    print(pr.makeDict(col))


if __name__ == '__main__':
    testOpen()
    testPreProcessor()
