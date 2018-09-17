import handler
import Preprocessor
import Model
from sklearn.metrics import accuracy_score

def testDrive():
    #initialize sources and models
    csvhand=handler.CSVHandler("../DATA/input.csv")
    csvhand.open()
    train_data=csvhand.getData()
    train_data_pro=Preprocessor.preprocess(train_data)
    labels=train_data_pro["FI"]
    Model.Init()
    labels_=Model.Train(train_data_pro)
    print(labels_)
    print(Model.getClusterCenters())
    print(Preprocessor.FIDict)
    print("Accuracy",accuracy_score(labels,labels_))
    print(Model.getInertia())

if __name__ == '__main__':
    testDrive()
