import xmlrpc.client
import json

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
            ['tag_id.epc', '=', 'AAA2']
        ]
    ]
    , {
        'fields': [
            'lot_id'
            ,'tag_id'
        ]
    }
)

print('lot_id: ', lot_id)
dumped = json.dumps(lot_id)
loadedd = json.loads(dumped)

lotid=loadedd[0]['lot_id'][0]
lotname=loadedd[0]['lot_id'][1]

new_stock_picking = models.execute_kw(db, uid, password, 'stock.picking', 'create',
                                      [{'picking_type_id': 85, 'state': 'draft',
                                        'move_type': 'direct', 'location_id': 84,
                                        'location_dest_id': 114}])
print('newly created stock.picking Id is :', new_stock_picking)
new_stock_move = models.execute_kw(db, uid, password, 'stock.move', 'create',
                                   [{'name': 'Pepsi Acidulant',
                                     'company_id': 1,
                                     'product_id': 2,
                                     'product_uom_qty': 22,
                                     'product_uom': 1,
                                     'location_id': 84,
                                     'location_dest_id': 114,
                                     'picking_id': new_stock_picking,
                                     'state': 'draft',
                                     'picking_type_id': 85
                                     }])
print('newly created stock.move Id is :', new_stock_move)
new_stock_move_line = models.execute_kw(db, uid, password, 'stock.move.line', 'create',
                                        [{
                                            'company_id': 1,
                                            'product_id': 40,
                                            'product_uom_qty': 22,
                                            'product_uom_id': 1,
                                            'location_id': 84,
                                            'location_dest_id': 114,
                                            'picking_id': new_stock_picking,
                                            'state': 'draft',
                                            'lot_id': lotid,
                                            'lot_name': lotname
                                        }])
print('newly created stock.move.line Id is :', new_stock_move_line)
