from django.shortcuts import render
from django.http import HttpResponse
from .models import PostView

# Create your views here.

def index(request):
	latest_blog_post = PostView.objects.order_by('-date_posted')[:10]
	for blog in latest_blog_post:
		return HttpResponse(blog)
	#return HttpResponse("<h2>It's working!!!</h2>")
