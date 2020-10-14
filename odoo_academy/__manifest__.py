# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Acadamy app to manage Training""",
    
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author': 'John',

    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_view.xml',
    ],
    
    'demo': [
        'demo/academy_demo.xml',
    ],
}
