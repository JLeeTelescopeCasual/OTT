# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exception import UserError, ValidationError

class Mission(models.Model):
    
    _name = 'mission'
    _description = 'A mission for the space mission module.'

    name = fields.Char(string='Title', required=True)
    description = fields.Char(string='Description', required=False)
    
#    spaceship many to one
# many to many - crew members
    launch_date = fields.Datetime(string='Launch Date', required=True)
    return_date = fields.Datetime(string='Return Date', required=True)
    
    @api.onchange('launch_date','return_date')
    def _onchange_launch_date_vs_return_date
        if self.launch_date > self.return_date:
            raise UserError('Launch Date must be before Return Date')
            
    