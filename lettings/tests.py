""" Test case Lettings app """

from django.test import TestCase
from django.urls import reverse

from lettings.models import Letting

# Create tests for the models Letting and Address here.
# Create tests for the views index and details here.
# Create tests for the custom 404 and 500 views here.


class LettingsTestClass(TestCase):
    """Test Lettings URL"""

    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_index(self):
        """page should contain <title>Lettings</title>"""
        response = self.client.get(reverse("lettings:index"))
        assert response.status_code == 200
        self.assertEqual(True, b"<title>Lettings</title>" in response.content)

    def test_404(self):
        """page should contain <title>404 Page Not Found</title>"""
        response = self.client.get(reverse("dfdnk"))
        assert response.status_code == 404
        self.assertEqual(True, b"<title>404 Page Not Found</title>" in response.content)

    def test_lettings(self):
        """page should contain <title>lettings title value</title>"""
        Lettings_tests = Letting.objects.all()
        for letting in Lettings_tests:
            response = self.client.get(reverse("lettings:details", args=[letting.id]))
            assert response.status_code == 200
            print(letting.title)
            self.assertInHTML(letting.title, str(response.content))
