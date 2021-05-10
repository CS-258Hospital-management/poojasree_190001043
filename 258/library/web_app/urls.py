from django.urls import path
from .views import views_a
from .views import views_s
from .views import views_m
from .views import views_r


urlpatterns = [    path('home', views_m.home, name = 'home'),
    path('homeuser', views_a.homeuser, name = 'homeuser'),
    path('',views_m.adminlogin,name='adminlogin'),
    path('library', views_m.library, name = 'library'),
    path('userlog', views_a.userlog, name = 'userlog'),
    path('register', views_a.register, name = 'register'),
    path('userregister', views_a.userregister, name = 'userregister'),
    path('userloginfill', views_a.userloginfill, name = 'userloginfill'),
    path('ViewDoctorProfile', views_a.ViewDoctorProfile, name ='ViewDoctorProfile'),
    path('Medicines', views_a.Medicines, name = 'Medicines'),
    path('diabetes', views_a.diabetes, name = 'diabetes'),
    path('bp', views_a.bp, name = 'bp'),
    path('vaccinefill', views_a.vaccinefill, name = 'vaccinefill'),
    path('vaccineapp', views_a.vaccineapp, name = 'vaccineapp'),
    path('doctorfill', views_a.doctorfill, name = 'doctorfill'),
    path('doctorapp', views_a.doctorapp, name = 'doctorapp'),
    path('userpage', views_a.userpage, name = 'userpage'),
    path('diabcategory',views_m.diabcategory,name = 'diabcategory'),
    path('bpcategory',views_m.bpcategory,name = 'bpcategory'),
    path('patientprofile',views_s.patientprofile,name = 'patientprofile'),
    path('patientprofilerequest',views_s.patientprofilerequest,name = 'patientprofilerequest'),
    path('doctorprofile',views_s.doctorprofile,name = 'doctorprofile'),
    path('pharmadd',views_m.pharmadd,name = 'pharmadd'),
    path('pharmupdate',views_m.pharmupdate,name = 'pharmupdate'),
    path('pres',views_s.pres,name = 'pres'),
    path('billing',views_m.billing,name = 'billing'),
    path('adlog',views_m.adlog,name = 'adlog'), 
    path('credfill',views_m.credfill,name = 'credfill'), 
    path('sugarfill',views_m.sugarfill,name = 'sugarfill'), 
    path('bpfill',views_m.bpfill,name = 'bpfill'), 

]

