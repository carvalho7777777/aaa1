#from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Post



class ListPostView(ListView):
	model = Post
	template_name = 'home.html'


class DetailPostView(DetailView):
	model = Post
	template_name = 'post_detail.html'




#class HomePageView(TemplateView):
#	template_name = 'home.html'


