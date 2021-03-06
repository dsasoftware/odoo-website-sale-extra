# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)


class res_partner(models.Model):
    _inherit = "res.partner"

    def name_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if context.get('show_short_address_only'):
            if isinstance(ids, (int, long)):
                ids = [ids]
            return [(r.id,'%s,%s' % (r.street,r.city)) for r in self.browse(cr, uid, ids, context=context)]
        else:
            return super(res_partner, self).name_get(cr, uid, ids, context=context)


                                #~ <field name="partner_invoice_id" groups="sale.group_delivery_invoice_address" context="{'default_type':'invoice'}"/>
                            #~ <field name="partner_shipping_id" on_change="onchange_delivery_id(company_id, partner_id, partner_shipping_id, fiscal_position)" groups="sale.group_delivery_invoice_address" context="{'default_type':'delivery'}"/>

