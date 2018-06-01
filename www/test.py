import orm
from models import User, Blog, Comment
import asyncio
@asyncio.coroutine
def test():
	yield from orm.create_pool(loop=loop,user='root', password='', db='awesome',port=3306,host='127.0.0.1')

	u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank',id='110')

	yield from u.save()

loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test())

#关闭EventLoop
loop.close()

'sql check code'
import mysql.connector

conn=mysql.connector.connect(user='root', password='', database='awesome')
cursor=conn.cursor()
cursor.execute('select * from users')
data=cursor.fetchall()
print(data)