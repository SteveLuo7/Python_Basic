import hashlib

import pymysql

username = input('Please input username:')
password = input('Please input password:')
h = hashlib.md5()
h.update(password.encode('utf8'))
password = h.hexdigest()
print(password)



db = pymysql.connect(host='localhost',
                     user='root',
                     password='Luo-010495',
                     database='python201',
                     port=3306,
                     charset='utf8')

cursor = db.cursor()
sql = 'select * from user where name=%s and password=%s' % (username,password)
cursor.execute(sql)
cursor.close()
db.commit()
db.close()


print(cursor.fetchone())
