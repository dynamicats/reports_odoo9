# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom invoice reports for Dynamica',
    'version': '1.1',
    'category': 'Invoice Reports',
    'sequence': 10,
    'summary': 'Invoice reports',
    'depends': [
        'reports_dynamica', 'account',
    ],
    'description': """
        Custom invoice reports for Dynamica
    """,
    'data': [
        'views/layout_view.xml',
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
