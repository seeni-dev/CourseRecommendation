import pandas as pd


subjects=[]
fieldOfInterests=[]

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

def getSubjectsRaw(data):
    '''
    :param data: data consisting of tuples (FI,E1,E2,E3...EN)
    :return: set of subjects in data
    '''
    subjects=set()
    for row in data:
        subjects=subjects.union(row[1:])
    return subjects


def toRaw(data_pd):
    '''

    :param data_pd: pandas dataframe
    :return: data in raw list format
    '''
    data=data_pd.to_records(index=False)
    data_list=[]
    for d in data:
        data_list.append(list(d))
    return data_list


def getSubjectsPd(data):
    '''
    :param data: pandas Dataframe consisting of tuples (FI,E1...EN)
    :return: list of subjects
    '''
    data_r=toRaw(data)
    subjects=getSubjectsRaw(data_r)
    return subjects

def getFIPd(data):
    """

    :param data: pandas dataframe
    :return: list of FI

    """
    fieldOfInterest=set([fi for fi in data["FI"].values])
    return list(fieldOfInterest)

def preprocess(data,train=True):
    '''

    :param data: pandas dataframe containing data for preocessiong
    :return: dataframe with all the categorical data as separate dimension
    '''
    global subjects,fieldOfInterests
    data.drop("ID",axis=1,inplace=True)
    if(train):
        subjects=getSubjectsPd(data)
        fieldOfInterests=getFIPd(data)

    data_n=pd.DataFrame()
    #make cateogical values
    for fi in fieldOfInterests:
        col="FI_"+fi
        values=[0]*len(data)
        for fientry_i in range(len(data["FI"].values)):
            fientry=data["FI"].values[fientry_i]
            if(fientry==fi):
                values[fientry_i]=1
        data_n[col]=values

    for sub in subjects:
        subcol="S_"+sub
        values=[0]*len(data)
        for subject_i in range(len(data.drop("FI",axis=1).values)):
            subject=data.drop("FI",axis=1).values[subject_i]
            if(sub in subject):
                values[subject_i]=1
        data_n[subcol]=values
    return data_n

def getRevereseDict(d):
    return dict(zip(
        d.values(),d.keys())
    )

