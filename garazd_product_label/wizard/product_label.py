# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductLabel(models.TransientModel):
    _name = "product.label"
    _description = 'Product Label'

    selected = fields.Boolean(
        string='Print',
        compute='_compute_selected',
        readonly=True,
    )
    wizard_id = fields.Many2one('print.product.label', 'Print Wizard')
    product_id = fields.Many2one('product.product', 'Product', required=True)
    barcode = fields.Char('Barcode', related='product_id.barcode')
    qty_initial = fields.Integer('Initial Qty', default=1)
    qty = fields.Integer('Label Qty', default=1)

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
            record.update({'qty': record.qty + 1})

    @api.multi
    def action_minus_qty(self):
        for record in self:
            if record.qty > 0:
                record.update({'qty': record.qty - 1})
