# AI-and-IOT-based-Baby-Monitoring-System

⦁ Introduction
In today’s world, parents are coming across infant injuries that are happening every now and then. This is because of lack of parent’s attention on their infants.The most common cause of infant injury is falls, which account for more than 50% of all seriously injured children. Beds are linked to the most injuries up to age of 16 months, mostly because infants fall, roll, or slide off them. 

The main objective of this project is to provide a system to monitor the baby continuously and send alert notification to parents and care takers. The parents will get an alert when baby comes close to the edges of bed as well as if any insects or pets comes close to baby.

⦁	Methodology
The information regarding baby sleep is collected using camera. Camera is attached to the baby’s bed which detects baby face to know that baby is in the bed or not. The picture taken by the camera is send to the TensorFlow api for analysis. The data collected is stored in csv file which is later used for prediction using machine learning algorithms. If baby is not visible to camera then ultrasonic sensor gets activated and it measures the distance between baby and bed boundary. If distance is less alert is sent to parents using email.  A report is sent to parents about sleep pattern of baby via email once in a day.

⦁ Hardware Specifications
  Processor	1.4 GHz 64-bit Quad-Core Processor
  Memory	1 GB RAM
  Hard Disk	Minimum 32 GB
  Devices	Raspberry Pi 3 B+, Camera, Ultrasonic Sensor, LED Bulb, Motion Sensor, Temperature Sensor, Servo Motor, Jumper Wire, Mobile/Desktop Device

⦁ Software Specifications
  Operating System	Raspbian 7
  Image Analysis Tool	TensorFlow for Poets
  Language	Python3
  Adafruit Sensors Library

