import xmlrpc.client
import json
from datetime import datetime

url = 'http://localhost:8099'
db = 'db58atest'
username = 'baganaa@alldomain.biz'
password = 'work3939'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
lotid = 2
lotname = '19-8900-0061'

prod_id=40
prod_name='[121005] Sting Gold Sucralose'
now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
new_stock_picking=117
new_stock_move = models.execute_kw(db, uid, password, 'stock.move', 'create',
                                   [{'name': prod_name,
                                     'company_id': 1,
                                     'product_id': prod_id,
                                     'product_uom_qty': 22,
                                     'product_uom': 1,
                                     'location_id': 84,
                                     'location_dest_id': 114,
                                     'picking_id': new_stock_picking,
                                     'picking_type_id': 85
                                     }])
print('newly created stock.move Id is :', new_stock_move)
