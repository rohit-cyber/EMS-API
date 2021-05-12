from django.core.management.base import BaseCommand
from ems.settings import EMAIL_HOST_USER
from api.tasks import ems_send_mail
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self,*args,**options):

        user = User.objects.all()
        email_list = [i.email for i in user]

        for email in email_list:

            unique = User.objects.get(email=email)

            ems_send_mail.delay({'email':email,'host':EMAIL_HOST_USER,'user':unique.first_name})
        
        self.stdout.write(self.style.SUCCESS('Mail Sent'))