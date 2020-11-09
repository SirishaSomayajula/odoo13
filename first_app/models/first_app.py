from odoo import fields, models
class app(models.Model):
  _name = 'first.app'
  _description = ('app')
class Project(models.Model):
    _inherit = "project.project"
    _description = "Project"
    _order = "sequence, name, id"
    _rating_satisfaction_days = False  # takes all existing ratings
    _check_company_auto = True

