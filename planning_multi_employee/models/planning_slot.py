from odoo import fields, models

class PlanningSlot(models.Model):
    _inherit = 'planning.slot'

    multi_employee_ids = fields.Many2many(
        'resource.resource',
        string="Employés",
        help="Sélectionnez plusieurs employés pour ce créneau"
    )
