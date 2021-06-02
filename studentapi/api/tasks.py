from __future__ import absolute_import, unicode_literals
from studentapi.celery import app
from django.core.mail import send_mail
from celery.decorators import periodic_task
from celery.schedules import crontab
from django.template import loader
from api.models import Student,Guardian

@periodic_task(run_every=(crontab(minute='*/1')))
def add():
    x=10
    y=20
    print(x+y)

#student_registration email
@app.task
def student_send_mail(args):
    host = args.get('host')
    mail = args.get('email')
    user = args.get('user')
    ctx =   {
                'user_name': user,
                'subject':  'Your mail id will be ' + mail
            }       

    html_message = loader.render_to_string('student_registration_email.html',context=ctx)


    send_mail('New Registration',
              "Welcome To EMS",
              host,
              [mail],
              html_message=html_message,
              fail_silently=False)




# student_details_email sending through command line
@app.task
def ems_send_mail(args):
    host = args.get('host')

    stu = {
            'first_name': args.get('first_name'),
            'last_name': args.get('last_name'),
            'id': args.get('id'),
            'email': args.get('email'),
            'standard': args.get('standard'),
            'city': args.get('city'),
            'active':args.get('active'),
            'joined_on': args.get('joined_on'),   
            } 
    

    stud = Student.objects.get(email=args.get('email'))
    guar = Guardian.objects.filter(student=stud)
          

    html_message = loader.render_to_string('student_detail_email.html',{'student':stu,'guardian':guar})


    send_mail('Complete Student Detail',
              "Student Details",
              host,
              [args.get('email')],
              html_message=html_message,
              fail_silently=False)


    
