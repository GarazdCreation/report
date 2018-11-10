# -*- coding: utf-8 -*-

from . import num2t4ua
from odoo import api, models


class report_letter_authority(models.AbstractModel):
    _name = 'report.l10n_ua_letter_authority.report_la'

    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('l10n_ua_letter_authority.report_la')
        docs = self.env['account.invoice'].browse(docids)
        qty_char = {}
        for doc in docs:
            lines_qty = {}
            for line in doc.invoice_line_ids:
                lines_qty[line.id] = num2t4ua.num2text(int(line.quantity))
            qty_char[doc.id] = lines_qty
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': docs,
            'data': data,
            'qty_char': qty_char,
        }
        return report_obj.render('l10n_ua_letter_authority.report_la', docargs)
