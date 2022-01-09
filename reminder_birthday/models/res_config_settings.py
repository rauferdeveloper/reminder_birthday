# -*- coding: utf-8 -*-
# Powered by Raul F.
# © 2022 Raul F.(<https://github.com/rauferdeveloper>)

from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    send_employee_reminder_birthday = fields.Boolean(related="company_id.send_employee_reminder_birthday", readonly=False)
