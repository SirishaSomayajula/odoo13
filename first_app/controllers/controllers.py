# -*- coding: utf-8 -*-
# from odoo import http


# class FirstApp(http.Controller):
#     @http.route('/first_app/first_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/first_app/first_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('first_app.listing', {
#             'root': '/first_app/first_app',
#             'objects': http.request.env['first_app.first_app'].search([]),
#         })

#     @http.route('/first_app/first_app/objects/<model("first_app.first_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('first_app.object', {
#             'object': obj
#         })
