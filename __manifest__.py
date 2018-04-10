# -*- coding: utf-8 -*-
{
    'name': "classe",

    'summary': """
        Module de test pour Odoo""",

    'description': """
        Ceci est une description pour notre module personnalisé Odoo 11
    """,

    'author': "JohanTerrenoire",
    'website': "https://github.com/JohanTerrenoire/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/helico/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/iut_classe_views.xml',
        'iut_it_classe_menu.xml',
        'views/iut_model_type_views.xml',
        'security/tdsimodel_security.xml',
        'datas/datas.xml',
        'views/views.xml',
        'tdsimodel_menu.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
