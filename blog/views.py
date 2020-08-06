from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post


#def about(request):
#    return render(request, 'blog/about.html')

#def contact(request):
#    return render(request, 'blog/contact.html')


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name ='blog/update_post.html'
    fields = ['title', 'body']