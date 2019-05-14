# 2019 Robbin Law
import sqlite3 as sql
from sqlite3 import Error

def createDataBase(dbName):
    try:
        print("Creating DataBase file if not already in this directory")
        con = sql.connect(dbName)
    except Error as e:
        print(e)
    finally:
        con.close()

def createTable(dbName, tbName):
    try:
        print("Creating DataBase table or clearing if exists")
        con = sql.connect(dbName)
        cur = con.cursor() 
        cur.execute("DROP TABLE IF EXISTS {tn}".format(tn=tbName))
        cur.execute("CREATE TABLE {tn} ({nf1} {ft1}, {nf2} {ft2}, {nf3} {ft3})"\
            .format(tn=tbName, nf1="timestamp", ft1="TEXT", nf2="temp", ft2="NUMERIC", nf3="hum", ft3="NUMERIC"))
        #cur.execute("CREATE TABLE HatData(timestamp DATETIME, temp NUMERIC, hum NUMERIC)")
    except Error as e:
        print(e)
    finally:
        con.close()

def main():
    dbName = "SensorsData.db"
    tbName = "HatData"
    createDataBase(dbName)
    createTable(dbName, tbName)

main()

