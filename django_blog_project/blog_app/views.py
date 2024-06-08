from django.shortcuts import render

posts = [
    {'author' : 'Miguel Silva',
     'title' : 'HFT : Introduction',
     'content' : 'sample content',
     'date' : '01/01/2025'
     },
     {'author' : 'Edu Faria',
     'title' : 'Trading in Surfing',
     'content' : 'sample content',
     'date' : '01/01/2026'
     }
]

def home(request):
    
    context = {
        'posts' : posts,
        'title' : 'Fast Trading Blog'
    }
    return render(request, 'blog_app/home.html', context)


def about(request):
    return render(request, 'blog_app/about.html')


