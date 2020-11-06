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
# lots=models.execute_kw(db,uid,password,'dev.rfid.tag.lot.rel','get_lot_id')
# mas = {'AAA1', 'AAA2', 'AAA3', 'AAA4', 'AAA5'}
# tag_id = models.execute_kw(db, uid, password, 'dev.rfid.tag', 'search',
#                            [[['epc', '=', 'AAA2']]])
# print('tag id:', tag_id)
lot_id = models.execute_kw(
    db
    , uid
    , password
    , 'dev.rfid.tag.lot.rel', 'search_read'
    , [
        [
            ['tag_id.epc', '=', 'AAA3'],
            ['lot_id.product_id', '=', 40]
        ]
    ]
    , {
        'fields': {
            'lot_id': {
                'fields': [
                    'id'
                ]
            }
            , 'tag_id': {
                'fields': [
                    'id'
                ]
            }
        }
    }
)

print('lot_id: ', lot_id)
dumped = json.dumps(lot_id)
loadedd = json.loads(dumped)

lotid = loadedd[0]['lot_id'][0]
lotname = loadedd[0]['lot_id'][1]
prod = models.execute_kw(db, uid, password, 'stock.production.lot', 'search_read',
                         [[['id', '=', lotid]]],
                         {
                             'fields': ['product_id']
                         }
                         )
print('porduct_id: ', prod)
dumped2 = json.dumps(prod)
loadedd2 = json.loads(dumped2)
prod_id = loadedd2[0]['product_id'][0]
prod_name = loadedd2[0]['product_id'][1]
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now)
new_stock_picking = models.execute_kw(db, uid, password, 'stock.picking', 'create',
                                      [{'picking_type_id': 85,
                                        'state': 'draft',
                                        'location_id': 84,
                                        'location_dest_id': 114}])
print('newly created stock.picking Id is :', new_stock_picking)
new_stock_move = models.execute_kw(db, uid, password, 'stock.move', 'create',
                                   [{'name': prod_name,
                                     'company_id': 1,
                                     'product_id': prod_id,
                                     'product_uom_qty': 33,
                                     # 'product_qty': 33,
                                     'product_uom': 1,
                                     'location_id': 84,
                                     'location_dest_id': 114,
                                     'picking_id': new_stock_picking,
                                     'description_picking': prod_name,
                                     'state': 'draft',
                                     'picking_type_id': 85,
                                     'procure_method': 'make_to_stock'
                                     }])
print('newly created stock.move Id is :', new_stock_move)
# new_stock_move2 = models.execute_kw(db, uid, password, 'stock.move', 'create',
#                                    [{'name': 'Pepsi Acidulant',
#                                      'company_id': 1,
#                                      'product_id': 2,
#                                      'product_uom_qty': 22,
#                                      'product_uom': 1,
#                                      'location_id': 84,
#                                      'location_dest_id': 114,
#                                      'picking_id': new_stock_picking,
#                                      'state': 'draft',
#                                      'picking_type_id': 85
#                                      }])
# print('newly created stock.move Id2 is :', new_stock_move2)
# new_stock_move3 = models.execute_kw(db, uid, password, 'stock.move', 'create',
#                                    [{'name': 'Pepsi Acidulant',
#                                      'company_id': 1,
#                                      'product_id': 2,
#                                      'product_uom_qty': 22,
#                                      'product_uom': 1,
#                                      'location_id': 84,
#                                      'location_dest_id': 114,
#                                      'picking_id': new_stock_picking,
#                                      'state': 'draft',
#                                      'picking_type_id': 85
#                                      }])
# print('newly created stock.move Id2 is :', new_stock_move3)
#
new_stock_move_line = models.execute_kw(db, uid, password, 'stock.move.line', 'create',
                                        [{
                                            'company_id': 1,
                                            'product_id': prod_id,
                                            'qty_done': 33,
                                            'product_uom_id': 1,
                                            'location_id': 84,
                                            'location_dest_id': 114,
                                            'picking_id': new_stock_picking,
                                            'state': 'draft',
                                            'move_id': new_stock_move,
                                            'lot_id': lotid,
                                            # 'lot_name': lotname
                                        }])
print('newly created stock.move.line Id is :', new_stock_move_line)
# new_stock_move_line2 = models.execute_kw(db, uid, password, 'stock.move.line', 'create',
#                                         [{
#                                             'company_id': 1,
#                                             'product_id': 40,
#                                             'product_uom_qty': 22,
#                                             'product_uom_id': 1,
#                                             'location_id': 84,
#                                             'location_dest_id': 114,
#                                             'picking_id': new_stock_picking,
#                                             'state': 'draft',
#                                             'lot_id': lotid,
#                                             'lot_name': lotname
#                                         }])
# print('newly created stock.move.line Id2 is :', new_stock_move_line2)
# new_stock_move_line3 = models.execute_kw(db, uid, password, 'stock.move.line', 'create',
#                                         [{
#                                             'company_id': 1,
#                                             'product_id': 40,
#                                             'product_uom_qty': 22,
#                                             'product_uom_id': 1,
#                                             'location_id': 84,
#                                             'location_dest_id': 114,
#                                             'picking_id': new_stock_picking,
#                                             'state': 'draft',
#                                             'lot_id': lotid,
#                                             'lot_name': lotname
#                                         }])
# print('newly created stock.move.line Id3 is :', new_stock_move_line3)
