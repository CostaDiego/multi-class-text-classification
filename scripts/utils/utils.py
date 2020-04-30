

def queryGenerator(mode: str):
    mode = mode.upper()

    def insertQuery(table: str, **kwargs):
        tableQuery = table.lower()
        columns = kwargs.get('columns')
        values = kwargs.get('values')
        
        if columns:
            columnsQuery = "("

            for i in range(len(columns)):
                columnsQuery += str(columns[i]).lower()
                
                if i < len(columns) - 1:
                    columnsQuery += ", "
            
            columnsQuery += ")"

        else:
            columnsQuery = None

        if values:
            valuesQuery = "("

            for i in range(len(values)):
                # valuesQuery += "'"
                valuesQuery += str(values[i])
                # valuesQuery += "'"

                if i < len(values) - 1:
                    valuesQuery += ", "
            
            valuesQuery += ")"

        if columnsQuery:
            query = "INSERT INTO {tbl} {clm} VALUES {vle};".format(
                tbl = tableQuery, clm = columnsQuery, vle = valuesQuery)
        else:
            query = "INSERT INTO {tbl} VALUES {vle};".format(
                tbl = tableQuery, vle = valuesQuery)

        return query

    if mode == 'INSERT':
        return insertQuery
