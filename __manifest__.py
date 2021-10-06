# -*- coding: utf-8 -*-
{
    'name': "Hotel Booking",
    'sequence': 1,
    'summary': """
        Booking nearby hotels""",

    'description': """
        Booking nearby hotels
    """,
    'author': "Kamrul",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_item_views.xml',
        'views/nearby_hotels_views.xml',
        'views/hotel_booking_views.xml',
        'views/hotel_api_views.xml',
        'reports/report.xml',
        'reports/booking_invoice_views.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
