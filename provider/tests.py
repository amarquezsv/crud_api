from django.test import TestCase
from provider.models import Providers

class ProvidersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.providers = Providers.objects.create(
        name="Office Depot",
        address="North Military Trail Boca Raton, FL 33496",
        phone="1-888-263-3423",
        description="A description of text here"
        )

    def test_model_content(self):
        self.assertEqual(self.providers.name, "Office Depot")
        self.assertEqual(self.providers.address, "North Military Trail Boca Raton, FL 33496")
        self.assertEqual(self.providers.phone, "1-888-263-3423")
        self.assertEqual(self.providers.description, "A description of text here")
        self.assertEqual(str(self.providers), "Office Depot")


