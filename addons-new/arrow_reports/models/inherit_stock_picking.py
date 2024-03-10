from odoo import api, models, fields, _


class StockPicking(models.Model):
    _inherit = "stock.picking"

    # total_number_of_model = fields.Integer()
    total_product_of_delivery_orders = fields.Integer(string='Total Product:',compute='_total_product_of_delivery_orders',help="total Products of delivery orders")
    total_quantity_of_delivery_orders = fields.Integer(string='Reserved Quantity:',compute='_total_quantity_of_delivery_orders',help="total Quantity of delivery orders")
    total_quantity_of_delivery_orders_done = fields.Integer(string='Done Quantity:',compute='_total_quantity_of_delivery_orders',help="total Quantity of delivery orders")

    #compute method of total product
    def _total_product_of_delivery_orders(self):
        for record in self:
            list_of_delivery_product=[]
            for line in record.move_lines:
                list_of_delivery_product.append(line.product_id)
            record.total_product_of_delivery_orders = len(set(list_of_delivery_product))

    #compute method of total quantity
    def _total_quantity_of_delivery_orders(self):
        for record in self:
            total_qty = 0
            total_qty_done = 0
            for line in record.move_lines:
                total_qty = total_qty + line.product_uom_qty
                total_qty_done = total_qty_done + line.quantity_done
            record.total_quantity_of_delivery_orders = total_qty
            record.total_quantity_of_delivery_orders_done = total_qty_done

