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

            ems_send_mail.delay({'email':email,
                                  'id':unique.id,
                                  'host':EMAIL_HOST_USER,
                                  'first_name':unique.first_name,
                                  'last_name':unique.last_name,
                                  'standard':unique.standard,
                                  'city':unique.city,
                                  'active':unique.active,
                                  'joined_on':unique.joined_on
                                  })
            
            self.stdout.write(self.style.SUCCESS('Mail {} Sent Successfully'.format(unique.id)))
        self.stdout.write(self.style.SUCCESS(' All Mail Sent'))