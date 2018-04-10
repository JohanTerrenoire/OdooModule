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
class classe(models.Model):
    _name = 'iut.dip.classe'
    name = fields.Char()
    level = fields.Selection([('seconde', 'Seconde'), ('premiere', 'Première'), ('terminal', 'Terminale')])
    teacher_id = fields.Many2one('iut.dip.teacher', string="Professeur")
    student_ids = fields.One2many('iut.dip.student', 'classe_id', string="Elèves")
    nbStudents = fields.Integer(compute='_compute_nbStudents')
    agenda_ids = fields.One2many('iut.dip.agenda', 'classe_id', string="Agenda")

    @api.depends('student_ids')
    def _compute_nbStudents(self):
        for record in self:
            record.nbStudents = len(record.student_ids)
