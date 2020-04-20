import psycopg2
from getpass import getpass

class DatabaseConection(object):
    """
    """

    def __init__(self, host:str, database, user):
        try:    
            self._con = psycopg2.connect(
                host= host,
                database= database,
                user=user,
                password = getpass(
                    prompt= 'Input the password:\n',
                    stream= None
                ))
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