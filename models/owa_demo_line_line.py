# -*- coding: utf-8 -*-
# QQ: 1294739135
# EMAIL: youzengjian@gmail.com
# AUTHOR: You Zengjian

from odoo import models, fields, api, _

class OwaDemoLineLine(models.Model):
    _name = 'owa.demo.line.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string=_("Name"))
    boolean = fields.Boolean(string=_("Boolean"))
    integer = fields.Integer(string=_("Integer"))
    float = fields.Float(string=_("Float"))
    company_currency = fields.Many2one(string=_('Currency'), comodel_name="res.currency", default=lambda self: self.env.user.company_id.currency_id)
    monetary = fields.Monetary(string=_("Monetary"), currency_field='company_currency')
    text = fields.Text(string=_("Text"))
    html = fields.Html(string=_("Html"))
    date = fields.Date(string=_("Date"))
    datetime = fields.Datetime(string=_("Datetime"))
    binary = fields.Binary(string=_("Binary"))
    image = fields.Image(string=_("Image"))
    selection = fields.Selection(string=_("Selection"),
                                 selection=[('selection_test_1', _("Selection Test 1")),
                                            ('selection_test_2', _("Selection Test 2")),
                                            ('selection_test_3', _("Selection Test 3"))])
    reference = fields.Reference(selection=[('ir.actions.report', 'ir.actions.report'),
                                            ('ir.actions.act_window', 'ir.actions.act_window'),
                                            ('ir.actions.act_url', 'ir.actions.act_url'),
                                            ('ir.actions.server', 'ir.actions.server'),
                                            ('ir.actions.client', 'ir.actions.client')],
                                 string=_("Reference"))
    many2one = fields.Many2one(string=_("Many2one"), comodel_name='res.partner')
    demo_line_id = fields.Many2one(string=_("Many2one"), comodel_name='owa.demo.line')
    many2many = fields.Many2many(string=_("Many2many"), comodel_name='owa.demo.tag')
