# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2012 OpenERP - Team de Localización Argentina.
# https://launchpad.net/~openerp-l10n-ar-localization
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields
from openerp.tools.translate import _
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class account_issued_check(osv.osv):

    def _get_checkbook_id(self, cr, uid, context=None):
        res={}
        if context is None: 
            context = {}
        checkbook_pool = self.pool.get('account.checkbook')

        res = checkbook_pool.search(cr, uid, [('state', '=', 'active')],)
        if res:
            return res[0] 
        else:
            return False

                
    _name = 'account.issued.check'
    _inherit = 'account.issued.check'
    _description = 'Add checkbook ' 
    _columns = {
                'checkbook_id': fields.many2one('account.checkbook','Checkbook',readonly=True,required=True,states={'draft': [('readonly', False)]}),
                }
                
    _defaults = {
        'checkbook_id': _get_checkbook_id,            
                }

                    
    def create(self, cr, uid, vals, context={}):
        order_obj= self.pool.get('account.voucher')

        if not order_obj.browse(cr, uid, context.get('active_ids', []), context=context):
            raise osv.except_osv(_('Error !'), _('The Check must be create on one payment !'))
            return res
        
        
        checkbook_obj = self.pool.get('account.checkbook')       
        num = vals['checkbook_id'] 
        book = checkbook_obj.browse(cr, uid, num, context=context)
        
        actual=0
        hasta=0
        actual= int(book.actual_number)
        hasta= int(book.range_hasta)
        if actual == hasta:
            checkbook_obj.write(cr, uid, num, {'state': 'used',})  
        else:
            if str(book.actual_number) < str(book.range_hasta):
                sum_actual_number = int(book.actual_number) + 1
                checkbook_obj.write(cr, uid, num, {'actual_number': str(sum_actual_number),
                                              }) 
        
        vals['account_bank_id'] = book.account_bank_id.id
        res = super(account_issued_check, self).create(cr, uid, vals, context)            
        return res
         
    def onchange_checkbook_id(self, cr, uid, ids, number, checkbook_id, context=None):
        result = {}
        checkbook_obj = self.pool.get('account.checkbook')
        if checkbook_id:

            res = checkbook_obj.browse(cr, uid, checkbook_id, context=context)
                                           
            #Busca la chequera activa de acuerdo a la cuenta                                    
            if not res.id:
                result = {'value':{'checkbook_id': None}}
                result = {'value':{'number': None}}
                result.update({'warning': {'title': _('Error !'), 'message': _('You must be create a checkbook or change state')}})
                return result
            
            if res.state != 'active':
                result = {'value':{'checkbook_id': 0}}
                result.update({'warning': {'title': _('Error !'), 'message': _('The Checkbook is not active')}})
            else:
                result = {'value':{'number': str(res.actual_number)}}
                                                             
        return result 
        

        
account_issued_check()
