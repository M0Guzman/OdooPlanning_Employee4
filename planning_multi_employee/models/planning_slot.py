from odoo import fields, models

class PlanningSlot(models.Model):
    _inherit = 'planning.slot'
    
    multi_employee_ids = fields.Many2many(
        'hr.employee', 
        string="Employés",
        help="Sélectionnez plusieurs employés pour ce créneau"
    )
     # Solution définitive pour supprimer le champ
    employee_skill_ids = None  # Suppression radicale au niveau Python

class PlanningSlotTemplate(models.Model):
    _inherit = 'planning.slot.template'
    
    multi_employee_ids = fields.Many2many(
        'hr.employee', 
        string="Employés",
        help="Sélectionnez plusieurs employés pour ce modèle"
    )