import pandas as pd

def makeDict(col):
    d={}
    num=0
    for cell in col:
        try:
            d[cell]
        except:
            d[cell]=num
            num+=1
    return d


FIDict=None
subjectsDict=None

def getSubjects(data):

    electives=["E1","E2","E3","E4"]
    subjects=set()

    for el in electives:
        subjects_=list(data[el].values)
        subjects=subjects.union(set(subjects_))

    return subjects

def preprocess(data,train=True):
    '''

    :param data: pandas dataframe containing data for preocessiong
    :return: dataframe with all the categoraicl data replaced with its numerical equivalents
    '''
    global FIDict, subjectsDict
    #remove ID
    data.drop(labels=["ID"],axis=1,inplace=True)
    electives=["E1","E2","E3","E4"]
    if(train):
        subjects_list=getSubjects(data)
        subjectsDict=makeDict(subjects_list)

    for el in electives:
        data[el].replace(subjectsDict,inplace=True)

    if(train):
        #find field of interest
        FIDict=makeDict(data["FI"])

    #replace FI by id
    data["FI"].replace(FIDict,inplace=True)

    return data
