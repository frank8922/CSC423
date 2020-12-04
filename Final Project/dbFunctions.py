import pandas as pd

def insertData(values,cursor):
    cursor = cursor
    table = values[0]
    col = values[1]
    if len(values) < 3:
        cursor.execute("""INSERT INTO :table(:col)
                   VALUES(:values) """,values)
    else:
        optClause = values[2]
        cursor.execute("""INSERT INTO :table(:col)
                   VALUES(:values) WHERE :optClause""",values)

def selectData(values,cursor):
    cursor = cursor
    print(len(values))
    if len(values) < 3:
        cursor.execute("""SELECT :col FROM :table """,col=input("col:"),table=input("table"))
    else:
        optClause = values[2]
        cursor.execute("""SELECT :col FROM :table WHERE :optClause""",values)

def updateData(values,cursor):
    table = values[0]
    col = values[1]
    cursor = cursor
    if len(values) < 3:
        cursor.execute("""UPDATE :table SET :col """,table,col)
    else:
        optClause = values[2]
        cursor.execute("""UPDATE :table SET :col WHERE :optClause""",values)

def deleteData(values,cursor):
    table = values[0]
    col = values[1]
    cursor = cursor
    if len(values) < 3:
        print("ERROR: What should I delete?")
    else:
        optClause = values[2]
        cursor.execute("""DELETE FROM: table WHERE :optClause""",values)

def getInput(query):
    query.append(input("Enter table: "))
    query.append(input("Enter columns: "))
    query.append(input("Enter optional clauses"))
    if not query[2]:
        del query[-1] 
    return query

def printRes(cursor):
    columns = [c[0] for c in cursor.description]
    # fetch data
    data = cursor.fetchall()
    # bring data into a pandas dataframe for easy data transformation
    df = pd.DataFrame(data, columns = columns)
    print(df) # examine
    print(df.columns)

