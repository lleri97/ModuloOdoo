# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    subscription_ids = fields.One2many(
        'subscription.subscription', 'customer_id', string="Contracts")
    subscription_count = fields.Integer(compute='_compute_sub_count')

    @api.multi
    def _compute_sub_count(self):
        for rec in self:
            rec.subscription_count = len(rec.subscription_ids)

    @api.multi
    def action_open_subscriptions(self):
        self.ensure_one()
        ctx = self.env.context.copy()
        action = self.env.ref('subscription.action_subscription').read()[0]
        action['domain'] = [('customer_id', '=', self.id)]
        return action
