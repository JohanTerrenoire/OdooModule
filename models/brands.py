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

class iutbrand(models.Model):
	_name = 'iut.it.brand'

	name = fields.Char(required = True, unique = True)
	warranty_delay_month = fields.Integer()
	support_phone = fields.Integer()