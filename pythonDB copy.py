import pymysql
import csv

conn, cur = None, None
data1, data2, data3, data4 = "","","",""
#sql = ""

print("------------------------------------")
#sql = "insert into ROOM_INFO (ROOM_NO, CO2_DNSTY) values (%s, %f)"
sql = ""
f = open('test.csv', 'r', encoding='utf-8')
rd = csv.reader(f)


conn = pymysql.connect(host='127.0.0.1', user='root', password='1234',db='room_data', charset='utf8')
cur = conn.cursor()


for line in rd:
    print(rd)
    sql = "INSERT INTO ROOM_INFO (ROOM_NO, CO2_DNSTY) VALUES('" + line[0] + "','" + line[1] + "')"
    cur.execute(sql)
    #cur.execute(sql, (line[0], float(line[1])))

# while(True):
#     data1 = input("ㅁ 사용자ID : ")
#     if data1 == "" :
#         break
    
#     data2 = input("ㅁ 사용자명 : ")
#     data3 = input("ㅁ 사용자주소 : ")
#     sql = "INSERT INTO membertbl VALUES('" + data1 + "','" + data2 + "','" + data3 + "')"
#     cur.execute(sql)

conn.commit()
conn.close()
f.close()
print("ㅁㅁㅁㅁㅁㅁ완료ㅁㅁㅁㅁㅁㅁㅁ")