# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class Dock(models.Model):
    _name="dock"
    _description="dock description"

    name = fields.Char()