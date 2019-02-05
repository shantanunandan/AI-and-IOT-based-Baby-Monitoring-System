import csv
import datetime

time = datetime.datetime.now()
d = str(time.date())
t = str(time.time())

def csvWrite(csvFileName,n,l,r,f,nf):
    """Writes the given data row-wise to the given csv file."""
    with open(csvFileName, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([d,t,n,l,r,f,nf])

#        writer.writerow(["    Date    ","  Time  "," Normal Sleep "," Left Sleep "," Right Sleep "," Face Down "," Not In Bed "])

#csvWrite("babyMovents.csv")
