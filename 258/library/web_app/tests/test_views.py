from django.test import TestCase, Client
from django.urls import reverse
from web_app.views import views_s
import json

class TestViews(TestCase):
    def setUp(self):
      self.client = Client()
      self.patientprofilerequest_url = reverse('patientprofilerequest')
      self.patientprofile_url = reverse('patientprofile',)

    def test_patientprofilerequest_GET(self):
     
      response = self.client.get(self.patientprofilerequest_url)
      self.assertEquals(response.status_code, 200)
      self.assertTemplateUsed(response,'web_app/patientprofilerequest.html')

    def test_patientprofile_GET(self):

      response = self.client.get(self.patientprofile_url)
      self.assertEquals(response.status_code, 200)
      self.assertTemplateUsed(response,'web_app/patientprofile.html')
