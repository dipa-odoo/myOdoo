#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Spaceship(models.Model):
    _name = "academy.orgTask"
    _description = "Organization tasks"
    
    name = fields.Char("Name")
    description = fields.Text("Description")
    taskType = fields.Selection(string="Task Type", selection=[('regular', 'Regular'),('electrical','Electrical'),('nuclear','Nuclear')])
    
    #[('Internal','internal'),('External','external')]
    
    startTime = fields.Datetime(string="Start time", default = lambda self: fields.datetime.now(), required=True)
    endTime = fields.Datetime(string="End time", default = lambda self: fields.datetime.now(), required=True)
    recurring = fields.Booleans(string="repeating",required=True, default=False)