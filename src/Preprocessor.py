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

def getSubjectsRaw(data):
    '''
    :param data: data consisting of tuples (FI,E1,E2,E3...EN)
    :return: set of subjects in data
    '''
    subjects=set()
    for row in data:
        subjects=subjects.union(row[1:])
    return subjects

def sortSubjects(data):
    '''

    :param data: data consisting of tuples (FI,E1,E2,E3...EN)
    :return :similar data consisting of tuples (FI,E1,E2,E3...EN) with subjects sorted for each row
    '''
    data_sort=[]
    for rowi in data:
        row=list(rowi)

        subjects=row[1:]
        subjects.sort()
        for si in range(len(subjects)):
            subject=subjects[si]
            row[1+si]=subject
        data_sort.append(row)
    return data_sort

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
    data.drop("ID",axis=1,inplace=True)
    subjects=getSubjectsPd(data)
    fieldOfInterest=getFIPd(data)
    data_n=pd.DataFrame()
    #make cateogical values
    for fi in fieldOfInterest:
        col="FI_"+fi
        values=[]
        for fientry in data["FI"].values:
            values.append(1 if fientry==fi else 0)
        data_n[col]=values

    for sub in subjects:
        subcol="S_"+sub
        values=[]
        for subjects in data.drop("FI",axis=1).values:
            values.append(1 if sub in subjects else 0)
        data_n[subcol]=values
    return data_n

def getRevereseDict(d):
    return dict(zip(
        d.values(),d.keys())
    )


def getStringSubjects(nums):
    global  subjectsDict
    reverseSubjectsDict=getRevereseDict(subjectsDict)
    if(not type(nums)==list):
        return reverseSubjectsDict[nums]
    else:
        return [  reverseSubjectsDict[num] for num in nums ]


def getStringFI(fi):
    global FIDict
    FIReverseDict=getRevereseDict(FIDict)
    fi = list(fi)
    return [ FIReverseDict[fi_] for fi_ in fi ]
