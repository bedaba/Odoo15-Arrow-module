{
    'name': 'Arrow Reports',
    'author': 'El-Mahaba Group',
    'website': "https://almahabagroup.com/",
    'description': """Arrow Custom Reports""",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'stock', 'sale' ,'account','account_accountant', 'purchase'],
    
    'data': [
        'security/stock_picking_security.xml',
        
        # Invoice
        # 'reports/report_invoice_without_pricing.xml',
        # 'reports/action_reports.xml',
        # Stock
        # 'reports/report_deliveryslip.xml',
        'reports/stock_picking_report.xml',
        
        # 'views/purchase_order.xml',
        # 'views/account_move.xml',
        # 'views/stock_picking.xml',
    ],
    
}
 
