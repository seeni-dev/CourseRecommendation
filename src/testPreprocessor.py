import Preprocessor as pr
import handler as han

def testPreProcessor():
    csvhand=han.CSVHandler("../DATA/input.csv")
    csvhand.open()
    data=csvhand.getData()
    data_train=pr.preprocess(data)
    csvhand=han.CSVHandler("../DATA/input.csv")
    csvhand.open()
    data_test = csvhand.getData()
    data_test=pr.preprocess(data_test,train=False)
    import pdb
    pdb.set_trace()
    return

def testmakeDict(col):
    print(pr.makeDict(col))


testPreProcessor()
