import RPi.GPIO as GPIO                           #Import GPIO library
import time                                       #Import time library
#import led

class motion:
	sensorStatus = "2"
	def setstatus(self):
		try:
			#self.sensorStatus = str(GPIO.input(self.FlamePin))
			f = open("motion.txt","w")
			f.write(self.sensorStatus)
			#print("Try : ",self.sensorStatus)
			#if self.sensorStatus == "motion1":
			#	f.close()
			#	time.sleep(2)
			#	f = open("trial.txt","w")
			#	f.write(" ")
		except:
			#self.sensorStatus = str(self.sensorStatus())
			f = open("motion.txt","w")
			f.write(self.sensorStatus)
			print("Except : ",self.sensorStatus)
			#if self.sensorStatus == "motion1":
			#	f.close()
			#	time.sleep(2)
			#	f = open("trial.txt","w")
			#	f.write(" ")
		finally:
			f.close()
			
	def __init__(self,pir,red,green):
		GPIO.setmode(GPIO.BOARD)                          #Set GPIO pin numbering
		GPIO.setup(pir, GPIO.IN)                          #Set pin as GPIO IN
		print ("Waiting for sensor to settle")
		time.sleep(0.2)                                     #Waiting for 2 Milli Seconds
		print ("Detecting motion")
		for i in range(0,665):
			print(i)
			if GPIO.input(pir):                            #Check whether pir is HIGH
				print ("Motion Detected!")
				break
			time.sleep(0.1)                                #While loop delay should be less than detection(hardware) delay

#motion(33,3,5)
