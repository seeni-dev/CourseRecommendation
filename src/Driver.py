import handler
import Preprocessor
import model

def testDrive():
    #initialize sources and models
    csvhand=handler.CSVHandler()
    csvhand.open()
    train_data=csvhand.getData()
    train_data_pro=Preprocessor.preprocess(train_data)
    model.init()
    model.train(train_data_pro)
    model.predict(train_data_pro)
    print(model.clusters)
