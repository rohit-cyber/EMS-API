from django.core.management.base import BaseCommand
from studentapi.settings import EMAIL_HOST_USER
from api.tasks import ems_send_mail
from api.models import Student

class Command(BaseCommand):

    def handle(self,*args,**options):

        student = Student.objects.all()
        email_list = [i.email for i in student]

        for email in email_list:

            unique = Student.objects.get(email=email)

            ems_send_mail.delay({'email':email,'host':EMAIL_HOST_USER,'user':unique.first_name})
        
        self.stdout.write(self.style.SUCCESS('Mail Sent'))