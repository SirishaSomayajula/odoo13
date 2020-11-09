from odoo.tests.common import TransactionCase
class TestProject(TransactionCase):
 def test_create_data(self):
        test_project = self.env['project.project'].create({
            'name': 'TestProject'
        })
        test_project_task = self.env['project.task'].create({
            'name': 'ExampleTask',
            'project_id': test_project.id
        })
        self.assertEqual(test_project.name, 'TestProject')
        self.assertEqual(test_project_task.name, 'ExampleTask')
        self.assertEqual(test_project_task.project_id.id, test_project.id)
        print('Your test was succesfull!')

