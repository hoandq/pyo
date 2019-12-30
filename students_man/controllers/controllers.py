# -*- coding: utf-8 -*-
# from odoo import http


# class StudentsMan(http.Controller):
#     @http.route('/students_man/students_man/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/students_man/students_man/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('students_man.listing', {
#             'root': '/students_man/students_man',
#             'objects': http.request.env['students_man.students_man'].search([]),
#         })

#     @http.route('/students_man/students_man/objects/<model("students_man.students_man"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('students_man.object', {
#             'object': obj
#         })
