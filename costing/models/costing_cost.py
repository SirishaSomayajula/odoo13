from odoo import fields, models
class cost(models.Model):
  _name = 'costing.cost'
  _description = ('Cost')
  name = fields.Char('name')
  Type = fields.Char('Type')
  season = fields.Char('Season')
  style = fields.Char('Style/Ref name')
  pricelist = fields.Char('Pricelist')
  currency = fields.Char('Currency')
  stage = fields.Char('Stage')
  customer_id = fields.Many2one('res.partner', string='Customer')
  company_id = fields.Many2one('res.partner', string='Company')
  def name_get(self):
        names = []
        for rec in self:
            name = '%s/%s' % (rec.customer_id, rec.company_id)
            names.append((rec.id, name))
        return names

#      Cost_sheet_details = fields.Text(string='Cost sheet details')
 #     order_quantity = fields.Text(string='order quantity')
  #    sample_size = fields.Text(string='sample size')
   #   size = fields.Text(string='size')
    #  specifications = fields.Text(string='specifications')
     # merch_of_division = fields.Text(string='merch of division')
      #merch_fabrication = fields.Text(string='merch fabrication')
      #merch_size_offerings = fields.Text(string='merch_size_offerings')
     # pattern = fields.Text(string='pattern')
