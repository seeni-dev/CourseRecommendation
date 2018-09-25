import Handler
import Preprocessor
import Model

def Train():
    """
       Trains the model with data from DATA/input.csv
    :return:
    """
    # initialize source -csv source
    csvhand = Handler.CSVHandler("../DATA/input.csv")
    train_data = csvhand.getData()
    train_data_pro = Preprocessor.preprocess(train_data)
    Model.Init() #intialize the model
    labels_ = Model.Train(train_data_pro)
    return

def Predict():
    """
        Predicts the data from DATA/test.csv
    :return:
    """

    #get user input from file test.csv
    csvhand=Handler.CSVHandler("../DATA/test.csv")
    pred_data=csvhand.getData()
    pred_data_pro=Preprocessor.preprocess(pred_data,train=False)
    fieldsInData=list(Preprocessor.getFI())+list(Preprocessor.getSubjects()) # fields are FI_X and S_X
    predictions=Model.Predict(pred_data_pro)
    C = Model.getClusterCenters() #cluster centers
    for pred_i in range(len(predictions)):
        pred=predictions[pred_i] #get the prediciton vlaue form the list
        Ctarget=C[pred]  # get the corresponding cluster
        student=pred_data_pro.values[pred_i] #get the row of values (for a student) for which predicition is done
        print("Needed ",end=" ")
        for att_i in range(len(fieldsInData)):
            Catt=Ctarget[att_i] #Cluster attribute value
            studentAtt=student[att_i]  # attribute value present in thhe
            field=fieldsInData[att_i]  # column name
            if(Catt>0.5): #if the value is high . Value might me changed later
                print(field,end=" ") # print the field or append it to the result array
        print()
    return

if __name__ == '__main__':
    Train()
    Predict()
