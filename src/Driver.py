import Handler
import Preprocessor
import Model
import pandas as pd
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

def PredictRaw(studentRecord):
    """
        Predicts the data from DATA/test.csv
    :studentRecord: data of the format [ID,FI,E1...E2] ID and FI are must
    :return: list of subjects he should have studied
    """

    pred_data=pd.DataFrame().from_records([studentRecord])
    pred_data.columns=["ID","FI","E","E","E"]
    pred_data_pro=Preprocessor.preprocess(pred_data,train=False)
    FI=list(Preprocessor.getFI())
    subjects=list(Preprocessor.getSubjects())
    fieldsInData=FI+subjects # fields are FI_X and S_X
    predictions=Model.Predict(pred_data_pro)
    C = Model.getClusterCenters() #cluster centers

    pred=predictions[0] #get the prediciton value which is the only value present
    Ctarget=C[pred]  # get the corresponding cluster
    student=pred_data_pro.values[0] #get the row of values (for a student) for which predicition is done
    print("Needed ",end=" ")
    result={
        "FI":None,
        "S":[]
    }
    for att_i in range(len(fieldsInData)):
        Catt=Ctarget[att_i] #Cluster attribute value
        studentAtt=student[att_i]  # attribute value present in thhe
        field=fieldsInData[att_i]  # column name
        if(Catt>0.5): #if the value is high . Value might me changed later
            print(field,end=" ") # print the field or append it to the result array
            if(field in FI):
                result["FI"]=field
            else:
                result["S"].append(field)
    print()
    return result

def getDifficulty():
    return {
        "ML":70,
        "SC":80,
        "DM":50,
        "SA":40,
        "DC":30,
        "AE":12,
        "CV":45,
        "CN":67,
        "OS":34,
        "UI":45,
        "SW":54,
        "WT":67,
        "CS":24,
        "WS":12
    }

def PredictNextSubject(student_subjects,pred_subjects,debug=False):
    difficulty=getDifficulty()
    difficulty_subjects=[difficulty[sub] for sub in student_subjects if sub!=None]
    difficulty_subjects.append(0)
    maxDifficultyStudent=max(difficulty_subjects) # find the subjects which the student has taken for the field
    #find the next smaller higher difficulty subject
    nextDifficulty=1000
    #highest Diffulty Subject
    nextDifficultySubject=None
    for sub in difficulty.keys():
        diffi=difficulty[sub]
        if( not sub in pred_subjects):
            continue
        if(diffi>maxDifficultyStudent): # check for subject is challenging enough
            if(diffi<nextDifficulty):
                nextDifficulty=diffi
                nextDifficultySubject=sub
    if(debug):
        print("Difficulty of Subjects choosen by student {}".format([[sub, difficulty[sub]] for sub in student_subjects if sub!=None]))
        print("Difficulty of Subjects predicted for student {}".format([[sub, difficulty[sub]] for sub in pred_subjects if sub!=None]))
        print("Next Difficulty : {}  Subject: {}".format(nextDifficulty,nextDifficultySubject))
    return nextDifficultySubject


if __name__ == '__main__':
    Train()
    result=PredictRaw([1,"AI","OS","CN","CV"])
    print("OUTPUT:",result)
    result=PredictRaw([1,"AI",None,None,None])
    print("OUTPUT:",result)
    nextSubject=PredictNextSubject(["SA",None,None],result["S"])
    import pdb
    pdb.set_trace()
