# -*- coding: utf-8 -*-
# Powered by Raul F.
# © 2022 Raul F.(<https://github.com/rauferdeveloper>)

from odoo import api, fields, models, _

class HrEmployee(models.Model):
    _inherit = 'mail.channel'

    member_count = fields.Integer(string="Member Count", compute='_compute_member_count', compute_sudo=True, help="Excluding guests from count.")
    
    @api.depends('channel_partner_ids')
    def _compute_member_count(self):
        read_group_res = self.env['mail.channel.partner'].read_group(domain=[('channel_id', 'in', self.ids)], fields=['channel_id'], groupby=['channel_id'])
        member_count_by_channel_id = {item['channel_id'][0]: item['channel_id_count'] for item in read_group_res}
        for channel in self:
            channel.member_count = member_count_by_channel_id.get(channel.id, 0)