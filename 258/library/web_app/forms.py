from django import forms

class SugarForm(forms.Form):
    userid = forms.IntegerField()
    testid = forms.IntegerField()

class bpForm(forms.Form):
    uid = forms.IntegerField()
    tid = forms.IntegerField()

class presForm(forms.Form):
    uid = forms.IntegerField()
   

class doctorprofileForm(forms.Form):
    did = forms.IntegerField()
   
class patientprofileForm(forms.Form):
    uid = forms.IntegerField()
    mobile_no = forms.IntegerField()
   
   
