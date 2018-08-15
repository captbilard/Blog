from django.shortcuts import render
from django.http import HttpResponse
from .models import PostView

# Create your views here.

"""Where to pick up from, I need to adjust my views in such a way that it displays post based on the latest one
then link the views to the html file already on ground. 
"""

def index(request):
	latest_blog_post = PostView.objects.order_by('-date_posted')
	for blog in latest_blog_post:
		return HttpResponse(blog)
	#return HttpResponse("<h2>It's working!!!</h2>")

def homepage(request):
	return render(request, 'bilard_blogs/index.html')