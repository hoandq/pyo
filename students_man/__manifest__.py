# -*- coding: utf-8 -*-
{
    'name': "Shcool Managements 10",

    'summary': """
        Phan mem quan ly Sinh vien""",

    'description': """
        Quan ly Diem, Sinh vien,...
    """,

    'author': "Doan Quang Hoan",
    'website': "http://www.yourcompany.com",

    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/v_students.xml',
       # 'views/templates.xml',
    ],
	'application':True,
	#'demo': [
    #    'demo/demo.xml',
	#],
}
