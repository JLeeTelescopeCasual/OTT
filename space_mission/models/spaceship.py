# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Spaceship(models.Model):

    _name = 'spaceship'
    _description = 'Something to get us to the Moon!!'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Char(string='Description', required=False)
    
    length = fields.Float(string='Length', required=True)
    diameter = fields.Float(string='Diameter', required=True)
    volume = fields.Float(string='Volume', readonly=True)
    
    fuel_type = fields.Selection(string='Fuel Type',
                                 required=True,
                                 selection=[('rocket_fuel', 'Rocket Fuel'),
                                            ('nuclear', 'Nuclear')],
                                 copy=False)
    
    number_of_passengers = fields.Integer(string='Number of Passengers',
                                          required=True,
                                          copy=False)
    
    active = fields.Boolean(string='Active', default=True)

    @api.onchange('length','diameter')
    def _onchange_length_vs_diameter(self):
        if self.diameter > self.length:
            raise UserError('Length must be longer than diameter')
            
        self.volume = self.length * 3.14159265358979 * ( self.diameter / 2 ) * ( self.diameter / 2 )
            
    @api.constrains('length')
    def _check_length(self):
        for record in self:
            if record.length < 0:
                raise ValidationError('Length must be set greater than 0.')
                
    @api.constrains('diameter')
    def _check_diameter(self):
        for record in self:
            if record.diameter < 0:
                raise ValidationError('Diameter must be set greater than 0.')