import pandas

class Handler():

    def __init__(self):
        pass

    def connect(self):
        raise Exception("Need to be implemented")

    def open(self):
        raise Exception("Need to be implemented")

    def read(self):
        raise Exception("Need to be implemented")

    def getData(self):
        raise Exception("Need to be implemented")

    def getId(self):
        raise Exception("Need to be implemented")


class CSVHandler(Handler):
    """
        Class for CSV Handler which reads CSV files and handles data that is read
    """
    def __init__(self, filepath="input.csv"):
        """
        Initializes the handler for reading inputs from csv
        :param filepath: location to the input file
        :return:
        """

        super().__init__()
        self.filepath=filepath
        self.data = pandas.read_csv(self.filepath)
        return


    def getData(self):
        """

        :return: pandas dataframe for the data read from the csv file
        """
        return self.data
