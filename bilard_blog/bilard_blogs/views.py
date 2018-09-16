from django.shortcuts import render
#from django.http import HttpResponse
from .models import PostView

# Create your views here.


def index(request):
	latest_blog_post = PostView.objects.order_by('-date_posted')[:10]

	context = {'latest_blog_post':latest_blog_post}
	return render(request, 'bilard_blogs/index.html', context)
	#for blog in latest_blog_post:
	#	return HttpResponse(blog)
	#return HttpResponse("<h2>It's working!!!</h2>")

def post(request, post_id):
	article = PostView.objects.get(pk=post_id)
	blog_article = article.post
	context = {"blog_article":blog_article}
	return render(request, 'bilard_blogs/post.html', context)


def about(request):
	return render(request, 'bilard_blogs/bilard.html')

def contact_us(request):
	return render(request, 'bilard_blogs/contact_us.html')