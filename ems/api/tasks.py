from __future__ import absolute_import, unicode_literals
from .serializers import RegisterSerializer,ProfileSerializer
from myapp.models import Profile
from ems.celery import app
from django.core.mail import send_mail

@app.task
def add(x,y):
    print(x+y)

@app.task
def ems_send_mail(args):
    host = args.get('host')
    mail = args.get('email')


    send_mail('New Registration',
              "Welcome To EMS",
              host,
              [mail],
              fail_silently=False)
    
