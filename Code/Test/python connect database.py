import pymysql

#   打开一个数据库连接
db = pymysql.connect(host='localhost', user='root', password='Luo-010495', database='python201', port=3306, charset='utf8')





#   关闭数据库连接
db.close()