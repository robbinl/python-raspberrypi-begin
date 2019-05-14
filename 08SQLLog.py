# 2019 Robbin Law
import time
import datetime
import sqlite3 as sql
from sense_hat import SenseHat

dbname = 'SensorsData.db'
samplefreq = 1 # time in seconds

def getData():
    hat = SenseHat()
    temp = hat.get_temperature()
    hum = hat.get_humidity()
    if temp is not None:
        temp = round(temp, 2)
    if hum is not None: 
        hum = round(hum, 2)   
    return temp, hum

def logData (temp, hum):
    conn=sql.connect(dbname)
    curs=conn.cursor()
    dt = datetime.datetime.now()
    curs.execute("INSERT INTO {tn} VALUES (DATETIME('now'), {f2}, {f3})" .format(tn="HatData", f2=temp, f3=hum))
    conn.commit()
    conn.close()

def main():
    while True:
        try:
            temp, hum = getData()
            logData (temp, hum)
            time.sleep(samplefreq)
        except KeyboardInterrupt as ki:
            print("Caught:", repr(ki))
            print("Exiting.")
            break

main()

