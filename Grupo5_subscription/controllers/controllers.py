# -*- coding: utf-8 -*-
from odoo import http

# class Subscription(http.Controller):
#     @http.route('/subscription/subscription/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/subscription/subscription/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('subscription.listing', {
#             'root': '/subscription/subscription',
#             'objects': http.request.env['subscription.subscription'].search([]),
#         })

#     @http.route('/subscription/subscription/objects/<model("subscription.subscription"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('subscription.object', {
#             'object': obj
#         })