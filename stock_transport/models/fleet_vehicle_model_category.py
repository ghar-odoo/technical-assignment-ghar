# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class FleetVehicleModelCategory(models.Model):
    _inherit="fleet.vehicle.model.category"

    max_weight=fields.Integer(string="Max Weight")
    max_volume=fields.Integer(string="Max Volume")

    @api.depends("max_weight","max_volume")
    def _compute_display_name(self):
        for record in self:
         record.display_name = record.name + ' (' + str(record.max_weight) + ',' + str(record.max_volume) + ')'