{
    'name': "hospital_system",

    'summary': "Manage clinics, doctors and patients",

    'description': """
Hospital Management
====================
- Manage Clinics (with cost, state, doctor, patients)
- Manage Patients
- Open/Close clinic workflow restricted to a dedicated security group
- Doctors (res.partner) show the clinics they are assigned to
- List, Form, Kanban, Pivot and Graph views for Clinics
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Services/Hospital',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/clinic_views.xml',
        'views/patient_views.xml',
        'views/res_partner_views.xml',
    ],

    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
