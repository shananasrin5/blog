from django.shortcuts import render
from django.views.generic import CreateView, ListView,DetailView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy




# Create your views here.
class HomeView(ListView):
    model = Post
    template_name="home.html"
    ordering = ['-id']


    
class ArticleDetailView(DetailView):
  model=Post
  template_name='article_details.html'
    

class AddPostView(CreateView):
    model = Post
    template_name= 'add_post.html'
    fields= '__all__'
 
class UpdatePostView(UpdateView):
    model = Post
    template_name='edit.html'
    fields=['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name='delete_post.html'
    success_url = reverse_lazy('home')
    

