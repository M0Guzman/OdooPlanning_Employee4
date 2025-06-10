{
    'name': 'Planning Multi Employee',
    'version': '1.0',
    'summary': 'Permet d\'assigner plusieurs employés à un créneau de planning',
    'description': "Ce module étend le module Planning d'Odoo pour permettre la sélection de plusieurs employées.",
    'category': 'Human Resources',
    'author': 'Cortys SRL',
    'depends': ['planning', 'hr'],
    'data': [
    'views/planning_slot_form_views.xml',
    'views/planning_slot_list_views.xml',
    'views/planning_slot_kanban_views.xml',
    'views/planning_slot_template',
],

    'installable': True,
    'application': True,
    
}