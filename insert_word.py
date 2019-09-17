'''

'''
import pymysql
import re
f = open('dict.txt')

db = pymysql.connect(
    user = 'root',
    password = '123456',
    database = 'stu',
    charset  = 'utf8'
)
cur = db.cursor()
sql = "insert into words(word,mean) values(%s,%s);"

for line in f:
    # tmp = line.split(' ',1)
    # word = tmp[0]
    # mean = tmp[1].strip()
    # cur.execute(sql,[word,mean])
    tup = re.findall(r'(\S+)\s+(.*)',line)[0]
    cur.execute(sql,tup)
try:
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()