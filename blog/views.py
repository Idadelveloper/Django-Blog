from django.shortcuts import render


posts = [
    {
        'author': 'Ida',
        'title': 'Blog Post 1',
        'content': 'First post created',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Delphine',
        'title': 'Blog Post 2',
        'content': 'Second post created',
        'date_posted': 'August 28, 2018'
    }
]



# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})