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
from openerp import netsvc
from datetime import datetime

class account_voucher(osv.osv):

    _name = 'account.voucher'
    _inherit = 'account.voucher'
    _description = 'Change the journal_id in Check Model'

    _columns = {
        'issued_check_ids': fields.one2many('account.issued.check','voucher_id', 'Issued Checks', required=False, readonly=True, states={'draft':[('readonly',False)]}),
        'third_check_receipt_ids': fields.one2many('account.third.check','voucher_id', 'Third Checks', required=False,readonly=True, states={'draft':[('readonly',False)]}),
        'third_check_ids': fields.many2many('account.third.check','third_check_voucher_rel', 'third_check_id', 'voucher_id','Third Checks',required=False,readonly=True, states={'draft':[('readonly',False)]}),
        
        'show_check_page': fields.boolean('Show Check Page', ),
        'use_issued_check': fields.boolean('Use Issued Checks', ),
        'use_third_check': fields.boolean('Use Third Checks', ),
    }
    
    _defaults = {
        'show_check_page': False,
        'use_issued_check': False,
        'use_third_check': False,
    }
    

    def _amount_checks(self, cr, uid, voucher_id):
        res = {}
        res['issued_check_amount'] = 0.00
        res['third_check_amount'] = 0.00
        res['third_check_receipt_amount'] = 0.00
        if voucher_id:
            voucher_obj = self.pool.get('account.voucher').browse(cr, uid, voucher_id)
            if voucher_obj.issued_check_ids:
                for issued_check in voucher_obj.issued_check_ids:
                    res['issued_check_amount'] += issued_check.amount
            if voucher_obj.third_check_ids:
                for third_check in voucher_obj.third_check_ids:
                    res['third_check_amount'] += third_check.amount
            if voucher_obj.third_check_receipt_ids:
                for third_rec_check in voucher_obj.third_check_receipt_ids:
                    res['third_check_receipt_amount'] += third_rec_check.amount
        return res  

    def onchange_issued_checks(self, cr, uid, ids, issued_check_ids, third_check_ids, journal_id, partner_id, currency_id,
                               type, date, context=None):
        data = {}
        amount = 0.00
        third_checks = self.pool.get('account.third.check').browse(cr, uid, third_check_ids[0][2])
        for check in third_checks:
            amount += check.amount
        for check in issued_check_ids:
            amount += check[2].get('amount', 0.00)
        data['amount'] = amount
        
        vals = self.onchange_partner_id(cr, uid, ids, partner_id, journal_id, amount, currency_id, type, date)
        data.update(vals.get('value'))
        
        return {'value': data}

    def onchange_third_check_receipt_ids(self, cr, uid, ids,third_check_receipt_ids,
                                        journal_id, partner_id, currency_id, type,date,state, context=None):
                                        
        data = {} 
        if len(ids) < 1:
            data.update({'warning': {'title': _('ATENTION !'), 'message': _('Journal must be fill')}})
                     
        amount = 0.00
        for check in third_check_receipt_ids:
            amount += check[2].get('amount', 0.00)
        data['amount'] = amount
        
        vals = self.onchange_partner_id(cr, uid, ids, partner_id, journal_id,
                amount, currency_id, type, date)
        data.update(vals.get('value'))
        
        return {'value': data}
        

    def onchange_third_check_ids(self, cr, uid, ids, issued_check_ids, third_check_ids, journal_id, partner_id,
                                 currency_id, type, date):
        
        data = {}
        amount = 0.00
        third_checks = self.pool.get('account.third.check').browse(cr, uid, third_check_ids[0][2])
        for check in third_checks:
            amount += check.amount
        for check in issued_check_ids:
            amount += check[2].get('amount', 0.00)
        data['amount'] = amount

        vals = self.onchange_partner_id(cr, uid, ids, partner_id, journal_id, amount, currency_id, type, date)
        data.update(vals.get('value'))

        return {'value': data}
        


    def action_move_line_create(self, cr, uid, ids, context=None):
        voucher_obj = self.pool.get('account.voucher').browse(cr, uid, ids)[0]
        wf_service = netsvc.LocalService('workflow')
        if voucher_obj.type == 'payment':
            if voucher_obj.issued_check_ids:
                for check in voucher_obj.issued_check_ids:
                    check.write({
                        'issued': True,
                        'receiving_partner_id': voucher_obj.partner_id.id,
                    })
                    wf_service.trg_validate(uid, 'account.issued.check',check.id, 'draft_handed', cr)
            else:
                if voucher_obj.third_check_ids:
                    for check in voucher_obj.third_check_ids:

                        check_obj = self.pool.get('account.third.check')
                        result= check_obj.browse(cr,uid,check.id)
                        if result.state != 'holding':
                            raise osv.except_osv(_('State!'), _('The check must be in holding state.'))
                            return False
                        else:
                            check.write({'destiny_partner_id': voucher_obj.partner_id.id,
                                    })
                                    
                            wf_service.trg_validate(uid, 'account.third.check',check.id, 'draft_holding', cr)             
                            wf_service.trg_validate(uid, 'account.third.check',check.id, 'holding_handed', cr)
        elif voucher_obj.type == 'receipt':
            voucher_obj = self.pool.get('account.voucher').browse(cr, uid, ids)[0]
            for check in voucher_obj.third_check_receipt_ids:
                check.write({
                        'source_partner_id': voucher_obj.partner_id.id,
                    })
                wf_service.trg_validate(uid, 'account.third.check', check.id, 'draft_holding', cr)
                
               
        return super(account_voucher, self).action_move_line_create(cr, uid, ids, context=None)
        
    def onchange_journal(self, cr, uid, ids, journal_id, line_ids, tax_id, partner_id, date, amount,
                         ttype, company_id, context=None):
        '''
        Override the onchange_journal function to check which are the page and fields that should be shown
        in the view.
        '''
        ret = super(account_voucher, self).onchange_journal(cr, uid, ids, journal_id, line_ids, tax_id, partner_id,
                                                    date, amount, ttype, company_id, context=context)
        
        if not journal_id:
            return ret
        
        journal_obj = self.pool.get('account.journal')
        journal = journal_obj.browse(cr, uid, journal_id, context=context)
        if isinstance(journal, list):
            journal = journal[0]
        
        if journal.use_issued_check:
            ret['value']['use_issued_check'] = True
        else:
            ret['value']['use_issued_check'] = False
        
        if journal.use_third_check:
            ret['value']['use_third_check'] = True
        else:
            ret['value']['use_third_check'] = False
        
        if ttype in ['sale', 'receipt']:
            if not journal.use_third_check:
                ret['value']['show_check_page'] = False
            else:
                if journal.type == 'bank':
                    ret['value']['show_check_page'] = True
                else:
                    ret['value']['show_check_page'] = False
        
        elif ttype in ['purchase', 'payment']:
            if not journal.use_issued_check and not journal.use_third_check:
                ret['value']['show_check_page'] = False
            else:
                if journal.type == 'bank':
                    ret['value']['show_check_page'] = True
                else:
                    ret['value']['show_check_page'] = False
        
        return ret
        
    def proforma_voucher(self, cr, uid, ids, context=None):
        '''
        Override the proforma_voucher function (called when voucher workflow moves to act_done activity)
        to check, when the associated journal is marked with validate_only_checks, if the total amount is
        the same of the sum of checks.
        '''
        for voucher in self.browse(cr, uid, ids, context=context):
            if voucher.journal_id.validate_only_checks:
                check_amount = 0
                compare_amounts = False
                
                if voucher.type == 'payment':
                    compare_amounts = True
                    for issued_check in voucher.issued_check_ids:
                        check_amount += issued_check.amount
                    for third_check in voucher.third_check_ids:
                        check_amount += third_check.amount
                
                if voucher.type == 'receipt':
                    compare_amounts = True
                    for third_check in voucher.third_check_receipt_ids:
                        check_amount += third_check.amount
                
                voucher_amount = voucher.amount
                
                if compare_amounts and voucher_amount != check_amount:
                    title = _('Cannot Validate Voucher')
                    message = _('The associated journal force that the total amount is the same as the one paid with checks.')
                    raise osv.except_osv(title, message)
        
        return super(account_voucher, self).proforma_voucher(cr, uid, ids, context=context)
                
account_voucher()
