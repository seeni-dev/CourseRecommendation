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
        subjects_list=getSubjectsPd(data)
        subjectsDict=makeDict(subjects_list)

    for el in electives:
        data[el].replace(subjectsDict,inplace=True)

    if(train):
        #find field of interest
        FIDict=makeDict(data["FI"])


    #replace FI by id
    data["FI"].replace(FIDict,inplace=True)
    features=data.columns
    data=toRaw(data)
    data=sortSubjects(data)
    data=pd.DataFrame(data)
    data.columns=features
    return data

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
