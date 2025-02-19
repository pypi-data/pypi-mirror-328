# -*- coding: utf-8 -*-
{
    'name': "eremuBerriak",

    'summary': """
        Herentzia bidez mantenuko ekipoei eremu berriak gehitzeko modulua""",

    'description': """
        Ekipoetarako eremu berriak
    """,

    'author': "Zornotza LHII Infor",
    'website': "https://fpzornotzalh.eus/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','maintenance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/eremuBerriak_bista.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
