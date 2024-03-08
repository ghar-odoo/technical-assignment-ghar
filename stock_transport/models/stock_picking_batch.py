# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models
from odoo.tools import float_compare
from odoo.exceptions import UserError,ValidationError

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    vehicle_id = fields.Many2one("fleet.vehicle",string="Vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category",string="Category")
    weight = fields.Float(string="Weight",compute="_compute_volume_weight",store="True")
    volume = fields.Float(string="Volume",compute='_compute_volume_weight',store="True")
    dock_id = fields.Many2one("dock",string="Dock")
    transfer = fields.Integer(string="Transfer",compute="_compute_transfer",store="True")
    lines = fields.Integer(string="Lines",compute="_compute_lines",store="True")
    total_weight = fields.Float(compute="_compute_volume_weight")
    total_volume = fields.Float(compute="_compute_volume_weight")

    @api.depends('vehicle_category_id','picking_ids')
    def _compute_volume_weight(self):
        for record in self:
            if record.vehicle_category_id and record.picking_ids:
                record.total_volume = sum(picking.volume for picking in record.picking_ids)
                record.total_weight = sum(picking.weight for picking in record.picking_ids)
                record.weight = (record.total_weight/record.vehicle_category_id.max_weight)*100
                record.volume = (record.total_volume/record.vehicle_category_id.max_volume)*100

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

    @api.depends("weight","volume")
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.weight}Kg) ({record.volume}m\u00b3)  {record.vehicle_id.driver_id.name}"

    @api.constrains("total_weight","vehicle_category_id")
    def _check_weight(self):
        for record in self:
            if(
                float_compare(record.total_weight,record.vehicle_category_id.max_weight,precision_rounding=0.01)>0
            ):
                raise ValidationError(
                    "total weight should be less than max weight of vehicle category"
                )