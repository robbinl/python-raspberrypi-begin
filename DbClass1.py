# 2019 Robbin Law
try:
    import sqlite3 as sql
    from sqlite3 import Error
    print("sqlite3 IS loaded on this machine")
except:
	print("sqlite3 ISNOT loaded on this machine")

import time
import datetime

class DataBaseClass():
    def __init__(self):
        try:
            print("Instantiating DataBaseClass")
        except:
            print("Unable to Instantiate DataBaseClass")
	
    def createDataBase(self, dbName):
        try:
            print("Creating DataBase file if not already in this directory")
            con = sql.connect(dbName)
        except Error as e:
            print(e)
        finally:
            con.close()

    def createTable(self, dbName, tbName):
        try:
            print("Creating DataBase table or clearing if exists")
            con = sql.connect(dbName)
            cur = con.cursor() 
            cur.execute("DROP TABLE IF EXISTS {tn}".format(tn=tbName))
            cur.execute("CREATE TABLE {tn} ({nf1} {ft1}, {nf2} {ft2}, {nf3} {ft3})"\
                .format(tn=tbName, nf1="timestamp", ft1="TEXT", nf2="temp", ft2="NUMERIC", nf3="hum", ft3="NUMERIC"))
        except Error as e:
            print(e)
        finally:
            con.close()

    def logData (self, dbName, tbName, temp, hum):
        try:
            print("Logging Data into Table")
            con = sql.connect(dbName)
            curs = con.cursor()
            curs.execute("INSERT INTO {tn} VALUES (DATETIME('now'), {f2}, {f3})".format(tn=tbName, f2=temp, f3=hum))
            con.commit()
        except Error as e:
            print(e)
            print("logData error")
        finally:
            con.close()

    def retrieveData (self, dbName, tbName, numRecords):
        try:
            print("Retrieving Data from Table")
            con = sql.connect(dbName)
            curs = con.cursor()
            curs.execute("SELECT * FROM {tn} ORDER BY {ts} DESC LIMIT {lt}".format(tn=tbName, ts="timestamp", lt=numRecords))
            rows = curs.fetchall()
            return rows
        except Error as e:
            print(e)
        finally:
            con.close()
            

