# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Subscription(models.Model):
    _name = 'subscription.subscription'
    _description = 'Abstract Recurring Contract'
    _order = 'date_start ASC, id DESC'

    @api.model
    def _select_plan(self):
        return [
            ('monthly', 'Monthly'),
            ('biannual', 'Biannual'),
            ('yearly', 'Yearly'),
        ]

    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.user.company_id.currency_id.id)
    name = fields.Char(compute='subscription_name_definition', store=True, index=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    agent_id = fields.Many2one('res.users', string='Commercial Agent')
    active = fields.Boolean(default=True, string='Active')
    invoicing_frequency = fields.Selection(string='Invoicing Frequency', selection=_select_plan, default='yearly')
    product_id = fields.Many2one('product.product', String='Product', required=True)
    price = fields.Float(string='Price')
    date_start = fields.Date(default=fields.Date.today, string='Date Start')
    date_end = fields.Date(string='Date End', store=True)
    tag_ids = fields.Many2many(
        comodel_name='subscription.tag',
        relation='subscription_tag_rel',
        column1='subscription_id',
        column2='tag_id',
        string='Tag',
    )

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for rec in self:
            if rec.date_end and rec.date_end <= rec.date_start:
                raise ValidationError(_('End date must be greater than start date.'))

    @api.depends('customer_id', 'customer_id.name', 'date_start')
    def subscription_name_definition(self):
        for rec in self:
            if rec.customer_id:
                rec.name = '%s - %s' % (rec.customer_id.name, rec.date_start)
            else:
                rec.name = 'Contract name...'

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.price = self.product_id.lst_price


class Tag(models.Model):
    _name = 'subscription.tag'
    _description = 'Tags for subscriptions'

    name = fields.Char('Name')
    color = fields.Integer(string='Color Index')
