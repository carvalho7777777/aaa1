#from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

#class CustomUser(AbstractUser):
#    slug = models.SlugField(max_length=150, unique = True)
#    birth_date = models.DateField(null=True, blank=True)
#    location = models.CharField(max_length=30, blank=True)
    
#    def get_absolute_url(self):
#        return reverse('post_detail_url', kwargs={'slug': self.slug})



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    

    def __str__(self):
        return 'Профиль моряка {}'.format(self.user.username)


