import pymysql
import csv

conn, cur = None, None
sql = ""
f1 = open('room_info.csv', 'r', encoding='utf-8')
rd = csv.reader(f1)

f2 = open('sensor_data.csv', 'r', encoding='utf-8')
rd2 = csv.reader(f2)

print("------------------------------------")

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234',db='room_data', charset='utf8')
cur = conn.cursor()


for line in rd:
    print(rd)
    sql = "INSERT INTO ROOM_INFO (ROOM_NO, LAST_MESURE_DT, CO2_DNSTY, INDOOR_HD, LIGHT_IN, PIR_SENSOR, INDOOR_TP) VALUES('" + line[0] + "','" + line[1] + "','" + line[2] + "','" + line[3] + "','" + line[4] + "','" + line[5] + "','" + line[6] + "')"
    cur.execute(sql)

for line in rd2:
    sql = "INSERT INTO ROOM_INFO (ROOM_NO, LAST_MESURE_DT, CO2_DNSTY, INDOOR_HD, LIGHT_IN, PIR_SENSOR, INDOOR_TP) VALUES('" + line[0] + "','" + line[1] + "','" + line[2] + "','" + line[3] + "','" + line[4] + "','" + line[5] + "','" + line[6] + "')"
    cur.execute(sql)    

conn.commit()
conn.close()
f1.close()
f2.close()
print("ㅁㅁㅁㅁㅁㅁ완료ㅁㅁㅁㅁㅁㅁㅁ")