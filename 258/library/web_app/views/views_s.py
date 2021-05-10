from django.shortcuts import render, redirect
from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
from django.contrib import messages
import sys
import base64
from datetime import datetime
from datetime import date
from django.http import HttpResponse
from django.template.loader import get_template
import smtplib

# Create your views here.

def patientprofilerequest(request):
    cursor = connection.cursor()
    cursor.execute("""select * from requests """)
    print(cursor.rowcount)
    row = cursor.fetchall()
    requests=[]
    data={
            'requests':None
        }
    a = cursor.rowcount
    if a!=0:
             for n in range(a):
                 requests.append({
                     'uid':row[n][0],
                     'request_message':row[n][1],
                 })

             data = {
                'requests':requests,
            
             }
    return render(request,'web_app/patientprofilerequest.html',data)

def patientprofile(request):
   if request.method=='GET':
     userid = request.GET.get('uid',None)
     uname = request.GET.get('uname',None)
     mobile_no = request.GET.get('mobile_no',None)
     address = request.GET.get('address',None)
     email = request.GET.get('email',None)
     cursor = connection.cursor()
     try:
          cursor.execute("""update users SET username=%s,mobilenum=%s,address=%s,email=%s WHERE userid=%s && role='patient'  """,(uname,mobile_no,address,email,userid))
          cursor.execute("""delete from requests where uid=%s""",[userid])
          return render(request, 'patientprofile.html')
     finally:
          cursor.close()   
    
def doctorprofile(request):
  if request.method=='GET':
     dnum = request.GET.get('did',None)
     dname=request.GET.get('dname',None)
     specialisation=request.GET.get('specialisation',None)
     available_from=request.GET.get('available_from',None)
     available_till=request.GET.get('available_till',None)
     cursor=connection.cursor()
     cursor.execute("""update doctors SET dname=%s,specialisation=%s,available_from=%s,available_till=%s WHERE did=%s""",(dname,specialisation,available_from,available_till,dnum))
     return render(request, 'web_app/doctorprofile.html') 

def pres(request):
   if request.method=='GET':
       uid=request.GET.get('uid')
       dname=request.GET.get('dname',None)
       pres=request.GET.get('pres',None)
       date=request.GET.get('date',None)
     
       cursor=connection.cursor()
       try:
             cursor.execute("""SELECT * FROM users WHERE userid=%s """,[uid])       
             row = cursor.fetchall()
             a = cursor.rowcount
             cursor.execute("""SELECT * FROM doctors WHERE dname=%s """,[dname])       
             row = cursor.fetchall()
             b = cursor.rowcount
             if a!=0 and b!=0:
            
               cursor.execute("""INSERT INTO prescriptions(uid,docname,prescription,Day) VALUES (%s,%s,%s,%s)""",(uid,dname,pres,date))      
               return render(request, 'web_app/success.html')
             else:
                 messages.success(request,'enter correct credentials!!')
                 return render(request, 'web_app/pres.html')    
       finally:
            cursor.close()     