import pandas as pd
import numpy as np

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


def sortElectives(data):
    electives=["E1","E2","E3","E4"]
    import pdb
    for i in range(len(data)):
        subjects=list(data[i:(i+1)][electives])
        subjects.sort()
        for el,sub in zip(electives,subjects):
            data[i:(i+1)][el]=sub
    pdb.set_trace()


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
    sortElectives(data)
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
