# -*- coding: utf-8 -*-

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    passport_type = fields.Char('Type of identification')
    passport_series = fields.Char('Passport Series')
    passport_issue_date = fields.Date('Date of issue', help='Date of issue of passport')
    passport_issued_by = fields.Char('Issued by', help='Passport issued by department')
