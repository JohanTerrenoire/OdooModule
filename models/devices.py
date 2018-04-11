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

class iutdevice(models.Model):
	_name = 'iut.it.device'

	name = fields.Char(required = True)
	date_allocation = fields.Date()
	serial_number = fields.Char(required = True)
	date_purchase = fields.Date()
	date_warranty_end = fields.Date()