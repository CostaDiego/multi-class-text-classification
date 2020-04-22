import pandas as pd
from os import getcwd, path

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

DICT_KEYS = ['issues', 'products', 'complaints_users', 'complaints_companies']

def _exportDict(keys = DICT_KEYS, values = _PATHS):
    dictList = []
    for key,path in zip(keys, values):
        dictList.append((key,path))

    return dict(dictList)

def uploadData(tables: dict):

    listDict = []
    for item in list(tables.items()):
        listDict.append((item[0], pd.read_csv(str(item[1]), low_memory=False)))

    tablesDF = dict(listDict)

    connection = DatabaseConection(
        host= input("Input the Host:\t"),
        database= input("Input the Database:\t"),
        user= input("Input the User:\t")
    )

    for key in tablesDF.keys():
        dataframe = tablesDF[key]




if __name__ == '__main__':
    from utils.connection import DatabaseConection
    uploadData(_exportDict())

else:
    from scripts.utils.connection import DatabaseConection