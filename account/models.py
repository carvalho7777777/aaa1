from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


#class CustomUser(AbstractUser):
#    type_choices = (
#        ('SU', 'Пользователь'),
#        ('CU', 'Компания'),
#    )
#    user_type = models.CharField(max_length=2,
#                                 choices=type_choices,
#                                 default='SU')
#    photo = models.ImageField('фотография', upload_to='users/%Y/%m/%d/', blank=True)
#    phone = models.CharField('телефон', max_length=140, blank=True, null=True)

#class Profile(CustomUser):
#    date_of_birth = models.DateField('дата рождения', blank=True, null=True)
#    position = models.CharField('должность', max_length=200, blank=True, null=True)

#class CompanyDetails(CustomUser):
#     title = models.CharField('название компании', max_length=200, blank=True, null=True)

############################################
############################################

#class TypeProfile(models.Model):
#    PROFILE_TYPES = (
#    (u'INDV', 'Individual'),
#    (u'CORP', 'Corporate'),
#)
#    type_profile = models.CharField(choices=PROFILE_TYPES, default=None)
    


#class UserProfile(models.Model):
#    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    type_profile = models.OneToOneField(TypeProfile, max_length=16, on_delete=models.CASCADE)   


#class Profile(models.Model):
#    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#    date_of_birth = models.DateField('дата рождения', blank=True, null=True)
#    photo = models.ImageField('фотография', upload_to='users/%Y/%m/%d/', blank=True)
    #user_balance = models.IntegerField(default=0)
#    phone = models.CharField('телефон', max_length=140, blank=True, null=True)
#    position = models.CharField('должность', max_length=200, blank=True, null=True)
    


####################################################
####################################################
#class User(AbstractUser):
    #location = models.CharField(max_length=30, blank=True)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_profile = True
    pid = models.AutoField(unique=True, primary_key=True) #patient identification
    date_of_birth = models.DateField('дата рождения', blank=True, null=True)
    photo = models.ImageField('фотография', upload_to='users/%Y/%m/%d/', blank=True)
    #user_balance = models.IntegerField(default=0)
    phone = models.CharField('телефон', max_length=140, blank=True, null=True)
    position = models.CharField('должность', max_length=200, blank=True, null=True)
    

#    class Meta:
#        db_table = 'individual_user'
 
    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    #instance.profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


#class Company(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    user.is_company = True
#    pin = models.AutoField(primary_key=True) #unique physician identification number
#    title = models.CharField('название компании', max_length=200, blank=True, null=True)
    
#    class Meta:
#        db_table = 'corporate_user'

#    def __str__(self):
#        return 'Профиль пользователя {}'.format(self.user.username)    


