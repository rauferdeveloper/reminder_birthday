# -*- coding: utf-8 -*-
# Powered by Raul F.
# © 2022 Raul F.(<https://github.com/rauferdeveloper>)

from odoo import api, fields, models, _

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model
    def cron_reminder_birthday(self):
        today = fields.Date.context_today(self)
        employees = self.env['hr.employee'].search([
            ('birthday', '!=', False), 
            ('work_email', '!=', False)
        ])
        mail_channel_partner_obj = self.env['mail.channel.partner']
        odoobot = self.env.ref('base.partner_root')
        for employee in employees:
            if employee.user_id:
                users = self.env['res.users'].search([
                    ('id', '!=', False), 
                ])
            else:
                users = self.env['res.users'].search([])
            if employee.company_id.send_employee_reminder_birthday and employee.birthday.day == today.day and employee.birthday.month == today.month:
                template_id = self.env.ref('reminder_birthday.employee_reminder_birthday_template')
                if template_id:
                    template_id.send_mail(employee.id, force_send=True)

                message = _("Today is %s's birthday, congratulations!") % employee.name
                if users:
                    for user in users:
                        if employee.user_id and employee.user_id.id == user.id:
                            continue
                        if employee.company_id.id not in user.company_ids.ids:
                            continue
                        channel = mail_channel_partner_obj.sudo().search([
                            ('partner_id','=',user.partner_id.id),
                            ('channel_id.channel_type','=','chat'),
                            ('channel_id.channel_partner_ids.id','=',user.partner_id.id),
                            ('channel_id.public','=','private')
                            
                        ])
                        channel = channel.filtered(lambda x: len(x.channel_id.channel_partner_ids) == 1 and x.channel_id.is_chat == True and x.channel_id.member_count == 2)
                        if channel:
                            channel_send = channel.channel_id
                            if channel_send:
                                notification_ids = [(0, 0, {
                                    'res_partner_id': user.partner_id.id,
                                    'notification_type': 'inbox'
                                })]
                                channel_send.message_post(body=message, message_type="notification", subtype_xmlid="mail.mt_comment", 
                                    author_id=odoobot.id, 
                                    notification_ids=notification_ids)
                        else:
                            channel_send = self.env['mail.channel'].sudo().create({
                                'channel_partner_ids': [
                                    (4, user.partner_id.id),
                            
                                ],
                                'is_chat': True,
                                'public': 'private',
                                'channel_type': 'chat',
                                'name': odoobot.name + ', '+ user.partner_id.name,
                                
                                
                            })
                            if channel_send:
                                notification_ids = [(0, 0, {
                                    'res_partner_id': user.partner_id.id,
                                    'notification_type': 'inbox'
                                })]
                                channel_send.message_post(body=message, message_type="notification", subtype_xmlid="mail.mt_comment", 
                                    author_id=odoobot.id, 
                                    notification_ids=notification_ids)
