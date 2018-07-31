from django.contrib import admin
from .models import PostView, Author, User

# Register your models here.
admin.site.register(Author)
admin.site.register(PostView)
admin.site.register(User)

