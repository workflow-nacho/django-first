from django.shortcuts import render

# Creating Fake posts into a list with some information in a dictionary
posts = [
    {
        'author': 'CoreyMS',
        'student': 'Nacho',
        'title': 'Blog post one',
        'content': 'First post content',
        'date_posted': 'March 26, 2020'
    },
    {
        'author': 'Nacho RM',
        'title': 'Blog post two',
        'content': 'Second post content',
        'date_posted': 'March 27, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })