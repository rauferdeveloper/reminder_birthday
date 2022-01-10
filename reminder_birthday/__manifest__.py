# -*- coding: utf-8 -*-
# Powered by Raul F.
# © 2022 Raul F.(<https://github.com/rauferdeveloper>)

{
    'name': 'Birthday Reminder Notification',
    'version': '15.0.0.1',
    'category': 'Tools',
    'summary': 'Birthday reminder for employee',
    'description': """
        This module send email and message notification to reminder birthday employees
    """,
    'license': 'LGPL-3',
    'author': 'Raúl F',
    'website': 'https://github.com/rauferdeveloper/reminder_birthday',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'data/cron.xml',
        'data/mail.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': ['static/description/icon.png'],
}