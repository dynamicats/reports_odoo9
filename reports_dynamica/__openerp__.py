# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom reports layouts for Dynamica',
    'version': '1.1',
    'category': 'Reports',
    'sequence': 10,
    'summary': 'Reports',
    'depends': [
        'base', 'report',
    ],
    'description': """
        Custom reports layouts for Dynamica
    """,
    'data': [
        'views/layout_header_view.xml',
        'views/layout_footer_view.xml',
        'views/res_partner_templates_view.xml',
        'views/report_style_layout.xml',
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
