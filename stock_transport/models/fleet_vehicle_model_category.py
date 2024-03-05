# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class FleetVehicleModelCategory(models.Model):
    _inherit="fleet.vehicle.model.category"

    max_weight=fields.Integer(string="Max Weight")
    max_volume=fields.Integer(string="Max Volume")

    @api.depends("name","max_weight","max_volume")
    def _compute_display_name(self):
       for record in self:
            record.display_name = f"{record.name} ({record.max_weight}Kg) ({record.max_volume}m\u00b3)"