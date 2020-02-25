from django.test import TestCase
from .models import Projects

# Create your tests here.
class ProjectsTest(TestCase):
    """
    Here we'll define the test that we'll run against our Project models
    """
    def test_str(self):
        test_name = Projects(name='A project')
        self.assertEqual(str(test_name), 'A project')