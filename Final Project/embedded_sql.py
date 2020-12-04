import dbFunctions
import cx_Oracle
import pandas as pd

"""
Some quick start guides:
* cx_Oracle 8: https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
* pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
"""
cx_Oracle.init_oracle_client(lib_dir = "./instantclient_19_8")
dsn = cx_Oracle.makedsn(host='<removed>', port=1521, sid='CSC423')


connection = cx_Oracle.connect(user="<removed for privacy>", password="******", dsn=dsn)
cursor = connection.cursor()
res = -1
data = pd.DataFrame
while (res != 6):
   print("Menu:\n(1) Print Staff Table\n(2) Print Client Table\n(3) Print Vehicle Table\n(4) Print Outlet Table\n(5) Print Hire Agreements\n(6) Exit")
   res = int(input("Please select an option from the menu: "))
   query = []
   if(res == 1):
      cursor.execute("""SELECT * FROM Staff """)
      dbFunctions.printRes(cursor)
   elif(res == 2):
      cursor.execute("""SELECT * FROM Client """)
      dbFunctions.printRes(cursor)
   elif(res == 3):
      cursor.execute("""SELECT * FROM Vehicle """)
      dbFunctions.printRes(cursor)
   elif(res == 4):
      cursor.execute("""SELECT * FROM Outlet """)
      dbFunctions.printRes(cursor)
   elif(res == 6):
      cursor.execute("""SELECT * FROM HireAgreement """)
      dbFunctions.printRes(cursor)
   else:
      break

connection.close()