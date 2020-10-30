from odoo import fields, models
class Book(models.Model):
  _name = 'costing'
  _description = ('Cost')
  name = fields.Char('Name', required=True)
  approvals = fields.Char('approvals')
  role = fields.Char('role')
  users= fields.Char('users')
  approval_type = fields.Char('approval type')
  folded_in_kanban_view = fields.Boolean( )
  allow_to_apply_changes = fields.Boolean( )
  final_stage = fields.Boolean( )
