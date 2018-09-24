import handler
import Preprocessor
import Model

def Train():
    # initialize sources and models
    csvhand = handler.CSVHandler("../DATA/input.csv")
    csvhand.open()
    train_data = csvhand.getData()
    labels = train_data["FI"]
    train_data_pro = Preprocessor.preprocess(train_data)
    Model.Init()
    labels_ = Model.Train(train_data_pro)
    return

def Predict():
    #get user input from file test.csv
    csvhand=handler.CSVHandler("../DATA/test.csv")
    csvhand.open()
    pred_data=csvhand.getData()
    labels=pred_data["FI"]
    pred_data_pro=Preprocessor.preprocess(pred_data,train=False)
    fieldsInData=pred_data_pro.columns
    pred=Model.Predict(pred_data_pro)
    C = Model.getClusterCenters()
    for pre_i in range(len(pred)):
        #get the cluster center for it
        pre=pred[pre_i]
        Ctarget=C[pre]
        stu=pred_data_pro.values[pre_i]
        print("Needed ",end=" ")
        for att_i in range(len(fieldsInData)):
            Catt=Ctarget[att_i]
            stuatt=stu[att_i]
            field=fieldsInData[att_i]
            if(Catt>0.5):
                print(field,end=" ")
        print()
    return


def testDrive():
    #initialize sources and models
    csvhand=handler.CSVHandler("../DATA/input.csv")
    csvhand.open()
    train_data=csvhand.getData()
    labels=train_data["FI"]
    train_data_pro=Preprocessor.preprocess(train_data)
    Model.Init()
    labels_=Model.Train(train_data_pro)
    print(labels_)
    print(labels.values)
    print(len(train_data_pro.columns))
    fields=train_data_pro.columns
    columns_len=len(train_data_pro.columns)
    input_stu=[0]*columns_len
    input_stu[1]=1
    C=Model.getClusterCenters()
    pred=Model.Predict([input_stu])
    predictedCluster=C[pred][0] #0 is due to pandas data storing format
    for i in range(len(predictedCluster)):
        value=predictedCluster[i]
        if(value>0):
            print("CLuster Value",value,"Column ",fields[i],"index",i)

if __name__ == '__main__':
    Train()
    Predict()
