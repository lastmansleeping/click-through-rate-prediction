## Use it as: python convert.py > train.vw
from datetime import datetime
import csv
import re
start = datetime.now()
i = 0
Loc1 = r"../../Data/test.csv"
Loc2 = r"../../Data/test.vw"
trainfile= open(Loc1, "r")
j = open(Loc2, 'wb')
csv_reader=csv.reader(trainfile)
linenum=0
for row in csv_reader:
    linenum +=1
    # If not header
    if linenum > 1:
        vw_line = ""
        vw_line += "1 |fe"
        dtime_numb=row[1]
        year  = dtime_numb[0:2]
        month = dtime_numb[2:4]
        day   = dtime_numb[4:6]
        hour  = dtime_numb[6:9]
        yeartime = " day:" + day +" hour:" + hour
        vw_line += yeartime
        vw_line += " |pos"
        vw_line += str(" c1_")+str(row[2])
        vw_line += str(" banner_pos_")+str(row[3])
        vw_line += " |site"
        vw_line += str(" site_id_")+str(row[4])
        vw_line += str(" site_domain_")+str(row[5])
        vw_line += str(" site_category_")+str(row[6])
        vw_line += " |app"
        vw_line += str(" app_id_")+str(row[7])
        vw_line += str(" app_domain_")+str(row[8])
        vw_line += str(" app_category_")+str(row[9])
        vw_line += " |device"
        vw_line += str(" device_id_")+str(row[10])
        vw_line += str(" device_ip_")+str(row[11])
        vw_line += str(" device_model_")+str(row[12])
        vw_line += str(" device_type_")+str(row[13])
        vw_line += str(" device_conn_type_")+str(row[14])
        vw_line += " |others"
        vw_line += str(" c14_")+str(row[15])
        vw_line += str(" c15_")+str(row[16])
        vw_line += str(" c16_")+str(row[17])
        vw_line += str(" c17_")+str(row[18])
        vw_line += str(" c18_")+str(row[19])
        vw_line += str(" c19_")+str(row[20])
        vw_line += str(" c20_")+str(row[21])
        vw_line += str(" c21_")+str(row[22]) + "\n"
        #print (vw_line)
        j.write(vw_line)
        if linenum % 1000000 == 0:
                print("%s\t%s"%(linenum, str(datetime.now() - start)))


print("\nTask execution time:\n\t%s"%(str(datetime.now() - start)))