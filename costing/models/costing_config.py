from odoo import fields, models


class Configuration(models.Model):
    _name = 'configuration'
    _description = 'Configuration'
    _order = 'sequence,name'


    name = fields.Char()
    priliminary_costing = fields.Boolean()
    buyer_approved_costing = fields.Boolean()
    factory_approved_costing = fields.Boolean()
    


