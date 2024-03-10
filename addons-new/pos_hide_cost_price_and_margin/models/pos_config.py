from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    iface_display_margin = fields.Boolean(string='Display Margin', default=False)
