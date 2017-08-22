import orm
from models import User, Blog, Comment
import asyncio

async def connecDB(loop):
    username = 'www'
    password = 'Www123456!'
    dbname = 'awesome'
    await orm.create_pool(loop,user=username,password=password,db=dbname)
async def destoryDB():
    await orm.destory_pool()
async def test_insert(loop):
    await orm.create_pool(loop, user='www', password='Www123456!', db='awesome')
    u = User(name='bb', email='bb@example.com', passwd='1234567890', image='about:blank')
    await u.save()
    await destoryDB()

async def test_findAll(loop):
    await connecDB(loop)
    users = await User.findAll()
    for user in users:
        print('user:%s' % user)
    await destoryDB()

async def test_findAll_t(loop):
    await connecDB(loop)
    users = await User.findAll_t()
    for user in users:
        print('user:%s' % user)
    await destoryDB()

async def test_find(loop):
    await connecDB(loop)
    user = await User.find('001503048923603070f16deb0fc465b877b11036f74e150000')
    print('user:%s' % user)
    await destoryDB()
	
async def test_delete(loop):
    await connecDB(loop)
    users = await User.findAll()
    print('find users:%s' % users)
    if users is not None:
        for user in users:
            await user.remove()
            print('user remove:%s' % user)
    await destoryDB()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    #loop.run_until_complete(test_insert(loop))
    #loop.run_until_complete(test_find(loop))
    loop.run_until_complete(test_findAll_t(loop))
    #loop.run_until_complete(test_findAll(loop))
    loop.run_until_complete(test_delete(loop))
    loop.close()
