import requests
import json
import urllib3
import logging

from odoo import http,models, fields
from odoo.http import request
 
# Configure the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DandyApi(models.AbstractModel):
    _inherit = "pos.order"

    def action_pos_order_paid(self):
            logger.info('model start successful#########################################################################')
            super(DandyApi, self).action_pos_order_paid()

            DandyApi.get_invoices(self)

    def get_invoices(self):
        logger.info('model start successful**********************++++++++++++++++++++++++++****************************')
        pos_order_objs = self.env['pos.order'].sudo().search([ ('employee_id', '=', 'Arab mall'), ('x_studio_invoice_sent', '=', False)])
        token=""

        if pos_order_objs:
            invoice_data = []
           
                # invoice_data.append(vals)

            # The first part to get the token
            url = 'https://rsmsapi.marakez.net/webservice/RestApi/Users/Login'
            api_key = 'Ya2bMAprxRUSDS041Py498maQk99ADs4'
            username = 'Encopedia'
            password = 'Encopedia@2021'

            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-API-Key': api_key,
            }

            frm_data = {
                'userName': 'moa@rsmsapi.marakez.net',
                'password': 'Moa@2023@encopedia',
            }

            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            try:
                # Get the token
                response = requests.post(url, headers=headers, auth=(username, password), data=frm_data, verify=False)
                response.raise_for_status()
                res = response.json()
                token = res['result']['token']
                logger.info('Token: %s', token)
                logger.info(api_key)
                # token='719b3e272993f083e389c16e6a3e82bdc22380f5a8539d874d1b332f3de7aacf'
                transactions_data = {
                        "store_id": "eb449b2c302492b72c3868654e363246a11f401c661cd337758e65dfd26f65e1",
                        "invoice_no": "Inv-11-01-2023-01",
                        "invoice_date": "2023-01-01 16:50:00:000",
                        "subtotal": "25.00",
                        "tax": "00.00",
                        "service": "00.00",
                        "total": "00.00",
                        "discount": "0"
                    }
                # Send the data
                url2 = 'https://rsmsapi.marakez.net/webservice/RestApi/Transactions/Record/'
                headers2 = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-API-Key': api_key,
                    'X-TOKEN': token,
                }

                for pos_order_obj in pos_order_objs:
                    subs = pos_order_obj.amount_total - pos_order_obj.amount_tax
                    logger.info('invoice_no: %s', pos_order_obj.name)
                    logger.info('invoice_date: %s', str(pos_order_obj.date_order))
                    logger.info('subtotal: %s', subs)
                    logger.info('tax: %s', pos_order_obj.amount_tax)
                    logger.info('total: %s', pos_order_obj.amount_total)
                    vals = {
                        "store_id": "eb449b2c302492b72c3868654e363246a11f401c661cd337758e65dfd26f65e1",
                        "invoice_no": pos_order_obj.name,
                        "invoice_date": str(pos_order_obj.date_order),
                        "subtotal": subs,
                        "tax": pos_order_obj.amount_tax,
                        "service": "00.00",
                        "total": pos_order_obj.amount_total,
                        "discount": "0"
                }
                    response2 = requests.post(url2, headers=headers2, auth=(username, password), json=vals, verify=False)
                    response2.raise_for_status()
                    logger.info('POST request successful: %s', response2.json())
                     # Mark the invoice as sent
                    pos_order_obj.x_studio_invoice_sent = True
                    
            except requests.exceptions.HTTPError as http_err:
                logger.error('HTTP error occurred: %s', http_err)
            except requests.exceptions.RequestException as req_err:
                logger.error('Request error occurred: %s', req_err)
            except json.JSONDecodeError as json_err:
                logger.error('JSON decoding error occurred: %s', json_err)
            except Exception as err:
                logger.error('An error occurred: %s', err)

        else:
            data = {
                'status': 404,
                'message': 'No invoices found for the specified POS sessions.',
                'invoices': [],
            }
            return json.dumps(data, indent=4)
