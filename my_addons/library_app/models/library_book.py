from odoo import api, fields, models
from odoo.exceptions import Warning
class Book(models.Model):
 def _check_isbn(self):
      self.ensure_one()
      digits = [int(x) for x in self.isbn if x.isdigit()]
      if len(digits) == 13:
           ponderations = [1, 3] * 6
           terms = [a * b for a, b in zip(digits[:12], ponderations)]
           remain = sum(terms) % 10
           check = 10 - remain if remain != 0 else 0
           return digits[-1] == check              
 def button_check_isbn(self):
      for book in self:
            if not book.isbn:
                  raise Warning('Please provide an ISBN for %s' % book.name)
            if book.isbn and not book._check_isbn():
                  raise Warning('%s is an invalid ISBN' % book.isbn)
      return True
 _name = 'library.book'
 _description = 'Book'
 name = fields.Char('Title', required=True)
 isbn = fields.Char('ISBN')
 active = fields.Boolean('Active?', default=True)
 date_published = fields.Date()
 image = fields.Binary('Cover')
 publisher_id = fields.Many2one('res.partner', string='Publisher')
 author_ids = fields.Many2many('res.partner', string='Authors')
 isbn = fields.Char('ISBN')
 book_type = fields.Selection(
   [('paper','Paperback'),
   ('hard','Hardcover'),
   ('electronic','Electronic'),
   ('other', 'Other')],
   'Type')
 notes = fields.Text('Internal Notes')
 descr = fields.Html('Description')
 # Numeric fields:
 copies = fields.Integer(default=1)
 avg_rating = fields.Float('Average Rating', (3, 2))
 price = fields.Monetary('Price', 'currency_id')
 currency_id = fields.Many2one('res.currency') # price helper
 # Date and time fields:
 date_published = fields.Date()
 last_borrow_date = fields.Datetime(
     'Last Borrowed On',
     default=lambda self: fields.Datetime.now())
 publisher_country_id = fields.Many2one(
     'res.country', string='Publisher Country',
      compute='_compute_publisher_country',
)
 @api.depends('publisher_id.country_id')
 def _compute_publisher_country(self):
     for book in self:
           book.publisher_country_id = book.publisher_id.country_id 
