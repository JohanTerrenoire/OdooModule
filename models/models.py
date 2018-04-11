# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class tdsimodel(models.Model):
#     _name = 'tdsimodel.tdsimodel'
#
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class iutmodel(models.Model):
	_name = 'iut.it.model'

	name = fields.Char(required = True)
	ref = fields.Char(unique = True)
	type_ids = fields.Many2many('iut.it.model.type', string='Types')
	brand_id = fields.Many2one('iut.it.brand', string='Brand')