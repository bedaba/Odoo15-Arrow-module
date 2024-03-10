# -*- coding: utf-8 -*-

# Copyright © 2018 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'Restriction of POS User',
    'version': '15.0.1.0.1',
    'category': 'Point of Sale',
    'author': 'ALMAHABA GROUP',
    'website': 'https://github.com/bedaba',
    'summary': 'Only allowed points of sale for POS users',
    'images': ['static/description/banner.png'],
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'security/pos_user_restrict_security.xml',
        'views/res_users_views.xml',
    ],
    'demo': [
        'demo/point_of_sale_demo.xml',
        'demo/res_users_demo.xml',
    ],
    'external_dependencies': {
    },
    'support': 'bedaba15@gmail.com',
    'application': False,
    'installable': True,
    'auto_install': False,
}
