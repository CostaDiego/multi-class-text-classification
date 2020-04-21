import psycopg2
from getpass import getpass

class DatabaseConection(object):
    """
    """

    def __init__(self, host: str, database: str, user: str):
        self._con = None
        self._host = host
        self._database = database
        self._user = user
        self.connected = False

        try:    
            self._con = psycopg2.connect(
                host= self._host,
                database= self._database,
                user= self._user,
                password = getpass(
                    prompt= 'Input the password:\n',
                    stream= None
                ))
            self.connected = True
            print('\tConnection established!')

        except:
            print('\tFailed to establish connection!')

    def send(self, sql: str):
        try:
            cursor = self._con.cursor()
            cursor.execute(str(sql))
            self._con.commit()
            
            return True

        except:
            return False

    def request(self, sql: str):
        try:
            cursor = self._con.cursor()
            cursor.execute(str(sql))
            request = cursor.fetchall()

            return request

        except:
            return None
    
    def closeConnection(self):
        self._con.close()
        self.connected = False

    def connect(self, host = None, database = None, user = None):
        if host:
            self._host = host
        if database:
            self._database = database
        if user:
            self._user = user

        try:
            self._con = psycopg2.connect(
                host= self._host,
                database= self._database,
                user= self._user,
                password = getpass(
                    prompt= 'Input the password:\n',
                    stream= None
                ))
            self.connected = True
            print('\tConnection established!')

        except:
            self.connected = False
            print('\tFailed to establish connection!')