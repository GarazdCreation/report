# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductLabel(models.TransientModel):
    _name = "product.label"

<<<<<<< HEAD
    selected = fields.Boolean('Print', compute='_compute_selected')
=======
    selected = fields.Boolean('Print', default=True)
>>>>>>> d4285b23632669a0e7dba2c338768e539caecd55
    product_id = fields.Many2one('product.product', 'Product', required=True)
    wizard_id = fields.Many2one('print.product.label', 'Print Wizard')
    qty_initial = fields.Integer('Initial Qty', default=1)
    qty = fields.Integer('Label Qty', default=1)

<<<<<<< HEAD
    @api.depends('qty')
    def _compute_selected(self):
        for record in self:
            if record.qty > 0:
                record.update({'selected': True})
            else:
                record.update({'selected': False})

    @api.multi
    def action_plus_qty(self):
        for record in self:
=======
    @api.multi
    def action_plus_qty(self):
        for record in self:
            if record.qty == 0:
                record.update({'selected': True})
>>>>>>> d4285b23632669a0e7dba2c338768e539caecd55
            record.update({'qty': record.qty+1})
            return record.wizard_id.reopen_form()

    @api.multi
    def action_minus_qty(self):
        for record in self:
            if record.qty > 0:
                record.update({'qty': record.qty-1})
<<<<<<< HEAD
=======
            if record.qty == 0:
                record.update({'selected': False})
>>>>>>> d4285b23632669a0e7dba2c338768e539caecd55
            return record.wizard_id.reopen_form()
