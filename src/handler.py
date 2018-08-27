import pandas

class Handler():

    def __init__(self):
        pass

    def connect(self):
        pass

    def open(self):
        pass

    def read(self):
        pass

    def getData(self):
        pass

    def getId(self):
        pass


class CSVHandler(Handler):
    def __init__(self,filepath="input.csv"):
        '''
        Initializes the handler for reading inputs from csv and the stream
        :param filepath: location to the input file
        '''

        self.filepath=filepath

        return

    def open(self):
        '''

        :return: it  opens the file
        '''
        self.df=pandas.read_csv(self.filepath)

    def getData(self):
        '''

        :return: python dataframe for the data in the csv file
        '''
        return  self.df

