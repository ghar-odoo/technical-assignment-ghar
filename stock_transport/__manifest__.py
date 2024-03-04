# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'STOCK TRANSPORT',
    'version': '1.0',
    'summary': 'Stock Transport Module',
    'description': "",
    'author': "Ghanshyam Rathore",
    'depends' : ['base','stock_picking_batch','fleet'],
    'data':[
        'security/ir.model.access.csv',
        'views/fleet_vehicle_category_view.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml'
    ],
     'installable': True,
    'application': True,
    'license': 'LGPL-3'
}