# 2019 Robbin Law
import time
import sqlite3 as sql

dbname = 'SensorsData.db'
samplefreq = 5 # time in seconds

def main():
    while True:
        try:
            count=0
            conn=sql.connect(dbname)
            curs=conn.cursor()
            tableName = "HatData"
            curs.execute("SELECT * FROM {tn} ORDER BY {ts} DESC".format(tn=tableName, ts="timestamp"))
            rows=curs.fetchall()
            print ("\nAll Records in the Database in Descending Order:")
            for row in rows:
                print ("TimeStamp = "+str(row[0])+" ==> Temp = "+str(row[1])+"	Hum ="+str(row[2]))
                count=count+1
            conn.close()
            print("\nNumber of Records in Database is "+str(count))
            conn=sql.connect(dbname)
            curs=conn.cursor()
            numRecords = "10"
            curs.execute("SELECT * FROM {tn} ORDER BY {ts} DESC LIMIT {lt}".format(tn="HatData", ts="timestamp", lt=numRecords))
            rows=curs.fetchall()
            print ("\nLast 10 Records in the Database in Descending Order:")
            for row in rows:
                print ("TimeStamp = "+str(row[0])+" ==> Temp = "+str(row[1])+"	Hum ="+str(row[2]))
            conn.close()
            conn=sql.connect(dbname)
            curs=conn.cursor()
            numRecords = "1"
            curs.execute("SELECT * FROM {tn} ORDER BY {ts} DESC LIMIT {lt}".format(tn="HatData", ts="timestamp", lt=numRecords))
            rows=curs.fetchall()
            print ("\nLast Record in the Database:")
            for row in rows:
                print ("TimeStamp = "+str(row[0])+" ==> Temp = "+str(row[1])+"	Hum ="+str(row[2]))
            conn.close() 
            time.sleep(samplefreq)
        except KeyboardInterrupt as ki:
            print("Caught:", repr(ki))
            print("Exiting.")
            break
main()


