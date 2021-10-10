#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Spaceship(models.Model):
    _name = "academy.spaceship"
    _description = "Spaceship go zoommm!!!"
    
    dimension = fields.Float(string='Dimension', required=True)
    fuelType = fields.Selection(string="Fueltype", selection=[('regular', 'Regular'),('electrical','Electrical'),('nuclear','Nuclear')])
    shipType = fields.Selection(string="Shiptype", selection=[('small', 'Small'),('medium','Medium'),('large','Large')])
    numberOfPassengers = fields.Integer(string="Number of Passenger")
    isActive = fields.Boolean(string="Active", dafault=False)