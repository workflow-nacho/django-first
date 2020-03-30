from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Creating models here.
# Part 5. https://www.youtube.com/watch?v=aHC3uTkT9r8&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=5
# To get the author for each post who will be the user who create the post,
# Now our user is in separate table, so we need to import the user model "from django.contrib.auth.models import User"
# Relationship: User are going to author post 
# => one to many relationship using Foreign key => "author = models.ForeignKey(User)"
# Do not forget to migrate changes: python manage.py makemigrations => result succesfully =>
# Migrations for 'blog':
#   blog\migrations\0001_initial.py
#     - Create model Post
# To migrate Running migrations: => python manage.py migrate
# To see in the CLI the SQL code we run python manage.py sqlmigrate blog 0001

# This is the first table we go to create
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Exact time when post is created. 
    # Passing function now withow parenthesis in render to execute it when we add the post
    date_posted = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Creating a dunde STR method
    def __str__(self):
        return self.title

    # Creating a get absolute url method
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
