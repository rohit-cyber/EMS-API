from __future__ import absolute_import, unicode_literals
from .serializers import RegisterSerializer,ProfileSerializer
from myapp.models import Profile
from ems.celery import app
from django.core.mail import send_mail
from celery.decorators import periodic_task
from celery.schedules import crontab
from django.template import loader

@periodic_task(run_every=(crontab(minute='*/1')))
def add():
    x=10
    y=20
    print(x+y)

@app.task
def ems_send_mail(args):
    host = args.get('host')
    mail = args.get('email')
    user = args.get('user')
    ctx =   {
                'user_name': user,
                'subject':  'Your mail id will be ' + mail
            }       

    html_message = loader.render_to_string('email.html',context=ctx)


    send_mail('New Registration',
              "Welcome To EMS",
              host,
              [mail],
              html_message=html_message,
              fail_silently=False)


    
