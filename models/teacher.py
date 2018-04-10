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
class teacher(models.Model):
    _name = 'iut.dip.teacher'
    name = fields.Char()
    classe_ids = fields.One2many('iut.dip.classe', 'teacher_id', string="Classes")
