from django.contrib import admin
from .models import Post,Follower_list,Following_list

admin.site.register(Post)
admin.site.register(Follower_list)
admin.site.register(Following_list)
