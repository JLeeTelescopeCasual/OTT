# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):

    _name = 'library.book'
    _description = 'A Library Book'
    
    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    editors = fields.Char(string='Editor')
    edition = fields.Char(string='Edition')
    isbn = fields.Char(string='ISBN',
                       copy=False)
    
    genre = fields.Selection(string='Genre',
                             selection=[('young_adult','Young Adult'),
                                        ('biography','Biography'),
                                        ('poetry','Poetry')],
                             copy=False)
    