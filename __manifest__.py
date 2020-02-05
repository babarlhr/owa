# -*- coding: utf-8 -*-
# QQ: 1294739135
# EMAIL: youzengjian@gmail.com
# AUTHOR: You Zengjian

{
    'name': "owa",

    'summary': """
        ODOO WEB AUTOMATION BACKEND MODULE""",

    'description': """
        Long description of module's purpose
    """,

    'author': "youzengjian@gmail.com",
    'website': "https://www.github.com/youzengjian/owa/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/ir_actions_act_window.xml',
        'security/ir_actions_server.xml',
        'security/menu_items.xml',
        'data/owa_demo_tag.xml',
        'views/owa_demo.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        "static/src/xml/menu.xml",
    ],
    'application': True,
}