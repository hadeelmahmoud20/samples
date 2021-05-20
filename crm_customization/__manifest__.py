# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring, manifest-version-format
# pylint: disable=manifest-required-author
{
    'name': 'customization for crm',
    'summary': 'customization in crm',
    'author': "Hadeel Mahmoud",
    'website': "http://www.white-code.co.uk",
    'category': 'CRM',
    'version': '13.0.0.2.0',
    'depends': [
        'base','account','sale','product','survey','mail'
    ],
    'data': [
        'security/access.xml',
        'security/ir.model.access.csv',
        'views/account_crm.xml',

    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
