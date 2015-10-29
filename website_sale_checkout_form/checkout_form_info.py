from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request
from openerp.addons.website_sale.controllers.main import get_pricelist
from openerp.tools.translate import _
from openerp import models, fields, api, _

class event_type(models.Model):
    _inherit = "event.type"
    
    link = fields.Char(string="URL")
    
class sale_order(models.Model):
    _inherit = "sale.order"
    
    driver_name = fields.Char(string = "Driver Name")
    parent_name = fields.Char(string = "Parent Name")
    birth_date = fields.Char(string = "Birth Date")
    length = fields.Char(string = "Length")
    other_info = fields.Char(string = "Other Info")
    
class event_registration(models.Model):
    _inherit = "event.registration"
    
    driver_name = fields.Char(string = "Driver Name")
    parent_name = fields.Char(string = "Parent Name")
    birth_date = fields.Char(string = "Birth Date")
    length = fields.Char(string = "Length")
    other_info = fields.Char(string = "Other Info")


class website_gokart_form(http.Controller):

    @http.route(['/gokart/<model("event.event"):event>/register'], type='http', auth="public", website=True)
    def gokart_event(self, event, **post):
        pricelist_id = int(get_pricelist())
        values = {
            'event': event.with_context(pricelist=pricelist_id),
            'main_object': event.with_context(pricelist=pricelist_id),
            'range': range,
        }
        return request.render('website_event.event_description_full', values)

    #~ @http.route(['/gokartserie/<model("event.event"):event>/register'], type='http', auth="public", website=True)
    #~ def gokartserie_event_register(self, event, **post):
        #~ pricelist_id = int(get_pricelist())
        #~ values = {
            #~ 'event': event.with_context(pricelist=pricelist_id),
            #~ 'main_object': event.with_context(pricelist=pricelist_id),
            #~ 'range': range,
        #~ }
        #~ return request.website.render("website_gokart_form.checkout_form_info", values)
