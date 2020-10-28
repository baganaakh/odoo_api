import xmlrpc.client

url = 'http://localhost:8099'
db = 'db58atest'
username = 'baganaa@alldomain.biz'
password = 'work3939'

# info=xmlrpc.client.ServerProxy('http://localhost:8099/').start()
# url,db,username,password=\
#     [url],[db],[username],[password]

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
# print("Details...",version)

uid = common.authenticate(db, username, password, {})
print('UID', uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# partner_ids = models.execute_kw(db, uid, password, 'res.partner', 'search',
#                              [[]]
#                              # [[['customer', '=', True]]]
#                              # , {'offset': 10, 'limit': 2}
#                              )
# print('partners...', partner_ids)
#
# partners_count=models.execute_kw(db, uid,password,'res.partner','search_count',[[]])
# print('partners count....', partners_count)
#
# partner_rec=models.execute_kw(db,uid,password,'res.partner','read',[partner_ids],
#                               {'fields':['id','name']})
# print('partner_rec ....',partner_rec)

mas={'AAA1','AAA2','AAA3','AAA4','AAA5'}

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

new_stock_move2 = models.execute_kw(db, uid, password, 'stock.move', 'create',
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
print('newly created stock.move Id 2 is :', new_stock_move2)
new_stock_move3 = models.execute_kw(db, uid, password, 'stock.move', 'create',
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
print('newly created stock.move Id 3 is :', new_stock_move3)

new_stock_move_line = models.execute_kw(db, uid, password, 'stock.move.line', 'create',
                                   [{
                                     'company_id': 1,
                                     'product_id': 2,
                                     'product_uom_qty': 22,
                                     'product_uom_id': 1,
                                     'location_id': 84,
                                     'location_dest_id': 114,
                                     'picking_id': new_stock_picking,
                                     'state': 'draft',
                                     }])
print('newly created stock.move.line Id is :', new_stock_move_line)

new_stock_move_line2 = models.execute_kw(db, uid, password, 'stock.move.line', 'create',
                                   [{
                                     'company_id': 1,
                                     'product_id': 2,
                                     'product_uom_qty': 22,
                                     'product_uom_id': 1,
                                     'location_id': 84,
                                     'location_dest_id': 114,
                                     'picking_id': new_stock_picking,
                                     'state': 'draft',
                                     }])
print('newly created stock.move.line Id 2 is :', new_stock_move_line2)

new_stock_move_line3 = models.execute_kw(db, uid, password, 'stock.move.line', 'create',
                                   [{
                                     'company_id': 1,
                                     'product_id': 2,
                                     'product_uom_qty': 22,
                                     'product_uom_id': 1,
                                     'location_id': 84,
                                     'location_dest_id': 114,
                                     'picking_id': new_stock_picking,
                                     'state': 'draft',
                                     }])
print('newly created stock.move.line Id 2 is :', new_stock_move_line3)
