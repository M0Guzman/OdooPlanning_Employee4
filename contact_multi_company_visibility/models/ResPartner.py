from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    allowed_company_ids = fields.Many2many(
        'res.company',
        string="Visible in Companies",
        help="Restrict visibility of this contact to specific companies. If empty, visible to all."
    )
