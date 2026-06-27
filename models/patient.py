from odoo import models, fields


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'

    name = fields.Char(
        string="Patient Name",
        required=True
    )

    age = fields.Integer(
        string="Age"
    )

    phone = fields.Char(
        string="Phone"
    )

    clinic_ids = fields.Many2many(
        'hospital.clinic',
        string="Clinics"
    )
