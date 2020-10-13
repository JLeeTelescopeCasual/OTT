# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):

    _name = 'volunteer.task'
    _description = 'Volunteer Task'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description', required=True)

    start = fields.Datetime(string='Start Time',
                            required=True)
    stop = fields.Datetime(string='Stop Time',
                           required=True)
    
    repeating = fields.Boolean(string='Repeating', default=False)
    repeats = fields.Integer('Repeats every X Days', default=0)
    
