from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted', 'author')

# Registering module to could see models in the admin GUI site
admin.site.register(Post, PostAdmin)
