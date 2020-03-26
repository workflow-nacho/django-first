from django.contrib import admin
from .models import Post

# Registering module to could see models in the admin GUI site
admin.site.register(Post)
