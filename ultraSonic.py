import RPi.GPIO as GPIO
import time

class ultraSonic:
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)

	def operation(self,TRIG,ECHO):
		print("Distance Measurement In Progress")
		GPIO.setup(TRIG,GPIO.OUT)
		GPIO.setup(ECHO,GPIO.IN)
		GPIO.output(TRIG, False)
		#print("Waiting For Sensor To Settle")
		#time.sleep(0.5)
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
		while GPIO.input(ECHO)==0:
		  pass
		pulse_start = time.time()
		#print(pulse_start)
		while GPIO.input(ECHO)==1:
		  pass
		pulse_end = time.time()
		#print(pulse_end)
		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17000
		#distance = round(distance, 2)
		if (int(distance)<10):
			print("Distance: "+str(distance)+"cm")
		GPIO.cleanup()

while True:
	print("Sensor 2")
	ultraSonic().operation(16,18)
	time.sleep(0.5)
	print("Sensor 1")
	ultraSonic().operation(38,40)
	time.sleep(0.5)
