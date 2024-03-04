# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    vehicle_id = fields.Many2one("fleet.vehicle.model",string="Vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category",string="Category")
    weight = fields.Float(string="Weight")
    volume = fields.Float(string="Volume")
    dock_id = fields.Many2one("dock",string="Dock")
    