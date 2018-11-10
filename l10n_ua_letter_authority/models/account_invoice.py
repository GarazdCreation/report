# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    la_number = fields.Integer('Number')
    la_issue_date = fields.Date('Date of issue', default=fields.Date.context_today)
    la_valid_until = fields.Date('Valid until') 
    la_employee_id = fields.Many2one('hr.employee', 'Employee of letter of authority')
    la_director_id = fields.Many2one('hr.employee', 'Director')
    la_accountant_id = fields.Many2one('hr.employee', 'Chief Accountant')

    @api.model
    def create(self, vals):
        result = super(AccountInvoice, self).create(vals)
        if result.type == 'in_invoice':
            result.la_number = self.env['ir.sequence'].next_by_code('letter.authority') or None
        return result

    @api.onchange('la_issue_date')
    def onchange_issue_date(self):
        if self.la_issue_date:
            date_valid = fields.Date.to_string(fields.Date.from_string(self.la_issue_date) + timedelta(days=10))
            self.update({'la_valid_until': date_valid})
