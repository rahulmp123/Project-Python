#############################################################################
# Python program to query oracle database for SQL performance and SPACE analysis
############################################################################


# import necessary packages to make this program work
import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt

# Connect to Oracle 18c pluggable database XEPDB1  and query data in SQLID_ANALYSIS toracle able.
# Note: Analysis data is already stored here in table so this simple program only fetch and display desired results from table.

con=cx_Oracle.connect("ptest","Winterland2020","DESKTOP-7D5AK1B.home/XEPDB1")
sql1="select to_char(begin_interval_time,'DD-MON-YYYY HH24:MI:SS') as begin_interval_time , avg_etime as runtime from sqlid_analysis"
sql2="select to_char(begin_interval_time,'DD-MON-YYYY HH24:MI:SS') as begin_interval_time , avg_lio as LogicalIO from sqlid_analysis"



cursor=con.cursor()

dfl1=pd.read_sql_query(sql1,con)
dfl2=pd.read_sql_query(sql2,con)


#Print SQL output on python screen for both oracle queries for user to take a look at data.
   
print(dfl1)
print(dfl2)

cursor.close()
con.close()

# Generate graph of sql analysis based on user input in form IF-ELIF-ELSE block

user_input=input("Do we need runtime or logical IO performance?     ")
if user_input == "runtime":
    print("Let's show runtime graph over a established period")
    dfl1.plot(kind='line',x='BEGIN_INTERVAL_TIME',y='RUNTIME',color='red',title='SQL analysis1')
    plt.show()
elif user_input ==  "logical IO":
    print("Let's show logical IO graph over a established period")
    dfl2.plot(kind='line',x='BEGIN_INTERVAL_TIME',y='LOGICALIO',color='green',title='SQL analysis2')
    plt.show()
else:
    print("User did not specify input correctly")

print("SQL Analysis done")

# Space Analysis

print("Begining Space Analysis")

con=cx_Oracle.connect("ptest","Winterland2020","DESKTOP-7D5AK1B.home/XEPDB1")
sql3="select tablespace_name,sum(bytes)/(1024*1024) as size_in_MB from dba_data_files group by tablespace_name"
cursor=con.cursor()
dfl3=pd.read_sql_query(sql3,con)
print(dfl3)

cursor.close()
con.close()

print("Lets' look at space within database")
dfl3.plot(kind='bar',x='TABLESPACE_NAME',y='SIZE_IN_MB', color='blue',title='Space Analysis')
plt.show()

print("Space Analysis done")




   
