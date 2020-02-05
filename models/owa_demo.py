# -*- coding: utf-8 -*-
# QQ: 1294739135
# EMAIL: youzengjian@gmail.com
# AUTHOR: You Zengjian

from odoo import models, fields, api, _
from odoo.exceptions import AccessDenied, AccessError, UserError, ValidationError

class OwaDemo(models.Model):
    _name = 'owa.demo'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string=_("Name"))
    char = fields.Char(string=_("Char"))
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
    many2one = fields.Many2one(string=_("Many2one"), comodel_name='owa.demo')
    one2many = fields.One2many(string=_("One2many"), comodel_name='owa.demo.line', inverse_name='demo_id')
    many2many = fields.Many2many(string=_("Many2many"), comodel_name='owa.demo.tag')
    state = fields.Selection(string=_("State"), selection=[('draft', _("Draft")),
                                                           ('approving', _("Approving")),
                                                           ('approved', _("Approved")),
                                                           ('disapproved', _("Disapproved")),
                                                           ('cancel', _("Cancel"))],
                             default="draft")

    def show_approve(self):
        form_view_ref = self.env.ref('owa.owa_demo_view_form_approve')
        return {
            'type': 'ir.actions.act_window',
            'name': 'APPROVE',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'views': [(form_view_ref.id, 'form')],
            'target': 'new',
        }

    def submit(self):
        self.ensure_one()
        if self.state != 'draft':
            raise UserError(_("You can not submit this record!"))
        self.state = 'approving'

    def approve(self):
        self.ensure_one()
        if self.state != 'approving':
            raise UserError(_("You can not approve this record!"))
        self.state = 'approved'

    def disapprove(self):
        self.ensure_one()
        if self.state != 'approving':
            raise UserError(_("You can not disapprove this record!"))
        self.state = 'disapproved'

    def cancel(self):
        self.ensure_one()
        if self.state != 'draft':
            raise UserError(_("You can not cancel this record!"))
        self.state = 'cancel'

    def reset_to_draft(self):
        for item in self:
            item.state = 'draft'
