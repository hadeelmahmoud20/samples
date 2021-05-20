# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring, manifest-version-format
# pylint: disable=manifest-required-author
{
    'name': 'Reservation for Vehicel',
    'summary': 'customization in fleet',
    'author': "Hadeel Mahmoud",
    'website': "Reservation for Vehicel",
    'category': 'Fleet',
    'version': '14.0.0.2.0',
    'depends': [
        'base','fleet','calendar'
    ],
    'data': [
        'security/access.xml',
        'security/ir.model.access.csv',
        'views/fleet_reservation.xml',


    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
