{
    'name': 'Planning Multi Employee',
    'version': '1.0',
    'summary': 'Permet d\'assigner plusieurs employés à un créneau de planning',
    'description': "Ce module étend le module Planning d'Odoo pour permettre la sélection de plusieurs employés.",
    'category': 'Human Resources',
    'author': 'Cortys SRL',
    'depends': ['planning', 'hr'],
    'data': [
        'views/planning_slot_search_views.xml',
        'views/planning_slot_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}