import pymysql

username = input('Please input username:')
pwd = input('Password please')

# 创建连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='db6',
    port=3306,
    charset='utf8'
)
# 创建游标
cur = conn.cursor()
sql = 'insert into tb1(id,name,pwd) values(2,%s,%s)'
print(sql)
res = cur.execute(sql,[username,pwd])
# 游标关闭、连接关闭

# 增  删  改  一定要commit（）
conn.commit()
cur.close()
conn.close()

if res:
    print('Login successful')
else:
    print('Login failed')

# Bill"-- uiabdug
#     auysdvuysdv"  or 1=1 -- uibdfuibf