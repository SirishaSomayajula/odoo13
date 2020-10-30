from odoo.tests.common import TransactionCase
class TestCost(TransactionCase):
    def setUp(self, *args, **kwargs):
       result = super().setUp(*args, **kwargs)
       user_admin = self.env.ref('base.user_admin')
       self.env= self.env(user=user_admin)
       self.Cost = self.env['Costing.cost']
       self.cost_ode = self.Cost.create({
           'name': 'new',
       return result
