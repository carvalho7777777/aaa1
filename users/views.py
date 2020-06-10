from django.shortcuts import render
from .models import Profile
from allauth.account.forms import SignupForm
#from .models import CustomUser
from .forms import  ProfileEditForm



def index(request):
    return render(request, "profile.html", {})



#def profiles_list(request):
#    prpfiles = CustomUser.objects.all()
#    return render(request, 'profile_list.html', context = {'profiles' : profiles})    


#def profile_detail(request, slug):
#    post = Post.objects.get(slug__iexact = slug)
#    return render(request, 'profile.html', context = {'profile' : profile})


class MyCustomSignupForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        
        # Создание профиля пользователя.
        Profile.objects.create(user=new_user).save(request)

        # Add your own processing here.
        # You must return the original result.
        return user




@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',
                {'user_form': user_form,'profile_form': profile_form})

