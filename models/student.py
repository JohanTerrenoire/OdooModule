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
class student(models.Model):
    _name = 'iut.dip.student'

    prenom = fields.Char()
    nom = fields.Char()
    date_anniv = fields.Date()
    age = fields.Integer(compute='_compute_age', default=0)
    classe_id = fields.Many2one('iut.dip.classe', string="Classe")

    @api.depends('date_anniv')
    def _compute_age(self):
    	for record in self:
    		now = datetime.date.today()
    		try:
    			date_anniv = datetime.datetime.strptime(record.date_anniv, '%Y-%m-%d').date()
    			record.age = (now-date_anniv).days/365
    		except TypeError:
    			record.age = 0
