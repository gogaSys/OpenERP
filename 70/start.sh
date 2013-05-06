#!/bin/bash
cd /home/dante/Escritorio/openerp70/OpenErp-dev/70
chmod +x openerp-server

python openerp-server --addons-path="/home/dante/Escritorio/openerp70/OpenErp-dev/70/openerp/addons,/home/dante/Escritorio/openerp70/OpenErp-dev/locale" --db_host=localhost --db_user=openerp70 --db_password=openerp70 --db_port=5432 --xmlrpc-port=8269 --netrpc-port=8270
