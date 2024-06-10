from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import  (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
    )
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse



class PostListView(ListView):
    model = Post
    template_name ='blog_app/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog_app/about.html')



def home(request):
    
    context = {
        'posts' : Post.objects.all(),
        'title' : 'Fast Trading Blog'
    }
    return render(request, 'blog_app/home.html', context)



def blog_post_like(request, pk):
    """functionality for liking and unliking posts"""
    #checks if user is logged
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
    else:
        return HttpResponseRedirect(reverse('login'))
    
    redirect_to_home = request.POST.get('redirect_to_home', 'True')
    
    #if user associated to request is in likes list then removes like
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        #if request user not in like list, then adds 
        post.likes.add(request.user)

    #added feature for when clicking on list view it returns home
    #else it returns to the post detail view
    if redirect_to_home == 'True':
        return HttpResponseRedirect(reverse('blog-home'))
    else:
        return HttpResponseRedirect(reverse('post-detail', kwargs={'pk': pk}))