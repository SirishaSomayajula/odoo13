from odoo import fields, models


class Configuration(models.Model):
    _name = 'configuration'
    _description = 'Configuration'
    _order = 'sequence,name'
    
   _name = 'costing stages'
   _description = 'Costing stages'
   _order = 'sequence,name'
