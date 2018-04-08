import serial
import time
import MySQLdb

arduino = serial.Serial('/dev/ttyUSB0', 9600)

def start():
	time.sleep(1)
	arduino.write('D')
	print "Getting data from Arduino"
	while True:
		# the last bit gets rid of the new-line chars
		temp = arduino.readline()[:-2]
		humi = arduino.readline()[:-2]
		pres = arduino.readline()[:-2]
		global sTemp, sHumi, sPres
		sTemp = str(temp)
		sHumi = str(humi)
		sPres = str(pres)
		print "Data from Arduino DHT22 sensor"
		print "Temp: ", sTemp
		print "Humi: ", sHumi
		print "Pres: ", sPres
		writeToDB()

def writeToFile():
	f = open('cache.txt', 'a')
	f.write(sTemp + '\n')
	f.close()
	print "Done"
	time.sleep(3)

def writeToDB():
	print "Connecting to database"
	conn = MySQLdb.connect(host= "IP",
					user="username",
					passwd="password",
					db="database")
	x = conn.cursor()

	try:
		print "Inserting data to DB"
		x.execute("""INSERT INTO table(temp, humi, pres) VALUES (%s, %s, %s)""" % (sTemp, sHumi, sPres))
		conn.commit()
	except:
		conn.rollback()

	conn.close()
	print "Done"
	time.sleep(1)
	quit()

time.sleep(2)
start()