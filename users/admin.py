#from django.contrib import admin
#from django.contrib.auth import get_user_model
#from django.contrib.auth.admin import UserAdmin

#from .forms import CustomUserCreationForm, CustomUserChangeForm
#from .models import CustomUser



#class CustomUserAdmin(UserAdmin):
#    add_form = CustomUserCreationForm
#    form = CustomUserChangeForm
#    model = CustomUser
#    list_display = ['email', 'username', 'birth_date', 'location']

#admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib import admin
from .models import Profile
@admin.register(Profile)




class ProfileAdmin(admin.ModelAdmin):
 list_display = ['user', 'date_of_birth', 'photo']