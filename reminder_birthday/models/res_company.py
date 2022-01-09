# -*- coding: utf-8 -*-

from odoo import models, fields


class res_company(models.Model):
    _inherit = 'res.company'

    send_employee_reminder_birthday = fields.Boolean(string='Reminder Birthday notification')