from .models import Student
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete,pre_init,post_init
from django.dispatch import receiver
from studentapi.settings import EMAIL_HOST_USER
from .tasks import student_send_mail

# # pre_init signal
# @receiver(pre_init, sender=Student)
# def at_beginning_init(sender, *args, **kwargs):
#  print("-----------------------------------------")
#  print("PRE INIT SIGNAL")
#  print('Sender:', sender)
#  print(f'Args: {args}')
#  print(f'Kwargs: {kwargs}')

# # post_init signal
# @receiver(post_init, sender=Student)
# def at_ending_init(sender, *args, **kwargs):
#  print("-----------------------------------------")
#  print("POST INIT SIGNAL")
#  print('Sender:', sender)
#  print(f'Args: {args}')
#  print(f'Kwargs: {kwargs}')



# pre_save signal
@receiver(pre_save,sender=Student)
def before_save(sender,instance,**kwargs):
     print("-------------------------")
     print('PRE SAVE SIGNAL')
     print('Sender:', sender)
     print('instance:' ,instance)

# post_save signal
@receiver(post_save, sender=Student)
def after_save(sender, instance, created, **kwargs):
    if created:
        print("-------------------------")
        print('POST SAVE SIGNAL')
        print('Sender:', sender)
        print('instance:' ,instance)
        print('created:', created)

        # sending mail via signal using instance

        # stu = Student.objects.get(first_name=instance)

        # student_send_mail.delay({'email':stu.email,'host':EMAIL_HOST_USER,'user':stu.first_name})

    else:
        print("-------------------------")
        print('POST SAVE UPDATE SIGNAL')
        print('Sender:', sender)
        print('instance:' ,instance)
        print('created:', created)


# pre_delete signals
@receiver(pre_delete,sender=Student)
def before_delete(sender,instance,**kwargs):
    print("-------------------------")
    print('PRE DELETE SIGNAL')
    print('Sender:', sender)
    print('instance:' ,instance)

# post_delete signals
@receiver(post_delete,sender=Student)
def after_delete(sender,instance,**kwargs):
    print("-------------------------")
    print('POST DELETE SIGNAL')
    print('Sender:', sender)
    print('instance:' ,instance)

