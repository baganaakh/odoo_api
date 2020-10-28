import xmlrpc.client

url = 'http://localhost:8099'
db = 'db58atest'
username = 'baganaa@alldomain.biz'
password = 'work3939'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

mas = {'AAA1', 'AAA2', 'AAA3', 'AAA4', 'AAA5'}
# for datas in mas:
# tag_id = models.execute_kw(db, uid, password, 'dev.rfid.tag', 'search',
#                            [[['epc', '=', 'AAA1']]])
# print('tag id:', tag_id)
# lot_id = models.execute_kw(db, uid, password, 'dev.rfid.tag.lot.rel', 'search',
#                            [[['tag_id', '=', tag_id]]])
# print('lotid: ', lot_id)
lot = models.execute_kw(db, uid, password, 'dev.rfid.tag.lot.rel',
                        'read', [1], {'fields': ['lot']})
print('lot: ', lot)
