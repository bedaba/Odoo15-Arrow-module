# -*- coding: utf-8 -*-

##############################################################################
#
#
#    Copyright (C) 2019-TODAY .
#    Author: Eng.Ramadan Khalil (<rkhalil1990@gmail.com>)
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
##############################################################################


import logging

LOGGER = logging.getLogger(__name__)

from odoo import http
from odoo.http import request
import werkzeug
import json
from datetime import date, datetime

_logger = logging.getLogger(__name__)
import requests
import dateutil.parser
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.service import db, security



class PlementusAuthentication(http.Controller):
    """Entitlement Authentication Web Controller"""

    @http.route('/pl_auth/', type='http', auth='public',
                methods=['GET'])
    def pl_authenticate(self, token, user, project):
        auth_validate_url = request.env['ir.config_parameter'].sudo().get_param(
            'pl_auth.pl_auth_validate_url')
        if not token or not auth_validate_url:
            return werkzeug.utils.redirect('/web/login')
        project_id = int(project)
        user_id = request.env['res.users'].sudo().search(
            [('login', '=', user)])
        if not user_id:
            return werkzeug.utils.redirect('/web/login')
        data = {
            'token': token,
            'date': datetime.now().strftime(DEFAULT_SERVER_DATETIME_FORMAT),
            'project_id': project_id,

        }
        headers = {
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        }
        response = requests.post(auth_validate_url, data=json.dumps(data),
                                 headers=headers)
        response_json = response.json()
        if response_json.get('result') and response_json['result'].get(
                'state') == 'success':
            request.uid = user_id.id
            request.session.uid = user_id.id
            request.session.login = user
            # request.session.db = 'ahl-masr-live'
            request.session.session_token = security \
                .compute_session_token(request.session,
                                       http.request.env)
            # _logger.info('session:::', request.session)
            http.request.session.get_context()
            return werkzeug.utils.redirect('/web')
        else:
            return werkzeug.utils.redirect('/web/login')
