import handler
import Preprocessor
import Model

def testDrive():
    #initialize sources and models
    csvhand=handler.CSVHandler("../DATA/input.csv")
    csvhand.open()
    train_data=csvhand.getData()
    train_data_pro=Preprocessor.preprocess(train_data)
    Model.Init()
    Model.Train(train_data_pro)
    print(Model.getClusterCenters())


if __name__ == '__main__':
    testDrive()
