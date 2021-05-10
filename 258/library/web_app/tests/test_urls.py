from django.test import SimpleTestCase
from django.urls import reverse,resolve
from web_app.views import sugarfill,bpfill

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse(('sugarfill'))
        print(resolve(url))
        self.assertEquals(resolve(url).func,sugarfill)

    
        
