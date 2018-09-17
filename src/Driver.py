import handler
import Preprocessor
import Model
from sklearn.metrics import accuracy_score

def getBestModel(iteration=100):
    """

    :param iteration: no of random models that has to be searched
    :return: best model with high accuracy
    """
    bestAccuracy=0
    bestModel=[]
    bestLoss=0

    # initialize sources and models
    csvhand = handler.CSVHandler("../DATA/input.csv")
    csvhand.open()
    train_data = csvhand.getData()
    train_data_pro = Preprocessor.preprocess(train_data)
    labels = train_data_pro["FI"]

    for _ in range(iteration):
        Model.Init()
        labels_=Model.Train(train_data_pro)
        acc=accuracy_score(labels,labels_) * 100
        loss=Model.getCost()
        if(acc>bestAccuracy):
            print(acc,end=" ")
            print(Model.getRandomState())
            bestAccuracy=acc
            bestModel=Model.model
            bestLoss=loss

    Model.model=bestModel
    print("BEST ACCURACY OVER TRAIN DATA: {}".format(bestAccuracy))
    print("LOSS: {}".format(bestLoss))
    print(Model.getRandomState())

def testDrive():
    #initialize sources and models
    csvhand=handler.CSVHandler("../DATA/input.csv")
    csvhand.open()
    train_data=csvhand.getData()
    train_data_pro=Preprocessor.preprocess(train_data)
    labels=train_data_pro["FI"]
    Model.Init()
    labels_=Model.Train(train_data_pro)
    print("Accuracy",accuracy_score(labels,labels_))
    print(Model.getCost())

if __name__ == '__main__':
    getBestModel(1000)
