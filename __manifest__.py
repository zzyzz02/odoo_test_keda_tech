# -*- coding: utf-8 -*-
{
    'name': "Fajar Odoo Test - Material Registration",

    'summary': """
        This module is used to register material in the system.    
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Fajar Aulia Anugrah - 081268888199",
    'website': "http://www.yourcompany.com",

    'category': 'Material',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        
        'views/material_registration.xml',
        'views/res_partner.xml',
        
        'menu.xml',
    ],
    # only loaded in demonstration mode
    
    'installable': True,
    'application': True,
}
