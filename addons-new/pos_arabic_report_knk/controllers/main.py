import requests
import json
import urllib3
import logging
from odoo import models, fields ,http
from odoo.http import request

# Configure the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PosOrder(models.Model):
    _inherit = 'pos.order'

    @classmethod
    def get_eta_uuids(cls):
        eta_uuids = cls.sudo().search([('state', '=', 'invoiced'), ('employee_id', '=', 'Arab mall')])
        logger.info('model start successful**************************************************************************' + eta_uuids)
        return eta_uuids

# class PosMirrorController(http.Controller):

#     @http.route('/get_eta_uuid', type='http', auth="public", website=True, sitemap=False)
#     def get_eta_uuid(self):
#         eta_uuids = request.env['pos.order'].get_eta_uuids()
#         return json.dumps(eta_uuids.read(), indent=4)
