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
class agenda(models.Model):
    _name = 'iut.dip.agenda'
    date_start = fields.Datetime()
    date_stop = fields.Datetime()
    room = fields.Char()
    classe_id = fields.Many2one('iut.dip.classe', string="Classe")
    cours_id = fields.Many2one('iut.dip.cours', string="Cours")
