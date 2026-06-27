from odoo import models, fields


class Clinic(models.Model):
    _name = 'hospital.clinic'
    _description = 'Clinic'

    name = fields.Char(
        string="Clinic Name",
        required=True
    )

    open_datetime = fields.Datetime(
        string="Open Datetime"
    )

    end_datetime = fields.Datetime(
        string="End Datetime"
    )

    description = fields.Text(
        string="Description"
    )

    cost = fields.Float(
        string="Cost"
    )

    state = fields.Selection([
        ('new', 'New'),
        ('open', 'Open'),
        ('close', 'Close'),
    ], string="State", default='new', tracking=True)

    doctor_id = fields.Many2one(
        'res.partner',
        string="Doctor"
    )

    patient_ids = fields.Many2many(
        'hospital.patient',
        string="Patients"
    )

    def action_open(self):
        for rec in self:
            rec.state = 'open'

    def action_close(self):
        for rec in self:
            rec.state = 'close'
