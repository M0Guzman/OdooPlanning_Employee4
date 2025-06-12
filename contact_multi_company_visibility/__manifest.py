{
    'name': 'Contact Multi-Company Visibility',
    'version': '1.0',
    'category': 'Contacts',
    'summary': 'Restrict contact visibility per company in multi-company setup',
    'depends': ['base'],
    'data': [
        'security/res_partner_rule.xml',
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
