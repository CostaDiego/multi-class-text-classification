import pandas as pd
import os
import gc

class PreProcess(object):
    """ Pre-Processing Class
    Class designed to perform all preprocessing operation on the '.csv' files
    """

    _OPERATION = ['COLUMN_CLEAR']

    def __init__(self, folder, fileFormat = 'csv', operation = None):
        self.folder = folder
        self.fileFormat = fileFormat
        self._files = []
        self._dataFrames = []

        if operation and operation in self.__class__._OPERATION:
            self.operation = self._getOperation(operation)

        else:
            self.operation = operation

        for file in os.listdir(self.folder):
            file = os.path.join(self.folder, file)

            if os.path.isfile(file) and file.lower().endswith('.' + self.fileFormat):
                self._files.append(file)
        

    @property
    def files(self):
        files = []
        for file in self._files:
            files.append(os.path.split(file)[1])
        
        return files

    def setOperation(self, operation):
        self._getOperation(operation)            

    def apply(self, **kwargs):
        dataframes = []

        for filePath, fileName in zip(self._files, self.files):
            fileName = os.path.splitext(fileName)[0]    
            tmpDf = pd.read_csv(filePath)

            tmpDf = self.operation(tmpDf, kwargs.get(fileName))
            dataframes.append(tmpDf)
            
            del(tmpDf)
            gc.collect()
        
        self._dataFrames = dataframes

        return self._dataFrames



    def _getOperation(self, operation):
        # COLUMN_CLEAR Option
        if operation.upper() == self.__class__._OPERATION[0]:
            return self.columnClearMethod
    
    def columnClearMethod(self, dataFrame: pd.DataFrame, columns: list):
        dfCleared = dataFrame[columns]

        return dfCleared