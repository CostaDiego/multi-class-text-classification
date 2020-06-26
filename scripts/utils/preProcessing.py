import pandas as pd
import os
import gc

class ColumnClear(object):
    """ Column Clear: A Pre-Processing Class
    Class designed to perform the column clear operation on the '.csv' files
    """
    TARGET_FOLDER = "columnClear"

    def __init__(self, folder, fileFormat = 'csv'):
        self.folder = os.path.normpath(folder)
        self.fileFormat = fileFormat
        # self.targetFolder = os.path.join(
        #     os.path.dirname(self.folder),
        #     targetFolder)
        self._files = []
        self._dataFrames = []

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

    def apply(self, **kwargs):
        dataframes = []

        for filePath, fileName in zip(self._files, self.files):
            fileName = os.path.splitext(fileName)[0]    
            tmpDf = pd.read_csv(filePath)

            tmpDf = self._columnClearMethod(tmpDf, kwargs.get(fileName))
            dataframes.append(tmpDf)
            
            del(tmpDf)
            gc.collect()
        
        self._dataFrames = dataframes

        return self._dataFrames
    
    def _columnClearMethod(self, dataFrame: pd.DataFrame, columns: list):
        dfCleared = dataFrame[columns]

        return dfCleared

