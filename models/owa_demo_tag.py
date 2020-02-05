# -*- coding: utf-8 -*-
# QQ: 1294739135
# EMAIL: youzengjian@gmail.com
# AUTHOR: You Zengjian

from odoo import models, fields, api, _

class OwaDemoTag(models.Model):
    _name = 'owa.demo.tag'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string=_("Name"))
