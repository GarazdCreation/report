# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class PrintProductLabel(models.TransientModel):
    _name = "print.product.label"

    @api.model
    def _get_products(self):
        res = []
        if self._context.get('active_model') == 'product.template':
            products = self.env[self._context.get('active_model')].browse(self._context.get('default_product_ids'))
            for product in products:
                label = self.env['product.label'].create({
                    'product_id': product.product_variant_id.id,
                })
                res.append(label.id)
        elif self._context.get('active_model') == 'product.product':
            products = self.env[self._context.get('active_model')].browse(self._context.get('default_product_ids'))
            for product in products:
                label = self.env['product.label'].create({
                    'product_id': product.id,
                })
                res.append(label.id)
        return res

    label_ids = fields.One2many('product.label', 'wizard_id',
        string='Labels for Products', default=_get_products)
    multi_label = fields.Boolean('Print Several Labels')
    template = fields.Selection([
            ('garazd_product_label.report_product_label_57x35_template', 'Label 57x35mm (A4: 21 pcs on sheet, 3x7)')
        ], default='garazd_product_label.report_product_label_57x35_template', string="Label template")

    @api.multi
    def action_print(self):
        self.ensure_one()
        return self.env['report'].get_action(self.label_ids.filtered('selected').mapped('id'), self.template)

    @api.multi
    def reopen_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Custom Product Labels',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }

    @api.multi
    def action_set_qty_to_one(self):
        self.ensure_one()
        self.label_ids.update({'qty': 1})
        return self.reopen_form()

    @api.multi
    def action_restore_initial_qty(self):
        self.ensure_one()
        for label in self.label_ids:
            if label.qty_initial:
                label.update({'qty': label.qty_initial})
        return self.reopen_form()
