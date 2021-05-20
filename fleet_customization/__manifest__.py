# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring, manifest-version-format
# pylint: disable=manifest-required-author
{
    'name': 'customization in fleet',
    'summary': 'customization in fleet',
    'author': "Hadeel Mahmoud",
    'category': 'Fleet',
    'version': '14.0.0.2.0',
    'depends': [
        'base','fleet'
    ],
    'data': [
        'security/access.xml',
        'security/ir.model.access.csv',
        'views/fleet_custom.xml',
        'report/report_fleet_temp.xml',
        'report/report_fleet.xml',


    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
