from odoo import models, fields

class Clinic(models.Model):
    _name = 'hospital.clinic'
    _description = 'Clinic'

    name = fields.Char(string="Clinic Name", required=True)

    open_datetime = fields.Datetime(
        string="Open Datetime"
    )

    end_datetime = fields.Datetime(
        string="End Datetime"
    )

    description = fields.Text(
        string="Description"
    )