# -*- coding: utf-8 -*-
{
    'name': "Bookstore",
    'summary': """Bookstore Management""",
    'description': """
        Bookstore Management
    """,
    'author': "Andrian",
    'website': "http://www.sgeede.com",
    'category': 'Management',
    'sequence': -100,
    'version': '0.1',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/employee_views.xml',
        'views/book_views.xml',
        'views/appointment_views.xml',
        'views/category_views.xml',
        'views/inventory_views.xml',
        'views/transaction_views.xml',
        'reports/transaction_report_detail.xml',
        # 'reports/report.xml',
        # 'reports/transaction_detail_template.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
