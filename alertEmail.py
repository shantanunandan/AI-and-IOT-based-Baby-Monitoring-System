import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
class email:
	def emailSend(self,name,path,temp,motion,fire):
		fromaddr = "From Email Address"
		toaddr = "To Email Address" 
		msg = MIMEMultipart()
 
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Subject Of Email"
 
		body = "Body Of Email"
		
		msg.attach(MIMEText(body, 'plain'))

		filename = name
		path = path
		attachment = open(path , "rb")
 
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
		msg.attach(part)
 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "From Email Password")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		print("Mail Send")

#email().emailSend("baby.png","/home/pi/Desktop/project/SC/tf_files/flower_photos/pro.png",'temp','life','fire')

