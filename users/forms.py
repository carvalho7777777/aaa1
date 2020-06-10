from django import forms
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from .models import CustomUser



#class CustomUserCreationForm(UserCreationForm):

#    class Meta(UserCreationForm):
#        model = CustomUser
 #       fields = ('username', 'email')

#class CustomUserChangeForm(UserChangeForm):

#    class Meta:
#        model = CustomUser
#        fields = ('username', 'email')


from .models import Profile



#class UserEditForm(forms.ModelForm):
    
#    class Meta:
#        model = User
#        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
