# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):

    _name = 'spaceship'
    _description = 'Something to get us to the Moon!!'
    
    name = fields.Char(string='Title', required=True)
    
    length = fields.Float(string='Length', required=True)
    diameter = fields.Float(string='Diameter', required=True)
    
    fuel_type = fields.Selection(string='Fuel Type',
                                 required=True,
                                 selection=[('rocket_fuel', 'Rocket Fuel'),
                                            ('nuclear', 'Nuclear')],
                                 copy=False)
    
    number_of_passengers = fields.Integer(string='Number of Passengers',
                                          required=True,
                                          copy=False)
    
    active = fields.Boolean(string='Active', default=True)
