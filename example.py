
import xmlrpc.client
import base64
import io



username    = 'demo'        # the user
password    = 'work3939'    # the password of the user
# db          = 'dbtestdemo'  # the database
db          = 'dbtestdemo'  # the database
# url         = "http://0.0.0.0:8069"                     # Localhost
# url         = "http://localhost:8069"                   # Localhost
url         = "http://19.server.alldomain.biz:8069"    # Server



common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
uid = common.authenticate(db, username, password, {})
# print("Uid",uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

limit = 23
lists = models.execute_kw(
   db
   , uid
   , password
   , 'hr.employee'
   , 'search_read'
   , [
       [

       ]
   ]
   , {
       'fields': [
           'id'
           , 'name'
           , 'image_1920'
       ]
       , 'order': 'id desc'
       # , 'limit': limit
   }
)

for index, employee in enumerate( lists ):
   print(' index = "', index, '"', ' lists[', index, ']["image_1920"] = "',
         lists[index]["image_1920"], '"')