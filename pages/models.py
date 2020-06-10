from django.db import models
from account.models import Profile
#from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver


#class UserProfile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#    birth_date = models.DateField(null=True, blank=True)
#    location = models.CharField(max_length=30, blank=True)
#    photo = models.ImageField(upload_to='static/photo/', 
#    	height_field=None,
#    	width_field=None, 
#    	max_length=100
#    	)
    
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()    

#class CorporateUser(models.Model):
#    profile = models.ForeignKey(UserProfile)


#    class Meta:
#        db_table = 'corporate_user'



class Post(models.Model):
	text = models.TextField()
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Моряк')

	def __str__(self):
		return self.text[:50]