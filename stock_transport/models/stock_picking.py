# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class StockPicking(models.Model):
    _inherit="stock.picking"

    volume = fields.Float(compute="_compute_picking_volume",string="Volume")
    weight = fields.Float(compute="_compute_picking_weight",string="weight")

    def _compute_picking_volume(self):
        for record in self:
            record.volume=0
            for product in record.move_ids:
                record.volume+=product.product_id.volume*product.quantity
    
    def _compute_picking_weight(self):
        for record in self:
            record.weight=0
            for product in record.move_ids:
                record.weight+=product.product_id.weight*product.quantity