import pymysql

conn, cur = None, None
data1, data2, data3, data4 = "","","",""
sql = ""

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234',db='shopdb', charset='utf8')
cur = conn.cursor()

while(True):
    data1 = input("ㅁ 사용자ID : ")
    if data1 == "" :
        break
    
    data2 = input("ㅁ 사용자명 : ")
    data3 = input("ㅁ 사용자주소 : ")
    sql = "INSERT INTO membertbl VALUES('" + data1 + "','" + data2 + "','" + data3 + "')"
    cur.execute(sql)

conn.commit()
conn.close()