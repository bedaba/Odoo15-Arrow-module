# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).
import requests
import json
import urllib3
import logging
from odoo import models, fields ,http
from odoo.http import request

# Configure the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ResCompany(models.Model):
    _inherit = "res.company"

    company_footer = fields.Char('Footer')
    company_heading_1 = fields.Char('Heading Line 1')
    company_heading_2 = fields.Char('Heading Line 2')
    company_heading_3 = fields.Char('Heading Line 3')
    company_heading_4 = fields.Char('Heading Line 4')
    arabic_name = fields.Char('Arabic Name')


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    arabic_translate = fields.Char('Arabic Translate')



# class PosMirrorController(http.Controller):

#     @http.route('/get_eta_uuid', type='http', auth="public", website=True, sitemap=False)
#     def get_eta_uuid(self):
#         eta_uuids = request.env['pos.order'].search([('pos_reference', '=', 'Order 02177-001-0023'), ('eta_submit_state', '=', 'sent'), ('eta_status', '=', 'valid')], order='date_order desc')
#         if eta_uuids:
#             for eta_uuids in eta_uuids:
#              invoice_data = []

#                 # invoice_data.append(vals)


#             vals =  eta_uuids.eta_uuid
#             invoice_data.append(vals)


#         data = vals
          
#         logger.info( data )
#         return json.dumps(data, indent=4).strip('"')
        
class PosMirrorController(http.Controller):

    @http.route('/get_eta_uuid', type='http', auth="public", website=True, sitemap=False)
    def get_eta_uuid(self, **kwargs):
        order_reference = kwargs.get('order_reference', '')  # Get the order reference from the request

        eta_uuids = request.env['pos.order'].search([('pos_reference', '=', order_reference), ('eta_submit_state', '=', 'sent'), ('eta_status', '=', 'valid')], order='date_order desc')
        invoice_data = []
        for eta_uuid in eta_uuids:
            invoice_data.append(eta_uuid.eta_uuid)

        data = invoice_data
          
        logger.info(data)
        return json.dumps(data, indent=4).strip('"')