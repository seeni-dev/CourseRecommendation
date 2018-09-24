import pandas as pd


subjects=[]  #list of subjects in the database
fieldOfInterests=[] #list of Field of interest FI in the database


def getSubjectsPd(data):
    '''
    :param data: pandas Dataframe consisting of tuples (FI,E1...EN)
    :return: set of subjects
    '''

    subjects=data.drop("FI",axis=1).values
    subjects.resize(subjects.size)
    subjects=set(subjects)
    return subjects

def getSubjects():
    """

    :return: set of subjects that are made from train data
    """
    return subjects

def getFI():
    """

    :return: set of field of interest(FI) made from the train data
    """
    return fieldOfInterests

def getFIPd(data):
    """

    :param data: pandas dataframe with schema (FI,E1,E2,E3...)
    :return: set of FI

    """
    fieldOfInterest=set(data["FI"].values)
    return set(fieldOfInterest)

def preprocess(data,train=True):
    '''

    :param data: pandas dataframe containing data for preprocessing
    :return: dataframe with all the categorical data as separate dimension for each subject and for each FieldOfIntereset FI
    '''
    global subjects,fieldOfInterests
    data.drop("ID",axis=1,inplace=True)
    if(train):
        subjects=getSubjectsPd(data)
        fieldOfInterests=getFIPd(data)

    data_n=pd.DataFrame() #new dataframe
    #make each  dimension for each value of fi
    for fi in fieldOfInterests:
        col="FI_"+fi
        values=[0]*len(data)
        for fientry_i in range(len(data["FI"].values)):
            fientry=data["FI"].values[fientry_i]
            if(fientry==fi):
                values[fientry_i]=1
        data_n[col]=values

    #make dimension for each subject possible
    for sub in subjects:
        subcol="S_"+sub
        values=[0]*len(data)
        for subject_i in range(len(data.drop("FI",axis=1).values)):
            subject=data.drop("FI",axis=1).values[subject_i]
            if(sub in subject):
                values[subject_i]=1
        data_n[subcol]=values
    return data_n
