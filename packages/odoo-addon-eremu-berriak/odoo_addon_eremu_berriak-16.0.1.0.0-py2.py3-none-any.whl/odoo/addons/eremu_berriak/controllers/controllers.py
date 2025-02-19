# -*- coding: utf-8 -*-
# from odoo import http


# class EremuBerriak(http.Controller):
#     @http.route('/eremu_berriak/eremu_berriak', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eremu_berriak/eremu_berriak/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('eremu_berriak.listing', {
#             'root': '/eremu_berriak/eremu_berriak',
#             'objects': http.request.env['eremu_berriak.eremu_berriak'].search([]),
#         })

#     @http.route('/eremu_berriak/eremu_berriak/objects/<model("eremu_berriak.eremu_berriak"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eremu_berriak.object', {
#             'object': obj
#         })
