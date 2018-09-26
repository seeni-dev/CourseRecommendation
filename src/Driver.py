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
    studentRecord=formatStudent(studentRecord)
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

def diffcultyForSubjects(subjects):
    diffculty=getDifficulty()
    return [diffculty[sub] for sub in subjects if sub!=None]

def PredictNextSubject(student_subjects,pred_subjects,debug=False):
    difficulty=getDifficulty()
    difficulty_subjects=diffcultyForSubjects(student_subjects)
    difficulty_subjects.append(0)
    maxDifficultyStudent=max(difficulty_subjects) # find the subjects which the student has taken for the field
    allowableSubjects=[sub for sub in pred_subjects if difficulty[sub] > maxDifficultyStudent]
    allowableSubjects.sort(key=lambda sub: difficulty[sub])
    nextDifficultySubject=allowableSubjects[0]
    nextDifficulty = difficulty[nextDifficultySubject]
    if(debug):
        print("Difficulty of Subjects choosen by student {}".format([[sub, difficulty[sub]] for sub in student_subjects if sub!=None]))
        print("Difficulty of Subjects predicted for student {}".format([[sub, difficulty[sub]] for sub in pred_subjects if sub!=None]))
        print("Next Difficulty : {}  Subject: {}".format(nextDifficulty,nextDifficultySubject))
    if(nextDifficultySubject==None):
        raise Exception("Max difficulty reached");
    return nextDifficultySubject,nextDifficulty,maxDifficultyStudent,allowableSubjects


def formatStudent(stu):
    if(len(stu)<2 ):
        raise Exception("Fields ID and FI are mandatory arguments")
    currentLength=len(stu)
    requiredLength=5
    while currentLength<requiredLength:
        stu.append(None)
        currentLength+=1
    print(stu)
    return stu

def PredictForServer(studentRecord):
    studentRecord=formatStudent(studentRecord)
    result=PredictRaw(studentRecord)
    nextSubject,nextSubjectDifficulty,maxDifficultyStudent,allowableSubjects=PredictNextSubject(studentRecord[2:],result["S"])
    print(nextSubject,nextSubjectDifficulty,maxDifficultyStudent)
    return nextSubject,nextSubjectDifficulty,maxDifficultyStudent

if __name__ == '__main__':
    Train()
    PredictForServer([1,"AI","SA"])
