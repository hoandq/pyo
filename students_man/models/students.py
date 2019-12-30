# -*- coding: utf-8 -*-

from odoo import models, fields, api


class students(models.Model):
     _name = 'students_info'
     _description = 'Thong tin sinh vien'

     ten = fields.Char()
     tuoi = fields.Integer()

