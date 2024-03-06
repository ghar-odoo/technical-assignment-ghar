# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class StockPicking(models.Model):
    _inherit="stock.picking"

    volume = fields.Float(compute="_compute_picking_volume_weight",string="Volume")
    weight = fields.Float(compute="_compute_picking_volume_weight",string="weight")

    @api.depends('move_ids')
    def _compute_picking_volume_weight(self):
        for record in self:
            record.volume = sum(product.product_id.volume*product.quantity for product in record.move_ids)
            record.weight = sum(product.product_id.weight*product.quantity for product in record.move_ids)
          
  
                