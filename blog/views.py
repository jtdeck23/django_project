from django.shortcuts import render

posts = [
    {
        'author': 'Jordan Deck',
        'title': 'First Blog Post',
        'content': 'First Post Losers',
        'date_posted': 'May 1, 2020'
    },
    {
        'author': 'Akacyea Deck',
        'title': 'Second Blog Post',
        'content': 'Second Post Losers',
        'date_posted': 'August 5, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
