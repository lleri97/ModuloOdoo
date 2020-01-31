# -*- coding: utf-8 -*-
{
    'name': "Grupo5_2dam2curious_subscription",

    'summary': """RETO2_GRUPO5_""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Grupo 5 Reto2",
    'website': "http://www.2dam2curious.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'product',
    ],

    # always loaded
    'data': [
        'views/subscription_views.xml',
        'views/partner_views.xml',
        'security/data_security.xml',
        'security/ir.model.access.csv',
        'views/subscription_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
    'installable': True
}
