# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    vehicle_id = fields.Many2one("fleet.vehicle.model",string="Vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category",string="Category")
    weight = fields.Float(string="Weight",compute="_compute_weight",store="True")
    volume = fields.Float(string="Volume",compute='_compute_volume',store="True")
    dock_id = fields.Many2one("dock",string="Dock")
    transfer = fields.Integer(string="Transfer",compute="_compute_transfer",store="True")
    lines = fields.Integer(string="Lines",compute="_compute_lines",store="True")
    
    @api.depends('vehicle_category_id','picking_ids')
    def _compute_volume(self):
        for record in self:
            if record.vehicle_category_id:
                total = sum(pick.volume for pick in record.picking_ids)
                record.volume = (total/record.vehicle_category_id.max_volume)*100

    @api.depends('vehicle_category_id','picking_ids')
    def _compute_weight(self):
        for record in self:
            if record.vehicle_category_id and record.picking_ids:
                total = sum(pick.weight for pick in record.picking_ids)
                record.weight = (total/record.vehicle_category_id.max_weight)*100
            

    @api.depends('move_line_ids')
    def _compute_lines(self):
        for record in self:
            record.lines=len(record.move_line_ids)

    @api.depends('picking_ids')
    def _compute_transfer(self):
        for record in self:
            record.transfer=len(record.picking_ids)

    @api.onchange("vehicle_id")
    def _onchange_vehicle(self):
        for record in self:
            record.vehicle_category_id = record.vehicle_id.category_id

    @api.depends("name","weight","volume")
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.weight}Kg) ({record.volume}m\u00b3)"