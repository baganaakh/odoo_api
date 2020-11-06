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
prod_name='Sting Gold Sucralose'
now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
new_stock_picking=117
# new_stock_move=785
new_stock_move_line = models.execute_kw(db, uid, password, 'stock.move.line', 'create',
                                        [{
                                            'company_id': 1,
                                            'product_id': prod_id,
                                            'qty_done': 22,
                                            'product_uom_id': 1,
                                            'location_id': 84,
                                            'location_dest_id': 114,
                                            'picking_id': new_stock_picking,
                                            'lot_id': lotid,
                                            # 'move_id':new_stock_move
                                        }])
print('newly created stock.move.line Id is :', new_stock_move_line)