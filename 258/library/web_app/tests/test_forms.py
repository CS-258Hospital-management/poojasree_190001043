from django.test import SimpleTestCase
from web_app.forms import SugarForm,bpForm,doctorprofileForm,presForm,patientprofileForm,docappform,vaccineappform

class TestForms(SimpleTestCase):

    def test_sugar_form_valid_data(self):
        form = SugarForm(data={
            'userid' : 1,
            'testid' : 2
        })
        
        self.assertIsNone('userid')


    def test_sugar_form_no_data(self):
            form = SugarForm(data={})
            self.assertFalse(form.is_valid())
            self.assertEquals(len(form.errors),2)

    def test_bp_form_valid_data(self):
        form = bpForm(data={
            'uid' : 1,
            'tid' : 2
        })
        self.assertTrue(form.is_valid())


    def test_bp_form_no_data(self):
            form = bpForm(data={})

            self.assertFalse(form.is_valid())
            self.assertEquals(len(form.errors),2)        

    
    def test_pres_form_valid_data(self):
        form = presForm(data={
            'uid' : 1,
        })
        self.assertTrue(form.is_valid())


    def test_pres_form_no_data(self):
            form = presForm(data={})

            self.assertFalse(form.is_valid())
            self.assertEquals(len(form.errors),1)  

    def test_patientprofile_form_valid_data(self):
        form = patientprofileForm(data={
            'uid' : 1,
            'mobile_no' : 1122334455
        })
        self.assertIsNone('mobile_no')
        self.assertTrue(form.is_valid())


    def test_patientprofile_form_no_data(self):
            form = patientprofileForm(data={})

            self.assertFalse(form.is_valid())
            self.assertEquals(len(form.errors),2) 

    def test_doctorprofile_form_valid_data(self):
            form = doctorprofileForm(data={
               'did' : 1
            })
            self.assertTrue(form.is_valid())


    def test_doctorprofile_form_no_data(self):
            form = doctorprofileForm(data={})

            self.assertFalse(form.is_valid())
            self.assertEquals(len(form.errors),1) 
    
    def test_docapp_form_valid_data(self):
         form = docappform(data={
            'user_id' : 1,
        })
        self.assertTrue(form.is_valid())
    
    def test_vaccineapp_form_valid_data(self):
        form = vaccineappform(data={
            'u_id' : 1,
        })
     