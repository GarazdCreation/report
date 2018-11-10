# -*- coding: utf-8 -*-
# Copyright (C) 2018 Yurii Razumovskyi <GarazdCreation@gmail.com>
# License OPL-1 (https://www.odoo.com/documentation/user/10.0/legal/licenses/licenses.html#odoo-apps).
{
    'name' : 'Ukrainian letter of authority',
    'version': '10.0.1.0.1',
    'category': 'Localization',
    'author': 'Garazd Creation',
    'website' : 'https://garazd.biz',
    'license': 'OPL-1',
    'summary': 'Printed form of ukrainian letter of authority',
    'description': """
        Module allows print the letter of authority for Ukraine.
    """,
    'depends' : ['account', 'hr'],
    'data': [
        'data/ir_sequence_data.xml',
        'views/account_invoice_views.xml',
        'views/hr_employee_views.xml',
        'report/letter_authority_reports.xml',
        'report/letter_authority_templates.xml',
    ],
    'price': 20.0,
    'currency': 'EUR',
    'support': 'support@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
