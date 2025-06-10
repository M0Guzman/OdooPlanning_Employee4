from odoo import fields, models

class PlanningSlot(models.Model):
    _inherit = 'planning.slot'

    multi_employee_ids = fields.Many2many('hr.employee', string="Employees")