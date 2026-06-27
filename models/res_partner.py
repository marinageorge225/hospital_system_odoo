from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    clinic_ids = fields.One2many(
        'hospital.clinic',
        'doctor_id',
        string="Clinics"
    )
