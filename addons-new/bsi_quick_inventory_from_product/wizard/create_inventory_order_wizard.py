# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2023-today Botspot Infoware Pvt. Ltd. <www.botspotinfoware.com>
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
#################################################################################
from odoo import api, fields, models


class CreateInventoryOrderWizard(models.TransientModel):
    _name = "create.inventory.order.wizard"
    _description = "CreateInventoryOrderWizard"

    partner_id = fields.Many2one('res.partner', string="Customer")
    scheduled_date = fields.Datetime(string="Quotation Date")
    user_id = fields.Many2one(
        'res.users', string="Salesperson", default=lambda self: self.env.user)
    payment_term_id = fields.Many2one(
        'account.payment.term', string="Payment Terms")
    move_ids_without_package = fields.One2many(
        'create.inventory.order.line.wizard', 'order_id', string="inventory Order Line")
    location_dest_id = fields.Many2one(
        "stock.location", string="Destination Location")
    location_id = fields.Many2one("stock.location", string="Source Location")
    picking_type_id = fields.Many2one(
        "stock.picking.type", string="Operation Type")

    def create_order(self):
        current_model = self.env.context.get('active_model')
        active_id = self.env[current_model].browse(
            self.env.context.get('active_id'))

        move_line_vals = []
        for lines in self.move_ids_without_package:
            line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.description, 'location_id': lines.location_id.id, 'location_dest_id': lines.location_dest_id.id,
                    'product_uom': lines.product_uom, 'product_uom_qty': lines.product_uom_qty, 'reserved_availability': lines.reserved_availability, 'quantity_done': lines.quantity_done})
            move_line_vals.append(line)
        inventory = {'partner_id': self.partner_id.id, 'location_id': self.location_id.id, 'location_dest_id': self.location_dest_id.id,
                     'picking_type_id': self.picking_type_id.id, 'scheduled_date': self.scheduled_date, 'move_ids_without_package': move_line_vals}
        inventory_ids = self.env['stock.picking'].create(inventory)

    def create_view_inventory_order(self):
        current_model = self.env.context.get('active_model')
        active_id = self.env[current_model].browse(
            self.env.context.get('active_id'))

        move_line_vals = []
        for lines in self.move_ids_without_package:
            line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.description, 'location_id': lines.location_id.id, 'location_dest_id': lines.location_dest_id.id,
                    'product_uom': lines.product_uom, 'product_uom_qty': lines.product_uom_qty, 'reserved_availability': lines.reserved_availability, 'quantity_done': lines.quantity_done})
            move_line_vals.append(line)
        inventory = {'partner_id': self.partner_id.id, 'location_id': self.location_id.id, 'location_dest_id': self.location_dest_id.id,
                     'picking_type_id': self.picking_type_id.id, 'scheduled_date': self.scheduled_date, 'move_ids_without_package': move_line_vals}
        inventory_ids = self.env['stock.picking'].create(inventory)
        ir_model_data = self.env['ir.model.data']
        view_id = ir_model_data._xmlid_lookup('stock.view_picking_form')[2]
        record_id = self.env['stock.picking'].search(
            [('partner_id', '=', self.partner_id.id)])
        return {
            'view_mode': 'form',
            'view_type': 'form',
            'views': [(view_id, 'form')],
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'res_model': 'stock.picking',
            'res_id': inventory_ids.id
        }

    def create_new_order(self):
        ir_model_data = self.env['ir.model.data']
        view_id = ir_model_data._xmlid_lookup(
            'bsi_quick_inventory_from_product.create_inventory_order_wizard')[2]

        move_line_vals = []
        for lines in self.move_ids_without_package:
            line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.description, 'location_id': lines.location_id.id, 'location_dest_id': lines.location_dest_id.id,
                    'product_uom': lines.product_uom, 'product_uom_qty': lines.product_uom_qty, 'reserved_availability': lines.reserved_availability, 'quantity_done': lines.quantity_done})
            move_line_vals.append(line)
        inventory = {'partner_id': self.partner_id.id, 'location_id': self.location_id.id, 'location_dest_id': self.location_dest_id.id,
                     'picking_type_id': self.picking_type_id.id, 'scheduled_date': self.scheduled_date, 'move_ids_without_package': move_line_vals}
        inventory_ids = self.env['stock.picking'].create(inventory)
        self.partner_id = False
        self.scheduled_date = False
        self.payment_term_id = False
        return {
            'name': 'Create Transfers/inventory Order',
            'view_mode': 'form',
            'view_type': 'form',
            'views': [(False, 'form')],
            'type': 'ir.actions.act_window',
            'res_model': 'create.inventory.order.wizard',
            'res_id': self.id,
            'target': 'new'
        }

    def create_and_confirm(self):
        current_model = self.env.context.get('active_model')
        active_id = self.env[current_model].browse(
            self.env.context.get('active_id'))

        move_line_vals = []
        for lines in self.move_ids_without_package:
            line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.description, 'location_id': lines.location_id.id, 'location_dest_id': lines.location_dest_id.id,
                    'product_uom': lines.product_uom, 'product_uom_qty': lines.product_uom_qty, 'reserved_availability': lines.reserved_availability, 'quantity_done': lines.quantity_done})
            move_line_vals.append(line)
        inventory = {'partner_id': self.partner_id.id, 'location_id': self.location_id.id, 'location_dest_id': self.location_dest_id.id,
                     'picking_type_id': self.picking_type_id.id, 'scheduled_date': self.scheduled_date, 'move_ids_without_package': move_line_vals}
        inventory_ids = self.env['stock.picking'].create(
            inventory).action_confirm()

    @api.model
    def default_get(self, fields):
        selected_ids = self.env.context.get('active_ids', [()])
        product = self.env['product.product'].search([])
        selected_records = self.env['create.inventory.order.wizard'].browse(
            selected_ids)
        res = super(CreateInventoryOrderWizard, self).default_get(fields)
        move_ids_without_package = [(5, 0, 0)]
        for pro in selected_ids:
            product_id = self.env['product.product'].browse(pro)
            line = (0, 0, {
                'product_id': product_id.id,
                'product_uom_qty': 1,
                'unit_price': product_id.lst_price,
            })
            move_ids_without_package.append(line)
        res.update({'move_ids_without_package': move_ids_without_package})
        return res


class CreateInventoryOrderLineWizard(models.TransientModel):
    _name = "create.inventory.order.line.wizard"
    _description = "CreateInventoryOrderLineWizard"

    product_id = fields.Many2one(
        'product.product', string="Product", required=True)
    unit_price = fields.Float(string="Unit Price", required=True)
    order_id = fields.Many2one('create.inventory.order.wizard')
    location_dest_id = fields.Many2one(
        "stock.location", string="Destination Location", required=True)
    location_id = fields.Many2one(
        "stock.location", string="Source Location", required=True)
    description = fields.Char(string="Description", required=True)
    product_uom = fields.Many2one('uom.uom', string="UoM", required=True)
    product_uom_qty = fields.Float(string="Demand", required=True)
    reserved_availability = fields.Float(
        string="Quantity Reserved", required=True)
    quantity_done = fields.Float(string="Quantity Done", required=True)
