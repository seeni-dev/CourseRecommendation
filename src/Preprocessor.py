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

def preprocess(data):
    '''

    :param data: pandas dataframe containing data for preocessiong
    :return: dataframe with all the categoraicl data replaced with its numerical equivalents
    '''
    print(data.columns)
    import pdb
    pdb.set_trace()
    data.get
