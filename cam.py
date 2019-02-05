import os
import time
#import buzzer

class cam:
	def __init__(self):
		cmd = 'fswebcam --no-banner -S 20 -q -r 640x480 /home/pi/Desktop/project/SC/tf_files/flower_photos/pro.png'
		for i in range(0,2):
			try:
				time.sleep(1)
				os.system(cmd)
			except:
				time.sleep(1)
				os.system(cmd)

cam()
exit(0)
#time.sleep(2)
