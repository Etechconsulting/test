# -*- coding: utf-8 -*-
from odoo import http

# class Scopeatesting(http.Controller):
#     @http.route('/scopeatesting/scopeatesting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scopeatesting/scopeatesting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scopeatesting.listing', {
#             'root': '/scopeatesting/scopeatesting',
#             'objects': http.request.env['scopeatesting.scopeatesting'].search([]),
#         })

#     @http.route('/scopeatesting/scopeatesting/objects/<model("scopeatesting.scopeatesting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scopeatesting.object', {
#             'object': obj
#         })