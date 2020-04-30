import pandas as pd
from os import getcwd, path
from utils.utils import queryGenerator

_BASE_DATA_FOLDER = path.normpath(
    path.join(
        getcwd(),
        'data/base'
    )
)

_ISSUES = path.join(_BASE_DATA_FOLDER, 'issues.csv')
_PRODUCTS = path.join(_BASE_DATA_FOLDER, 'products.csv')
_COMPLAINT_USERS = path.join(_BASE_DATA_FOLDER, 'complaints_users.csv')
_COMPLAINT_COMPANIES = path.join(_BASE_DATA_FOLDER, 'complaints_companies.csv')

_PATHS = [_ISSUES, _PRODUCTS, _COMPLAINT_USERS, _COMPLAINT_COMPANIES]

_DICT_KEYS = ['issues', 'products', 'complaints_users', 'complaints_companies']

def _exportDict(keys = _DICT_KEYS, values = _PATHS):
    dictList = []
    for key,path in zip(keys, values):
        dictList.append((key,path))

    return dict(dictList)

def _uploadData(tables: dict):

    listDict = []
    for item in list(tables.items()):
        listDict.append((item[0], pd.read_csv(str(item[1]), low_memory=False)))

    tablesDF = dict(listDict)

    connection = DatabaseConection(
        host= input("Input the Host:\t\t"),
        database= input("Input the Database:\t"),
        user= input("Input the User:\t\t")
    )

    if connection.connected:
        insert = queryGenerator('insert')

        for key in tablesDF.keys():
            dataframe = tablesDF[key]

            #issues
            if key == _DICT_KEYS[0]:
                columns = list(dataframe.columns)

            
            #products
            elif key == _DICT_KEYS[1]:
                columns = list(dataframe.columns)


            #complaints_users
            elif key == _DICT_KEYS[2]:
                columns = list(dataframe.columns)

                for i in range(len(columns)):
                    if str(columns[i]).upper() == 'DATE':
                        columns[i] = 'DATE_COMPLAINT'


            #complaints_companies
            elif key == _DICT_KEYS[3]:
                columns = list(dataframe.columns)

                for i in range(len(columns)):
                    if str(columns[i]).upper() == 'DATE':
                        columns[i] = 'DATE_COMPLAINT'


if __name__ == '__main__':
    from utils.connection import DatabaseConection
    _uploadData(_exportDict())