
import os
from motionClass import motion
import time


class run():
	def __init__(self):
		while True:
			os.system('sudo python cam.py')
			os.system('python3 -m scripts.label_image \
    			--graph=tf_files/retrained_graph.pb  \
    			--image=tf_files/flower_photos/pro.png')
			motion(33,13,14)
			time.sleep(4)

#l = ['pro']
#for i in l:
run()

