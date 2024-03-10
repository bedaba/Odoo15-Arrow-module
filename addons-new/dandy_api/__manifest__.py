# -*- coding: utf-8 -*-
{
    'name': "Dandy API",

    'summary': """
        Get data from odoo invoices""",

    'description': """
        Long description of module's purpose
    """,

    'author': "El-Mahaba Group",
    'website': "https://almahabagroup.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'installable': True,
    'application': True,
    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        # Other data files for views, security, etc.
        # 'data/scheduled_action_data.xml',  # Add this line to include the data file
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
