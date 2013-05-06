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
{
    'name' : 'Treasury', 
    'version' : '2.1',
    'author':   'OpenERP - Team de Localización Argentina',
    'category': 'Localization/Argentina',
    'website':  'https://launchpad.net/~openerp-l10n-ar-localization',
    'license':  'AGPL-3',
    'description' : '''
Modulo básico de cartera.

La funcionalidad es sencilla, y en este momento tiene como objetivo el llevar un registro de los documentos de tesorería (cheques, contado, transferencias, ...).

Este módulo es útil para la gestión de cartera (cobros y pagos), desde el momento que se recibe el documento hasta que se cobra / paga.

El módulo de tesorería está vinculado a los bancos y a los partners. Uno puede visualizar el estado de los diversos documentos desde el menú de gestión financiera o directamente desde la ficha del partner en sí.

    ''',
    'depends' : ['base','account','account_payment'],
    'init_xml' : [],
    'demo_xml' : [],
    'update_xml' : [
        'data/treasury_view.xml',
        'data/voucher_view.xml',
        'security/treasury_security.xml',
    ],
    'active': False 
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
