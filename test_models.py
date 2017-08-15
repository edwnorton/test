import orm
from models import User, Blog, Comment
import asyncio

async def connecDB(loop):
	username = 'www-data'
	password = '1qaz!QAZ'
	dbname = 'awesome'
	await orm.create_pool(loop,user=username,password=password,db=dbname)
async def destoryDB():
	await orm.destory_pool()
async def test(loop):
	await orm.create_pool(loop, user='www-data', password='1qaz!QAZ', db='awesome')
	u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
	await u.save()
	await destoryDB()
	
async def test_delete(loop):
	await connecDB(loop)
	user = await User.find('001502529538645353e48f753284c5793a251ca290eb420000')
	if user is not None:
		await user.remove()
		print('user remove:%s' % user)
	await destoryDB()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
#loop.run_until_complete(test_delete(loop))
loop.close()
