# -*- coding: utf-8 -*-
from odoo import models, fields, api
class employee(models.Model):
    _inherit = 'res.partner'
    aadhar = fields.char()