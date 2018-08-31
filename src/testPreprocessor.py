import Preprocessor as pr
import handler as han

def testPreProcessor():
    csvhand=han.CSVHandler("../DATA/input.csv")
    csvhand.open()
    data=csvhand.getData()
    data_p=pr.preprocess(data)
    return

def testmakeDict(col):
    print(pr.makeDict(col))

testmakeDict(["A","B","A","C","B"])

testPreProcessor()
