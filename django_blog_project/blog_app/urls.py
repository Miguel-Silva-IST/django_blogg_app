from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, blog_post_like
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('post/<int:pk>/like/', views.blog_post_like, name = 'post-like'),
    path('about/', views.about, name = 'blog-about'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users_app/login.html'), name = 'login'),
    
]
