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
lot_id = models.execute_kw(
    db
    , uid
    , password
    , 'dev.rfid.tag.lot.rel', 'search_read'
    , [
        [
            ['tag_id.epc', '=', 'AAA3'],
            ['lot_id.product_id', '=', 40],
            ['status','=',True]
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
prod = models.execute_kw(db, uid, password, 'stock.production.lot','search_read',
                            [[['id', '=', lotid]]],
                            {
                                'fields': ['product_id']
                            }
                        )
print('porduct_id: ',prod)
dumped2 = json.dumps(prod)
loadedd2 = json.loads(dumped2)
prod_id=loadedd2[0]['product_id'][0]
prod_name=loadedd2[0]['product_id'][1]
now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now)

new_stock_picking = models.execute_kw(db, uid, password, 'stock.picking', 'create',
                                      [{'picking_type_id': 85,
                                        'location_id': 84,
                                        'partner_id': 27,
                                        'priority':'',
                                        'location_dest_id': 114}])
print('newly created stock.picking Id is :', new_stock_picking)
